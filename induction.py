from manim import *

class Induction(Scene):
    def construct(self):
        steps : Text = Text("Steps to induction:", 40)
        font_size : int = 36
        p_of_n : Text = Text("Claim P(n)", font_size)
        basis : Text = Text("Show basis P(1)", font_size)
        hypothesis : Text = Text("Assume P(k)", font_size)
        induction : Text = Text("Show P(k+1)", font_size)

        steps.to_corner(UL)
        self.play(FadeIn(steps))
        group : VGroup = VGroup(p_of_n, basis, hypothesis, induction)
        group.arrange(DOWN, buff=0.5)
        group.move_to(ORIGIN)

        for text in group:
            self.play(FadeIn(text))
            self.wait(1)