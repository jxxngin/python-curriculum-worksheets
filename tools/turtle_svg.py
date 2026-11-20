"""터틀 프로그램을 창 없이 실행해 그림을 SVG로 만든다(2학기 교안의 "완성하면 이렇게 돼요"·도구 카드용).

    from turtle_svg import record
    svg = record(src, inputs)        # src를 실행하고 그린 그림을 <svg> 문자열로

- 진짜 turtle 대신 기록용 가짜 모듈을 sys.modules['turtle']에 끼워 실행한다. 창을 띄우지 않는다.
- 선·채우기·점·글자를 실행 순서대로 기록하고, 채우기는 begin_fill 자리에 놓아 그 뒤에 그린 선이 위에 보이게 한다(진짜 터틀과 같음).
- circle()은 파이썬 turtle과 같은 방식(여러 개의 짧은 직선)으로 계산한다.
- 지원하지 않는 기능을 쓰면 AttributeError가 나서 바로 알 수 있다.
"""
import math
import sys
import types
from html import escape

COLORS_OK = None  # 색 이름은 그대로 SVG에 넘긴다(SVG도 CSS 색 이름을 안다)


class Canvas:
    def __init__(self):
        self.items = []          # ('line', pts, color, width) / ('fill', idx) / ('dot', x, y, size, color) / ('text', ...)
        self.bg = 'white'
        self.title = ''


class FakeTurtle:
    def __init__(self, canvas):
        self._c = canvas
        self._x = self._y = 0.0
        self._h = 0.0
        self._down = True
        self._color = 'black'
        self._fill = 'black'
        self._width = 1
        self._path = None        # 지금 그리는 선(점 목록)
        self._fill_pts = None
        self._fill_slot = None
        self._visible = True

    # ---- 그리기 내부
    def _start_path(self):
        if self._down and self._path is None:
            self._path = [(self._x, self._y)]
            self._c.items.append(['line', self._path, self._color, self._width])

    def _end_path(self):
        self._path = None

    def _moveto(self, x, y):
        if self._down:
            self._start_path()
            self._path.append((x, y))
        if self._fill_pts is not None:
            self._fill_pts.append((x, y))
        self._x, self._y = float(x), float(y)

    # ---- 움직이기
    def forward(self, d):
        r = math.radians(self._h)
        self._moveto(self._x + d * math.cos(r), self._y + d * math.sin(r))
    fd = forward

    def backward(self, d):
        self.forward(-d)
    bk = back = backward

    def left(self, a):
        self._h = (self._h + a) % 360
    lt = left

    def right(self, a):
        self._h = (self._h - a) % 360
    rt = right

    def goto(self, x, y=None):
        if y is None:
            x, y = x
        self._moveto(x, y)
    setpos = setposition = goto

    def setx(self, x):
        self._moveto(x, self._y)

    def sety(self, y):
        self._moveto(self._x, y)

    def setheading(self, a):
        self._h = a % 360
    seth = setheading

    def home(self):
        self.goto(0, 0)
        self._h = 0.0

    def circle(self, radius, extent=None, steps=None):
        if extent is None:
            extent = 360
        if steps is None:
            frac = abs(extent) / 360
            steps = 1 + int(min(11 + abs(radius) / 6.0, 59.0) * frac)
        w = 1.0 * extent / steps
        w2 = 0.5 * w
        l = 2.0 * radius * math.sin(math.radians(w2))
        if radius < 0:
            l, w, w2 = -l, -w, -w2
        self.left(w2)
        for _ in range(steps):
            self.forward(l)
            self.left(w)
        self.left(-w2)

    # ---- 펜
    def penup(self):
        self._down = False
        self._end_path()
    pu = up = penup

    def pendown(self):
        self._down = True
    pd = down = pendown

    def isdown(self):
        return self._down

    def pensize(self, w=None):
        if w is None:
            return self._width
        self._width = w
        self._end_path()
    width = pensize

    def pencolor(self, *c):
        if not c:
            return self._color
        self._color = _col(c)
        self._end_path()

    def fillcolor(self, *c):
        if not c:
            return self._fill
        self._fill = _col(c)

    def color(self, *c):
        if not c:
            return self._color, self._fill
        if len(c) == 2:
            self.pencolor(c[0])
            self.fillcolor(c[1])
        else:
            self.pencolor(*c)
            self.fillcolor(*c)

    def begin_fill(self):
        self._fill_pts = [(self._x, self._y)]
        self._fill_slot = ['fill', None, None]
        self._c.items.append(self._fill_slot)
        self._end_path()

    def end_fill(self):
        if self._fill_pts is not None:
            self._fill_slot[1] = list(self._fill_pts)
            self._fill_slot[2] = self._fill
        self._fill_pts = None

    def dot(self, size=None, *c):
        size = size or max(self._width + 4, self._width * 2)
        self._c.items.append(['dot', self._x, self._y, size, _col(c) if c else self._color])

    def write(self, text, move=False, align='left', font=('Arial', 8, 'normal')):
        self._c.items.append(['text', self._x, self._y, str(text), align, font, self._color])

    # ---- 알아보기
    def position(self):
        return (round(self._x, 6), round(self._y, 6))
    pos = position

    def xcor(self):
        return round(self._x, 6)

    def ycor(self):
        return round(self._y, 6)

    def heading(self):
        return self._h

    def distance(self, x, y=None):
        if y is None:
            x, y = x
        return math.hypot(x - self._x, y - self._y)

    # ---- 화면에 영향이 없는 것
    def speed(self, *a):
        pass

    def shape(self, *a):
        pass

    def hideturtle(self):
        self._visible = False
    ht = hideturtle

    def showturtle(self):
        self._visible = True
    st = showturtle

    def clear(self):
        self._c.items.clear()
        self._end_path()


class FakeScreen:
    def __init__(self, canvas):
        self._c = canvas

    def bgcolor(self, *c):
        self._c.bg = _col(c)

    def title(self, t):
        self._c.title = t

    def setup(self, *a, **k):
        pass

    def tracer(self, *a, **k):
        pass

    def update(self):
        pass

    def mainloop(self):
        pass
    done = exitonclick = mainloop


def _col(c):
    if len(c) == 1 and isinstance(c[0], tuple):
        c = c[0]
    if len(c) == 3:
        r, g, b = (int(v * 255) if isinstance(v, float) and v <= 1 else int(v) for v in c)
        return f'#{r:02x}{g:02x}{b:02x}'
    return str(c[0])


def fake_module(canvas):
    m = types.ModuleType('turtle')
    default = FakeTurtle(canvas)
    screen = FakeScreen(canvas)
    m.Turtle = m.Pen = m.RawTurtle = lambda *a, **k: FakeTurtle(canvas)
    m.Screen = lambda: screen
    for name in dir(FakeTurtle):
        if not name.startswith('_'):
            setattr(m, name, getattr(default, name))
    for name in ('bgcolor', 'title', 'setup', 'tracer', 'update', 'mainloop', 'done', 'exitonclick'):
        setattr(m, name, getattr(screen, name))
    return m


def to_svg(canvas, max_width=360, pad=20):
    pts = []
    for it in canvas.items:
        if it[0] == 'line':
            pts += it[1]
        elif it[0] == 'fill' and it[1]:
            pts += it[1]
        elif it[0] == 'dot':
            pts += [(it[1] - it[3] / 2, it[2] - it[3] / 2), (it[1] + it[3] / 2, it[2] + it[3] / 2)]
        elif it[0] == 'text':
            pts += [(it[1], it[2]), (it[1], it[2] + it[5][1] * 1.5)]
    if not pts:
        pts = [(-50, -50), (50, 50)]
    x0 = min(p[0] for p in pts) - pad
    x1 = max(p[0] for p in pts) + pad
    y0 = min(p[1] for p in pts) - pad
    y1 = max(p[1] for p in pts) + pad
    w, h = x1 - x0, y1 - y0
    f = lambda p: f'{p[0] - x0:.1f},{y1 - p[1]:.1f}'   # 터틀은 위가 +y, SVG는 아래가 +y
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" role="img" aria-label="완성 그림"'
           f' style="display:block;width:100%;max-width:{max_width}px;height:auto;margin:0 auto;background:{escape(canvas.bg)}">']
    for it in canvas.items:
        if it[0] == 'fill' and it[1] and len(it[1]) > 2:
            out.append(f'<polygon points="{" ".join(f(p) for p in it[1])}" fill="{escape(it[2])}" stroke="none"/>')
        elif it[0] == 'line' and len(it[1]) > 1:
            out.append(f'<polyline points="{" ".join(f(p) for p in it[1])}" fill="none" stroke="{escape(it[2])}"'
                       f' stroke-width="{it[3]}" stroke-linecap="round" stroke-linejoin="round"/>')
        elif it[0] == 'dot':
            out.append(f'<circle cx="{it[1] - x0:.1f}" cy="{y1 - it[2]:.1f}" r="{it[3] / 2:.1f}" fill="{escape(it[4])}"/>')
        elif it[0] == 'text':
            anchor = {'left': 'start', 'center': 'middle', 'right': 'end'}.get(it[4], 'start')
            out.append(f'<text x="{it[1] - x0:.1f}" y="{y1 - it[2]:.1f}" font-size="{it[5][1] * 1.33:.0f}"'
                       f' text-anchor="{anchor}" fill="{escape(it[6])}">{escape(it[3])}</text>')
    out.append('</svg>')
    return ''.join(out)


def record(src, inputs=(), max_width=360):
    """src를 가짜 터틀로 실행하고 (화면 글자, svg)를 돌려준다. input()은 inputs를 차례로 쓴다."""
    import io
    canvas = Canvas()
    it = iter(inputs)
    out = io.StringIO()

    def fin(p=''):
        v = next(it)
        out.write(p + v + '\n')
        return v
    old_mod, old_out = sys.modules.get('turtle'), sys.stdout
    sys.modules['turtle'] = fake_module(canvas)
    sys.stdout = out
    try:
        exec(src, {'input': fin, '__name__': '__main__'})
    finally:
        sys.stdout = old_out
        if old_mod is None:
            sys.modules.pop('turtle', None)
        else:
            sys.modules['turtle'] = old_mod
    return out.getvalue().rstrip('\n'), to_svg(canvas, max_width)
