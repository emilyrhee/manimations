from manim import *

class Thumbnail(Scene):
    def construct(self):
        axes: Axes = Axes(
            x_range = [-8, 22],
            y_range = [-11, 11],
            tips=False,
        )
        n_squared_line: VMobject = axes.plot(lambda x: x**2, x_range=[-3, 3], color=DARK_BROWN)
        two_n_line: VMobject = axes.plot(lambda x: 2 * x, x_range=[-4, 5], color=DARK_BLUE)
        n_squared_points: List = [
            Dot(axes.coords_to_point(n, n * n), color=ORANGE)
            for n in range(-3, 4)
        ]
        two_n_points: List = [
            Dot(axes.coords_to_point(n, 2 * n), color=BLUE)
            for n in range(-4, 6)
        ]
        text: MathTex = MathTex("P(k - 1)").scale(2.5)

        text.shift(DOWN * 1.5, RIGHT * 2)

        self.add(axes, n_squared_line, two_n_line, *n_squared_points, *two_n_points, text)