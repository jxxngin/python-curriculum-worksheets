"""수업용 터틀 코드의 이동 명령을 정적인 인라인 SVG로 기록한다.

외부 그림·브라우저 스크립트를 사용하지 않으며 실제 앱 캡처를 가장하지 않는다.
"""
import contextlib
import html
import io
import math
import sys
import types


class Pen(types.ModuleType):
    def __init__(self):
        super().__init__('turtle')
        self.x = self.y = self.heading = 0
        self.ink = self.fill = 'black'
        self.down = True
        self.width = 1
        self.shapes = []
        self.filling = None
        self.dots = []
        self.moves = []
        self.colors = []
        self.circles = []

    def color(self, ink, fill=None):
        self.ink = ink
        self.fill = fill or ink

    def pencolor(self, ink):
        self.ink = ink
        self.colors.append(ink)

    def penup(self): self.down = False
    def pendown(self): self.down = True
    def speed(self, *args): pass
    def bgcolor(self, *args): pass
    def done(self): pass
    def pensize(self, value): self.width = value
    def setheading(self, angle): self.heading = angle
    def left(self, angle): self.heading += angle
    def right(self, angle): self.heading -= angle

    def goto(self, x, y):
        self.moves.append((x, y))
        if self.down:
            self.shapes.append(f'<path d="M{self.x},{-self.y} L{x},{-y}" '
                               f'fill="none" stroke="{html.escape(self.ink)}" '
                               f'stroke-width="{self.width}"/>')
        if self.filling is not None:
            self.filling.append((x, -y))
        self.x, self.y = x, y

    def forward(self, value):
        angle = math.radians(self.heading)
        self.goto(self.x + value * math.cos(angle), self.y + value * math.sin(angle))

    def backward(self, value): self.forward(-value)

    def circle(self, radius, extent=360):
        self.circles.append((radius, extent))
        angle = math.radians(self.heading)
        cx = self.x - radius * math.sin(angle)
        cy = self.y + radius * math.cos(angle)
        dx, dy = self.x - cx, self.y - cy
        for i in range(1, 121):
            turn = math.radians(extent * i / 120)
            self.goto(cx + dx * math.cos(turn) - dy * math.sin(turn),
                      cy + dx * math.sin(turn) + dy * math.cos(turn))
        self.heading += extent

    def begin_fill(self):
        self.filling = [(self.x, -self.y)]

    def end_fill(self):
        points = ' '.join(f'{x},{y}' for x, y in self.filling)
        self.shapes.append(f'<polygon points="{points}" fill="{html.escape(self.fill)}"/>')
        self.filling = None

    def dot(self, size, color):
        self.dots.append((self.x, self.y, size, color))
        self.shapes.append(f'<circle cx="{self.x}" cy="{-self.y}" r="{size / 2}" '
                           f'fill="{html.escape(color)}"/>')


def render(src, title):
    pen = Pen()
    previous = sys.modules.get('turtle')
    sys.modules['turtle'] = pen
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, 'mini-preview.py', 'exec'), {})
    finally:
        if previous is None:
            del sys.modules['turtle']
        else:
            sys.modules['turtle'] = previous
    return ('<svg class="result-preview" xmlns="http://www.w3.org/2000/svg" '
            'viewBox="-260 -190 520 380" role="img" '
            f'aria-label="{html.escape(title, quote=True)}"><title>{html.escape(title)}</title>'
            + ''.join(pen.shapes) + '</svg>')
