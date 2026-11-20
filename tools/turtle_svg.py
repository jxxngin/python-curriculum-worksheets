"""터틀 프로그램을 창 없이 실행해 그림을 SVG로 만든다(2학기 교안의 "완성하면 이렇게 돼요"·도구 카드용).

    from turtle_svg import record
    svg = record(src, inputs)        # src를 실행하고 그린 그림을 <svg> 문자열로

- 진짜 turtle 대신 기록용 가짜 모듈을 sys.modules['turtle']에 끼워 실행한다. 창을 띄우지 않는다.
- 선·채우기·점·글자를 실행 순서대로 기록하고, 채우기는 begin_fill 자리에 놓아 그 뒤에 그린 선이 위에 보이게 한다(진짜 터틀과 같음).
- circle()은 파이썬 turtle과 같은 방식(여러 개의 짧은 직선)으로 계산한다.
- 지원하지 않는 기능을 쓰면 AttributeError가, 정확히 흉내 낼 수 없는 옵션(write의 move=True)은 NotImplementedError가 나서 바로 알 수 있다.
- clear()는 그 거북이가 그린 것만 지운다(실제 터틀과 같음).
"""
import math
import sys
import types
from html import escape

COLORS_OK = None  # 색 이름은 그대로 SVG에 넘긴다(SVG도 CSS 색 이름을 안다)


class Canvas:
    def __init__(self):
        self.items = []          # ('line', pts, color, width) / ('fill', idx) / ('dot', x, y, size, color) / ('text', ...)
        self.bg = '#ffffff'
        self.title = ''
        self.turtles = []        # 만든 거북이들. 끝났을 때 보이는 거북이는 그림 맨 위에 그린다


# 파이썬 turtle에 들어 있는 모양 좌표(TurtleScreen._shapes와 같음). +y 쪽이 거북이가 보는 방향이다.
SHAPES = {
    'arrow': ((-10, 0), (10, 0), (0, 10)),
    'turtle': ((0, 16), (-2, 14), (-1, 10), (-4, 7), (-7, 9), (-9, 8), (-6, 5), (-7, 1), (-5, -3), (-8, -6),
               (-6, -8), (-4, -5), (0, -7), (4, -5), (6, -8), (8, -6), (5, -3), (7, 1), (6, 5), (9, 8), (7, 9),
               (4, 7), (1, 10), (2, 14)),
    'circle': tuple((round(10 * math.cos(math.radians(a)), 2), round(10 * math.sin(math.radians(a)), 2)) for a in range(0, 360, 18)),
    'square': ((10, -10), (10, 10), (-10, 10), (-10, -10)),
    'triangle': ((10, -5.77), (0, 11.55), (-10, -5.77)),
    'classic': ((0, 0), (-5, -9), (0, -7), (5, -9)),
    'blank': (),
}


class FakeTurtle:
    def __init__(self, canvas, register=True):
        self._c = canvas
        self._shape = 'classic'
        if register:
            canvas.turtles.append(self)
        self._x = self._y = 0.0
        self._h = 0.0
        self._down = True
        self._color = '#000000'
        self._fill = '#000000'
        self._width = 1
        self._path = None        # 지금 그리는 선(점 목록)
        self._fill_pts = None
        self._fill_slot = None
        self._visible = True
        self._mine = []          # 이 거북이가 그린 항목(clear()는 이것만 지운다)

    # ---- 그리기 내부
    def _add(self, item):
        self._c.items.append(item)
        self._mine.append(item)

    def _start_path(self):
        if self._down and self._path is None:
            self._path = [(self._x, self._y)]
            self._add(['line', self._path, self._color, self._width])

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
        self._add(self._fill_slot)
        self._end_path()

    def end_fill(self):
        if self._fill_pts is not None:
            self._fill_slot[1] = list(self._fill_pts)
            self._fill_slot[2] = self._fill
        self._fill_pts = None

    def dot(self, size=None, *c):
        if isinstance(size, (str, tuple)):   # dot("red")처럼 색만 준 경우(실제 터틀과 같음)
            c, size = (size,) + c, None
        size = size or max(self._width + 4, self._width * 2)
        self._end_path()   # 지금까지의 선을 끊어야 점 뒤에 그린 선이 점 위에 보인다(그린 순서 그대로)
        self._add(['dot', self._x, self._y, size, _col(c) if c else self._color])

    def write(self, text, move=False, align='left', font=('Arial', 8, 'normal')):
        if move:
            # 실제 터틀은 글꼴의 실제 폭만큼 움직인다. 기록용 터틀은 그 폭을 정확히 알 수 없어
            # 어림해서 움직이면 완성 그림이 조용히 달라진다. 그래서 쓰지 못하게 막는다.
            raise NotImplementedError('기록용 터틀은 write(move=True)를 지원하지 않아요. move 없이 쓰고 goto()로 옮겨요.')
        self._end_path()
        self._add(['text', self._x, self._y, str(text), align, font, self._color])

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

    def shape(self, name=None):
        if name is None:
            return self._shape
        if name not in SHAPES:
            raise ValueError(f'기록용 터틀이 모르는 모양이에요: {name!r} ({", ".join(SHAPES)})')
        self._shape = name

    def _cursor(self):
        """보이는 거북이의 모양 꼭짓점(터틀 좌표). 실제 터틀(_polytrafo, 크기 그대로)과 같은 계산."""
        e0, e1 = math.cos(math.radians(self._h)), math.sin(math.radians(self._h))
        return [(self._x + e1 * x + e0 * y, self._y - e0 * x + e1 * y) for x, y in SHAPES[self._shape]]

    def hideturtle(self):
        self._visible = False
    ht = hideturtle

    def showturtle(self):
        self._visible = True
    st = showturtle

    def clear(self):
        # 이 거북이가 그린 것만 지운다(다른 거북이의 그림과 배경색은 그대로). 위치·방향·펜 상태도 그대로다.
        mine = {id(it) for it in self._mine}
        self._c.items[:] = [it for it in self._c.items if id(it) not in mine]
        self._mine = []
        self._end_path()
        if self._fill_pts is not None:   # 채우는 중이면 이후 점부터 다시 모은다
            self._fill_slot = ['fill', None, None]
            self._add(self._fill_slot)
            self._fill_pts = [(self._x, self._y)]


class FakeScreen:
    def __init__(self, canvas):
        self._c = canvas

    def colormode(self, mode=None):
        """색 숫자의 범위: 1.0(기본, 0~1) 또는 255(0~255). 실제 터틀과 같다."""
        global _MODE
        if mode is None:
            return _MODE
        if mode not in (1, 1.0, 255):
            raise ValueError(f'colormode는 1.0이나 255만 돼요: {mode!r}')
        _MODE = 255 if mode == 255 else 1.0

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


_MODE = 1.0   # colormode. record()마다 1.0으로 되돌린다
_TK = None
_RGB = {}


def _tk_rgb(name):
    """색 이름을 실제 터틀이 쓰는 Tk에 물어 '#rrggbb'로 바꾼다.
    Tk 색 이름과 SVG/CSS 색 이름은 다르다(예: Tk의 gray50은 CSS에 없다). 이름을 그대로 넘기면 그림이 조용히 달라진다.
    Tk도 모르는 이름이면 실제 터틀처럼 오류를 낸다."""
    global _TK
    if name in _RGB:
        return _RGB[name]
    if _TK is None:
        import tkinter
        _TK = tkinter.Tk()
        _TK.withdraw()
    try:
        r, g, b = _TK.winfo_rgb(name)
    except Exception:
        raise ValueError(f'터틀이 모르는 색이에요: {name!r}')
    _RGB[name] = f'#{r // 257:02x}{g // 257:02x}{b // 257:02x}'
    return _RGB[name]


def _col(c):
    if len(c) == 1 and isinstance(c[0], tuple):
        c = c[0]
    if len(c) == 3:
        top = 255 if _MODE == 255 else 1.0
        if not all(0 <= v <= top for v in c):
            raise ValueError(f'색 숫자는 0~{top:g} 사이여야 해요(colormode {top:g}): {tuple(c)!r}')
        r, g, b = (round(v * 255 / top) for v in c)
        return f'#{r:02x}{g:02x}{b:02x}'
    return _tk_rgb(str(c[0]))


def fake_module(canvas):
    global _MODE
    _MODE = 1.0   # 실행마다 실제 터틀의 기본 색 모드로
    m = types.ModuleType('turtle')
    default = FakeTurtle(canvas, register=False)   # 실제 터틀처럼 모듈 함수를 처음 쓸 때 화면에 생긴다
    screen = FakeScreen(canvas)
    def make_turtle(shape='classic', undobuffersize=1000, visible=True):
        """turtle.Turtle()과 같은 인자. 모양·표시 여부를 그대로 적용한다(undobuffersize는 그림에 영향 없음)."""
        t = FakeTurtle(canvas)
        t.shape(shape)
        if not visible:
            t.hideturtle()
        return t

    def raw_turtle(*a, **k):
        raise NotImplementedError('기록용 터틀은 RawTurtle을 지원하지 않아요. turtle.Turtle()을 써요.')
    m.Turtle = m.Pen = make_turtle
    m.RawTurtle = m.RawPen = raw_turtle
    m.Screen = lambda: screen

    def use(name):
        def f(*a, **k):
            if default not in canvas.turtles:
                canvas.turtles.append(default)
            return getattr(default, name)(*a, **k)
        return f
    for name in dir(FakeTurtle):
        if not name.startswith('_'):
            setattr(m, name, use(name))
    for name in ('bgcolor', 'title', 'setup', 'tracer', 'update', 'mainloop', 'done', 'exitonclick', 'colormode'):
        setattr(m, name, getattr(screen, name))
    return m


def text_box(x, y, text, align, font):
    """write() 글자가 차지하는 네모의 두 꼭짓점(터틀 좌표). 폭은 글자 수로 어림한다:
    한글·한자 등 넓은 글자는 1em, 나머지는 0.6em. 터틀은 기준선이 y이고 글자는 그 위에 놓인다."""
    em = font[1] * 1.33   # SVG에 쓰는 글자 크기(px)와 같게
    w = sum(1.0 if ord(ch) > 0x2E80 else 0.6 for ch in text) * em
    x0 = {'left': x, 'center': x - w / 2, 'right': x - w}.get(align, x)
    return [(x0, y - em * 0.3), (x0 + w, y + em * 1.1)]


def to_svg(canvas, max_width=360, pad=20):
    cursors = [(t._cursor(), t._fill, t._color) for t in canvas.turtles if t._visible and SHAPES[t._shape]]
    pts = [q for poly, _, _ in cursors for q in poly]
    for it in canvas.items:
        if it[0] == 'line':   # 선은 두께의 절반만큼 양옆으로 퍼진다
            hw = it[3] / 2
            pts += [q for x, y in it[1] for q in ((x - hw, y - hw), (x + hw, y + hw))]
        elif it[0] == 'fill' and it[1]:
            pts += it[1]
        elif it[0] == 'dot':
            pts += [(it[1] - it[3] / 2, it[2] - it[3] / 2), (it[1] + it[3] / 2, it[2] + it[3] / 2)]
        elif it[0] == 'text':
            pts += text_box(it[1], it[2], it[3], it[4], it[5])
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
            font = tuple(it[5]) + ('normal',) * (3 - len(it[5]))
            style = str(font[2]).lower().split()
            out.append(f'<text x="{it[1] - x0:.1f}" y="{y1 - it[2]:.1f}" font-size="{font[1] * 1.33:.0f}"'
                       f' font-family="{escape(str(font[0]), quote=True)}, sans-serif"'
                       + (' font-weight="bold"' if 'bold' in style else '')
                       + (' font-style="italic"' if 'italic' in style else '')
                       + f' text-anchor="{anchor}" fill="{escape(it[6])}">{escape(it[3])}</text>')
    for poly, fc, oc in cursors:   # 보이는 거북이는 실제 창처럼 그림 맨 위에(채우기 색 + 펜 색 테두리, 두께 1)
        out.append(f'<polygon points="{" ".join(f(q) for q in poly)}" fill="{escape(fc)}" stroke="{escape(oc)}" stroke-width="1"/>')
    out.append('</svg>')
    return ''.join(out)


def record(src, inputs=(), max_width=360):
    """src를 가짜 터틀로 실행하고 (화면 글자, svg)를 돌려준다. input()은 inputs를 차례로 쓴다."""
    import io
    global _MODE
    _MODE = 1.0
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
