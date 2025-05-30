from manim import Line, Group, RED

class Strikethrough(Line):
    def __init__(self, mobject, color=RED, stroke_width=4, **kwargs):
        """
        Creates a strikethrough line across a mobject.
        Attributes:
        - group: A Group containing the mobject and the strikethrough line.

        Parameters:
        - mobject: The mobject to strike through.
        - color: The color of the strikethrough line (default: RED).
        - stroke_width: The width of the strikethrough line (default: 4).
        """
        super().__init__(
            start = mobject.get_left(),
            end = mobject.get_right(),
            color = color,
            stroke_width = stroke_width,
            **kwargs
        )
        self.group: Group = Group(mobject, self)