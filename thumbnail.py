from manim import *

class Thumbnail(Scene):
    def construct(self):
        axes: Axes = Axes(
            x_range = [-10, 30],
            y_range = [-9, 12],
            tips=False
        )
        self.add(axes)

        n_squared_points: List = [
            Dot(axes.coords_to_point(n, n * n), color=ORANGE)
            for n in range(-3, 4)
        ]
        two_n_points: List = [
            Dot(axes.coords_to_point(n, 2 * n), color=BLUE)
            for n in range(-4, 7)
        ]

        for point in n_squared_points:
            self.add(point)
        
        for point in two_n_points:
            self.add(point)

        intersections: List = [
            Dot(axes.coords_to_point(2,4), color=RED),
            Dot(axes.coords_to_point(0, 0), color=RED)
        ]
        for intersection in intersections:
            self.add(intersection)