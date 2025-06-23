from manim import *
from utils.strikethrough import Strikethrough

class Graph(Scene):
    def construct(self):
        axes: Axes = Axes(
            x_range = [-22, 22],
            y_range = [-11, 11],
            tips=False,
            x_axis_config={"numbers_to_include": [2]}
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
        remaining_points: List = n_squared_points[len(two_n_points):] + two_n_points[len(n_squared_points):]
        claim: MathTex = MathTex(
            r"2n", r"\leq", r"n^2"
        )
        for_all_negative: Tex = Tex("for all negative $n$.")
        for_all_positive: Tex = Tex("for all $n \geq 2$.")

        claim.shift(LEFT * 5, UP * 2)
        for_all_negative.next_to(claim, DOWN)
        for_all_negative.align_to(claim, LEFT)
        
        claim[0].set_color(BLUE)
        claim[2].set_color(ORANGE)

        claim_copy: MathTex = claim.copy()

        claim_copy.shift(DOWN * 3)
        for_all_positive.next_to(claim_copy, DOWN)
        for_all_positive.align_to(claim_copy, LEFT)

        self.play(FadeIn(axes, claim[0], claim[2]))
        self.play(
            Create(n_squared_line, rate_func=linear),
            Create(two_n_line, rate_func=linear),
        )
        for n_point, t_point in zip(n_squared_points, two_n_points):
            self.play(FadeIn(n_point, t_point, run_time=0.3))
        self.play(FadeIn(claim[1], for_all_negative))
        self.play(*[FadeIn(point, run_time=0.3) for point in remaining_points])
        self.play(FadeIn(claim_copy, for_all_positive))
        self.wait(1)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

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
            number = Tex(f"{i}.").next_to(text, LEFT)
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
        base_case.align_to(claim, LEFT).shift(UP * 2)
        self.play(FadeIn(base_case))
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

class Induction(Scene):
    def construct(self):
        hypothesis: Tex = Tex(
            "Assume $2k \leq k^2$ for some integer $k \geq$",
            " ", "$2$", "."
        )
        want: MathTex = MathTex(
            r"\text{We want }", r"2(k + 1) &\leq (k + 1)^2, \text{ or}\\",
            r"2k + 2", r"&\leq", r"k^2 + 2k + 1", r"."   
        )
        have: MathTex = MathTex(
            r"\text{We have }", r"2k + 2", r"&\leq k^2 + 2\\",
            r"&\leq k^2 + 2k\\",
            r"&\leq", r"k^2 + 2k + 1", r"."
        )
        twok_leq_2 :MathTex = MathTex(
            r"(2k \geq 2 \text{ for all } k \geq 1)", color=YELLOW
        )
        hence: MathTex = MathTex(
            r"&\text{Hence, by mathematical induction, }\\",
            r"&2n \leq n^2 \text{ for } \text{all integers } n \geq 2."
        )
        
        want_line_1: Group = want[0:2]
        want_line_2: Group = want[2:6]
        have_line_1: Group = have[0:3]
        have_line_2: Group = have[3:4]
        have_line_3: Group = have[4:7]

        want[2].set_color(BLUE)
        want[4].set_color(ORANGE)
        have_line_1[1].set_color(BLUE)
        have_line_3[1].set_color(ORANGE)

        hypothesis.to_edge(UP)
        want.shift(UP * 2)
        want.align_to(hypothesis, LEFT)
        have.align_to(hypothesis, LEFT)
        twok_leq_2.next_to(have_line_2)
        hence.align_to(hypothesis, LEFT)
        hence.shift(DOWN * 2).align_to(hypothesis, LEFT)

        self.play(FadeIn(hypothesis))  # Assume 2k <= k^2
        self.wait(1)
        self.play(FadeIn(want_line_1)) # Want 2(k + 1) <= (k + 1)^2
        self.wait(1)
        self.play(FadeIn(want_line_2)) # 2k + 2 <= 2k + 1
        self.wait(1)
        self.play(FadeIn(have_line_1)) # We have 2k + <= k^2 + 2
        self.wait(1)
        self.play(FadeIn(have_line_2)) # k^2 + 2k
        self.wait(1)
        self.play(FadeIn(twok_leq_2))
        self.wait(1)
        self.play(FadeIn(have_line_3)) # k^2 + 2k + 1
        self.wait(1)
        self.play(FadeIn(hence))
        self.wait(1)

class ExampleInequality(Scene):
    def construct(self):
        example: MathTex = MathTex(
            r"1 &\leq 2\\",
            r"3 &\leq 4",
        )
        number_line = NumberLine(
            x_range=[0, 5, 1],
            length=6,
            include_numbers=True,
            label_direction=DOWN,
        )
        two_plus: MathTex = MathTex("2 +", color=YELLOW)
        plus_2: MathTex = MathTex("+ 2", color=YELLOW)
        image: ImageMobject = ImageMobject("assets/check.png")
        leq: MathTex = MathTex(r"\leq")

        plus_2.next_to(example[0], RIGHT)
        two_plus.next_to(example[0], LEFT)
        image.shift(RIGHT * 3)   
        image.scale(0.25)
        number_line.shift(DOWN * 2)
        leq.move_to(number_line.n2p(1.5))
        leq.shift(DOWN * .4)

        self.play(
            FadeIn(Tex("Example inequality: ").to_edge(UP)),
            FadeIn(example[0])
        )
        self.wait(1)
        self.play(Write(plus_2), Write(two_plus))
        self.wait(1)
        self.play(FadeIn(example[1]))
        self.play(
            FadeIn(image)
        )
        self.wait(1)
        self.play(FadeOut(image))
        self.wait(1)
        self.play(FadeIn(number_line, leq))
        self.wait(1)
        self.play(leq.animate.move_to(number_line.n2p(3.5)).shift(DOWN * .4))
        self.wait(1)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
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
            "Base case: $n = -1$.",
        )
        base_case.align_to(p_of_n, LEFT).shift(UP * 2)
        self.play(FadeIn(base_case))

        left_hand_side: MathTex = MathTex(
            "2(-1)", "=", "-2"
        )
        right_hand_side: MathTex = MathTex(
            "(-1)^2", "=", "1"
        )
        Group(left_hand_side[0], left_hand_side[2]).set_color(BLUE)
        Group(right_hand_side[0], right_hand_side[2]).set_color(ORANGE)
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
            r"\text{Assume } 2k &\leq k^2 \text{ for some }", r"\text{negative integer } k.\\",
        )
        want: MathTex = MathTex(
            r"\text{We want } 2(k - 1) &\leq (k - 1)^2, \text{ or }\\",
            r"2k - 2", r"&\leq", r"k^2 - 2k + 1", r"."
        )
        have: MathTex = MathTex(
            r"\text{We have }", r"2k - 2", r"&\leq k^2 - 2\\",
            r"&\leq k^2 + 1\\",
            r"&\leq", r"k^2 - 2k + 1", r"."
        )
        by_hypothesis: Tex = Tex("(By hypothesis)", color=YELLOW)
        conclusion: Tex = Tex("We have shown", " ", "$2(k - 1)$", " ", "$\leq$", " ", "$(k - 1)^2$.")
        hence: MathTex = MathTex(
            r"&\text{Hence, by mathematical induction, } 2n \leq n^2 \text{ for}\\",
            r"&\text{all negative integers } n."
        )
        negative_two_k: Tex = Tex(
            "($-2k$ is positive)",
            color=YELLOW
        )

        want_line_1: Group = want[0:1]
        want_line_2: Group = want[1:5]
        have_line_1: Group = have[0:3]
        have_line_2: Group = have[3:4]
        have_line_3: Group = have[4:7]

        want_line_2[0].set_color(BLUE)
        want_line_2[2].set_color(ORANGE)
        have_line_1[1].set_color(BLUE)
        have_line_3[1].set_color(ORANGE)

        hypothesis.to_edge(UP)
        want.align_to(hypothesis, LEFT)
        have.align_to(hypothesis, LEFT)
        hence.align_to(hypothesis, LEFT)
        hence.shift(DOWN * 3).align_to(hypothesis, LEFT)
        want.shift(UP * 2)
        conclusion.shift(DOWN * 1.75).align_to(hypothesis, LEFT)
        by_hypothesis.next_to(have_line_1)
        negative_two_k.next_to(have_line_3)
        
        negative_k_emphasis: SurroundingRectangle = SurroundingRectangle(
            hypothesis[1], color=YELLOW
        )

        self.play(FadeIn(hypothesis))
        self.wait(1)
        self.play(FadeIn(want_line_1)) # We want 2(k - 1) <= (k - 2)^2
        self.wait(1)
        self.play(FadeIn(want_line_2)) # 2k - 2 <= k^2 - 2k + 1
        self.wait(1)
        self.play(FadeIn(have_line_1))
        self.wait(1)
        self.play(FadeIn(by_hypothesis))
        self.wait(1)
        self.play(FadeIn(have_line_2))
        self.wait(1)
        self.play(FadeIn(have_line_3))
        self.wait(1)
        self.play(Write(negative_k_emphasis))
        self.wait(1)
        self.play(FadeIn(negative_two_k))
        self.wait(1)
        self.play(FadeOut(negative_k_emphasis))
        self.wait(1)
        self.play(FadeIn(conclusion))
        self.wait(1)
        self.play(FadeIn(hence))
        self.wait(1)