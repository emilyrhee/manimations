from manim import *

class Intro(Scene):
    def construct(self):
        steps: Tex = Tex("Steps to induction:")
        p_of_n: Tex = Tex("Claim $P(n)$")
        basis: Tex = Tex("Show basis $P(1)$")
        hypothesis: Tex = Tex("Assume $P(k)$")
        induction: Tex = Tex("Show $P(k+1)$")

        steps.to_corner(UL)
        self.play(FadeIn(steps))
        group: VGroup = VGroup(p_of_n, basis, hypothesis, induction)
        group.arrange(DOWN, buff=0.5)
        group.move_to(ORIGIN)

        for text in group:
            self.play(FadeIn(text))
            self.wait(1)

        self.wait(1)

        p_of_k_minus_1: Tex = Tex("Show $P(k-1)$?")
        p_of_k_minus_1.move_to(induction.get_center())

        image: ImageMobject = ImageMobject("assets/think.png")
        image.shift(RIGHT * 4, DOWN * 2)
        image.scale(0.1)

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
        for expression in group:
            self.play(Write(expression))
            self.wait(1)

        result: MathTex = MathTex("-2", " ", "\leq", " ", "1")
        result.shift(DOWN)
        result.set_color_by_tex("-2", ORANGE).set_color_by_tex("1", BLUE)
        check_emoji: ImageMobject = ImageMobject("assets/check.png")
        check_emoji.scale(0.4).shift(RIGHT * 4, DOWN)
        self.play(Write(result), FadeIn(check_emoji))

class NegativeHypothesis(Scene):
    def construct(self):
        hypothesis: MathTex = MathTex(
            r"\text{Assume } 2k &\leq k^2 \text{ for some negative integer } k.\\",
            r"2k - 2 &\leq k^2 - 2\\",
            r"2k - 2 &\leq k^2 + 1\\",
            r"2k - 2 &\leq k^2 - 2k + 1."
        )
        self.play(hypothesis.get_part_by_tex(r"2k &\leq k^2").animate.to_edge(UP))
        self.wait(1)

        want: Tex = Tex(
            "We want $2(k - 1) \leq (k - 1)^2$."
        )
        self.play(FadeIn(want))
        self.wait(1)
        want_lhs_distributed: Tex = Tex(
            "We want $2k - 2 \leq (k - 1)^2$."
        )
        self.play(want.animate.become(want_lhs_distributed))
        self.wait(1)
        want_rhs_expanded: Tex = Tex(
            "We want $2k - 2 \leq k^2 - 2k + 1$."
        )
        self.play(want.animate.become(want_rhs_expanded))
        self.wait(1)
        self.play(want.animate.scale(0.5).to_corner(DL))

        self.play(hypothesis.get_part_by_tex(r"2k - 2 &\leq k^2 - 2\\").animate.shift(UP * 2))
        self.wait(1)
        self.play(hypothesis.get_part_by_tex(r"2k - 2 &\leq k^2 + 1\\").animate.shift(UP * 2))
        self.wait(1)
        self.play(hypothesis.get_part_by_tex(r"2k - 2 &\leq k^2 - 2k + 1.").animate.shift(UP * 2))
        # self.play(want.animate.shift(ORIGIN).scale(2))
    

class BasicEquationsSimple(Scene):
    def construct(self):
        eqns = MathTex(r"2x - 3 & = -7 \\", r"2x & = -4 \\", r"x & = -2")
        self.play(Write(eqns))