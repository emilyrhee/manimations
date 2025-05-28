from manim import *

class Intro(Scene):
    def construct(self):
        steps: Tex = Tex("Steps to induction:")
        p_of_n: Tex = Tex("Claim $P(n)$")
        basis: Tex = Tex("Show base case")
        hypothesis: Tex = Tex("Assume $P(k)$")
        induction: Tex = Tex("Show $P(k+1)$")
        p_of_k_minus_1: Tex = Tex("Show $P(k-1)$?")

        steps.to_corner(UL)
        self.play(FadeIn(steps))

        group: Group = Group(
            p_of_n,
            basis,
            hypothesis, 
            induction,
            p_of_k_minus_1
        )
        group.arrange(DOWN, buff=0.5)
        group.move_to(ORIGIN)
        p_of_k_minus_1.shift(UP)

        for text in group:
            text.align_to(group[0], LEFT)

        for i, text in enumerate(group[:-1], start=1):
            number = Tex(f"{i}.").next_to(text, LEFT)  # Add a number to the left of each element
            self.play(FadeIn(number), FadeIn(text))
            self.wait(1)

        self.wait(1)


        image: ImageMobject = ImageMobject("assets/think.png")
        image.shift(RIGHT * 4, DOWN * 2)
        image.scale(0.1)

        self.play(
            induction.animate.become(p_of_k_minus_1),
            FadeIn(image)
        )
        self.wait(2)

class PositiveInduction(Scene):
    def construct(self):
        claim: Tex = Tex(
            "Claim: ", "$2n$", " ", "$\leq$", " ", "$n^2$",
            " for all $n \geq 2$.",
        )
        claim.set_color_by_tex("2n", BLUE).set_color_by_tex("n^2", ORANGE)
        self.play(FadeIn(claim))
        self.wait(1)
        self.play(claim.animate.to_edge(UP))
        
        base_case: Tex = Tex("Base case: $n = 2$")
        self.play(FadeIn(base_case))
        self.wait(1)
        self.play(base_case.animate.shift(LEFT * 5, UP * 2))
        self.wait(1)

        expression: MathTex = MathTex("2(2)", "=", "4", "\qquad", "2^2", "=", "4")
        expression[0].set_color(BLUE)
        expression[2].set_color(BLUE)
        expression[4].set_color(ORANGE)
        expression[6].set_color(ORANGE)
        self.play(Write(expression[:4]))
        self.wait(1)
        self.play(Write(expression[4:7]))
        
        result: MathTex = MathTex("4", " ", "\leq", " ", "4")
        result.shift(DOWN)
        result[0].set_color(BLUE)
        result[4].set_color(ORANGE)
        check_emoji: ImageMobject = ImageMobject("assets/check.png")
        check_emoji.scale(0.4).shift(RIGHT * 4, DOWN)
        self.play(Write(result), FadeIn(check_emoji))

class NegativeInduction(Scene):
    def construct(self):
        p_of_n: Tex = Tex(
            "Claim: ", "$2n$", " ", "$\leq$", " ", "$n^2$",
            " for all negative $n$.",
        )
        p_of_n.set_color_by_tex("2n", BLUE).set_color_by_tex("n^2", ORANGE)
        self.play(FadeIn(p_of_n))
        self.wait(1)
        self.play(p_of_n.animate.to_corner(UP))
        self.wait(1)

        base_case: Tex = Tex(
            "Base case: $n = -1$",
        )
        self.play(FadeIn(base_case))
        self.wait(1)
        self.play(base_case.animate.shift(LEFT * 5, UP * 2))

        left_hand_side: MathTex = MathTex(
            "2(-1) = -2",
            color=BLUE
        )
        right_hand_side: MathTex = MathTex(
            "(-1)^2 = 1",
            color=ORANGE
        )
        group: Group = Group(left_hand_side, right_hand_side)
        group.arrange(RIGHT, buff=1)
        for expression in group:
            self.play(Write(expression))
            self.wait(1)

        result: MathTex = MathTex("-2", " ", "\leq", " ", "1")
        result.shift(DOWN)
        result.set_color_by_tex("-2", BLUE).set_color_by_tex("1", ORANGE)
        check_emoji: ImageMobject = ImageMobject("assets/check.png")
        check_emoji.scale(0.4).shift(RIGHT * 4, DOWN)
        self.play(Write(result), FadeIn(check_emoji))

class NegativeHypothesis(Scene):
    def construct(self):
        hypothesis: MathTex = MathTex(
            r"\text{Assume } 2k &\leq k^2 \text{ for some negative integer } k.\\",
            "2k - 2", r"&\leq k^2 - 2\\",
            r"&\leq k^2 + 1\\",
            r"  &\leq", "k^2 - 2k + 1."
        )
        self.play(FadeIn(hypothesis.get_part_by_tex(r"2k &\leq k^2")))
        self.play(hypothesis.get_part_by_tex(r"2k &\leq k^2").animate.to_edge(UP))
        self.wait(1)
        hypothesis.set_color_by_tex("2k - 2", BLUE)

        want: Tex = Tex(
            "We want $2(k - 1) \leq (k - 1)^2$."
        )
        self.play(FadeIn(want))
        self.wait(1)
        want_lhs_distributed: Tex = Tex(
            "We want", " ", "$2k - 2$", " ", "$\leq (k - 1)^2$."
        )
        want_lhs_distributed.set_color_by_tex("$2k - 2", BLUE)
        self.play(want.animate.become(want_lhs_distributed))
        self.wait(1)
        want_rhs_expanded: Tex = Tex(
            "We want", " ", "$2k - 2$", " ", "$\leq$", " ", "$k^2 - 2k + 1$."
        )
        want_rhs_expanded.set_color_by_tex("$2k - 2", BLUE).set_color_by_tex("$k^2 - 2k + 1", ORANGE)
        self.play(want.animate.become(want_rhs_expanded))
        self.wait(1)
        self.play(want.animate.scale(0.5).to_corner(DL))
        self.wait(1)
        group = Group(hypothesis.get_part_by_tex("2k - 2"), hypothesis.get_part_by_tex(r"&\leq k^2 - 2\\"))
        self.play(FadeIn(group))
        self.play(group.animate.shift(UP * 2))
        self.wait(1)
        plus_3: MathTex = MathTex(
            "+ 3",
            color=YELLOW
        )
        plus_3.next_to(hypothesis.get_part_by_tex(r"&\leq k^2 - 2\\"), RIGHT)
        self.play(Write(plus_3))
        self.wait(1)
        hypothesis.set_color_by_tex("k^2 - 2k + 1.", ORANGE)
       
       
        last_group = Group(hypothesis.get_part_by_tex(r"  &\leq"), hypothesis.get_part_by_tex("k^2 - 2k + 1."))
        self.play(last_group.animate.shift(UP * 2))
        self.play(want.animate.move_to(ORIGIN).scale(2))
        self.wait(1)
        conclusion: Tex = Tex("We have shown", " ", "$2(k - 1)$", " ", "$\leq$", " ", "$(k - 1)^2$.")
        conclusion.set_color_by_tex("$2(k - 1)$", ORANGE).set_color_by_tex("$(k - 1)^2$.", BLUE)
        self.play(want.animate.become(conclusion))
        hence: Tex = Tex(
            r"Hence, by mathematical induction, \\$2n \leq n^2$ for all negative integers $n$."
        )
        hence.shift(DOWN * 2)
        self.play(FadeIn(hence))
        self.wait(1)

