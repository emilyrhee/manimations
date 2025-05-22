from manim import *

class Induction(Scene):
    def construct(self):
        steps: Text = Text("Steps to induction:", font_size=40)
        font_size: int = 36
        p_of_n: Text = Text("Claim P(n)", font_size)
        basis: Text = Text("Show basis P(1)", font_size)
        hypothesis: Text = Text("Assume P(k)", font_size)
        induction: Text = Text("Show P(k+1)", font_size)

        steps.to_corner(UL)
        self.play(FadeIn(steps))
        group: VGroup = VGroup(p_of_n, basis, hypothesis, induction)
        group.arrange(DOWN, buff=0.5)
        group.move_to(ORIGIN)

        for text in group:
            self.play(FadeIn(text))
            self.wait(1)

        self.wait(1)

        p_of_k_minus_1: Text = Text("Show P(k-1)?", font_size)
        p_of_k_minus_1.move_to(induction.get_center())

        image: ImageMobject = ImageMobject("assets/think.png")
        image.shift(RIGHT * 4, DOWN * 2)
        image.scale(0.1,)

        self.play(
            Transform(induction, p_of_k_minus_1),
            FadeIn(image)
        )
        self.wait(2)

class NegativeInduction(Scene):
    def construct(self):
        font_size = 40
        p_of_n: Tex = Tex(
            "Claim: ", "$2n$", " ", "$\leq$", " ", "$n^2$",
            " for all negative $n$.",
            font_size=40
        )
        p_of_n.set_color_by_tex("2n", BLUE).set_color_by_tex("n^2", ORANGE)
        self.play(p_of_n.animate.to_corner(UP))
        self.wait(1)

        base_case: Tex = Tex(
            "Base case: $n = -1$",
            font_size=40
        )
        self.play(base_case.animate.shift(LEFT * 5, UP * 2))

        left_hand_side: MathTex = MathTex(
            "2(-1) = -2",
            font_size=40,
            color=BLUE
        )
        right_hand_side: MathTex = MathTex(
            "(-1)^2 = 1",
            font_size=40,
            color=ORANGE
        )
        group: Group = Group(left_hand_side, right_hand_side)
        group.arrange(RIGHT, buff=1)
        group.shift(UP * 3)
        for expression in group:
            self.play(Write(expression))
            self.wait(1)

        result: MathTex = MathTex("")