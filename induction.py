from manim import *
from utils.strikethrough import Strikethrough

class Graph(Scene):
    def construct(self):
        axes: Axes = Axes(
            x_range = [-22, 22],
            y_range = [-11, 11],
            tips=False
        )
        n_squared_points: List = [
            Dot(axes.coords_to_point(n, n * n), color=ORANGE)
            for n in range(-3, 4)
        ]
        two_n_points: List = [
            Dot(axes.coords_to_point(n, 2 * n), color=BLUE)
            for n in range(-4, 7)
        ]
        remaining_points: List = n_squared_points[len(two_n_points):] + two_n_points[len(n_squared_points):]
        two_n: MathTex = MathTex("2n", color=BLUE)
        n_squared: MathTex = MathTex("n^2", color=ORANGE)

        self.play(FadeIn(axes))
        for n_point, t_point in zip(n_squared_points, two_n_points):
            self.play(FadeIn(n_point, run_time=0.3),FadeIn(t_point, run_time=0.3))
        self.play(*[FadeIn(point, run_time=0.3) for point in remaining_points])
        self.play(1)

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
            r"(2k \leq 2 \text{ for all } k \leq 1)", color=YELLOW
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

class PositiveInduction2(Scene):
    def construct(self):
        hypothesis: Tex = Tex(
            "Assume $2k \leq k^2$ for some integer $k \geq$",
            " ", "$2$", ".")
        self.play(FadeIn(hypothesis))
        self.wait(1)
        rectangle = SurroundingRectangle(hypothesis[2],color=YELLOW)
        self.play(Write(rectangle))
        self.wait(1)
        self.play(FadeOut(rectangle))

        strikethrough = Strikethrough(hypothesis)
        self.play(Create(strikethrough))

        instead: Tex = Tex("Instead...")
        instead.shift(UP)
        self.play(strikethrough.group.animate.shift(UP * 2), FadeIn(instead))
        new_hypothesis: MathTex = MathTex(
            r"\text{Assume } 2(", r"k", r"+ 1) &\leq (", r"k",
            r"+ 1)^2 \text{ for some integer }", r"k", r"\geq 1.\\",

            r"2k + 2 &\leq k^2 + 2k + 1\\",
            r"2k + 4", r"&\leq k^2 + 2k + 3\\",
            r"&\leq k^2 + 2k + 4\\",
            r"&\leq", r"k^2 + 4k + 4"
        )
        new_hypothesis_line_1: Group = new_hypothesis[0:7].shift(DOWN)
        new_hypothesis.set_color_by_tex("k", PINK).shift(DOWN)
        self.play(FadeIn(new_hypothesis_line_1))
        k_equals_one: MathTex = MathTex(
            "2(", "1", "+ 1) = 2(2) = 4 \qquad (", "1", "+ 1)^2 = 2^2 = 4",
        )
        k_equals_one[1].set_color(PINK)
        k_equals_one[3].set_color(PINK)
        k_equals_one.shift(DOWN * 2)
        self.play(FadeIn(k_equals_one))
        self.wait(1)
        self.play(
            FadeOut(strikethrough.group, instead, k_equals_one),
            new_hypothesis_line_1.animate.to_edge(UP)
        )
        self.wait(1)

        want: MathTex = MathTex(
            r"\text{We want } 2(k + 2) &\leq (k + 2)^2\\",
            r"2k + 4", r"&\leq", r"k^2 + 4k + 4."
        )
        want[1].set_color(BLUE)
        want[3].set_color(ORANGE)
        self.play(FadeIn(want[0]))
        self.play(new_hypothesis_line_1.animate.set_color(WHITE))
        self.wait(1)
        
        self.play(FadeIn(want[1]))
        self.wait(1)
        self.play(FadeIn(want[2], want[3]))
        self.play(want.animate.scale(0.5).to_corner(DL))
        new_hypothesis.set_color(WHITE)
        self.play(
            FadeIn(new_hypothesis[7]),
            new_hypothesis[7].animate.shift(UP * 2.6)
        )
        self.wait(1)
        two_plus: MathTex = MathTex("2 +", color=YELLOW)
        two_plus.next_to(new_hypothesis[7], LEFT)
        plus_2: MathTex = MathTex("+ 2", color=YELLOW)
        plus_2.next_to(new_hypothesis[7], RIGHT)
        self.play(Write(two_plus), Write(plus_2))
        self.wait(1)

        new_hypothesis[8].set_color(BLUE) # 2k + 4
        self.play(
            FadeIn(new_hypothesis[8], new_hypothesis[9]),
            new_hypothesis[8].animate.shift(UP * 2.7),
            new_hypothesis[9].animate.shift(UP * 2.7)
        )
        self.wait(1)

        plus_1: MathTex = MathTex("+ 1", color=YELLOW)
        plus_1.next_to(new_hypothesis[9], RIGHT)
        self.play(Write(plus_1))
        self.wait(1)

        self.play(
            FadeIn(new_hypothesis[10]),
            new_hypothesis[10].animate.shift(UP * 2.75)
        )
        self.wait(1)
        plus_2k: MathTex = MathTex("+ 2k", color=YELLOW)
        plus_2k.next_to(new_hypothesis[10], RIGHT)
        self.play(Write(plus_2k))
        self.wait(1)

        new_hypothesis[12].set_color(ORANGE) # k^2 + 4k + 4
        self.play(
            FadeIn(new_hypothesis[11], new_hypothesis[12]),
            new_hypothesis[11].animate.shift(UP * 2.75),
            new_hypothesis[12].animate.shift(UP * 2.75)
        )
        self.wait(1)
        self.play(want.animate.scale(2).move_to(ORIGIN).shift(DOWN))
        shown: MathTex = MathTex(
            r"\text{We have shown } 2(k + 2) &\leq (k + 2)^2\\",
            r"2k + 4", r"&\leq", r"k^2 + 4k + 4."
        )
        shown[1].set_color(BLUE)
        shown[3].set_color(ORANGE)
        self.wait(1)
        self.play(want.animate.become(shown).shift(DOWN))
        self.wait(1)
        hence: Tex = Tex(
            r"Hence, by mathematical induction, \\$2n \leq n^2$ for all integers $n \geq 2$."
        )
        hence.shift(DOWN * 3)
        self.play(FadeIn(hence))
        self.wait(1)

class ExampleInequality(Scene):
    def construct(self):
        example: MathTex = MathTex(
            r"1 &\leq 2\\",
            r"3 &\leq 4",
        )
        self.play(
            FadeIn(Tex("Example inequality: ").to_edge(UP)),
            FadeIn(example[0])
        )
        self.wait(1)
        two_plus: MathTex = MathTex("2 +", color=YELLOW)
        plus_2: MathTex = MathTex("+ 2", color=YELLOW)
        plus_2.next_to(example[0], RIGHT)
        two_plus.next_to(example[0], LEFT)
        self.play(Write(plus_2), Write(two_plus))
        self.wait(1)
        self.play(FadeIn(example[1]))
        image: ImageMobject = ImageMobject("assets/check.png")
        image.shift(RIGHT * 3, DOWN * 2)
        image.scale(0.5)
        self.play(
            FadeIn(image)
        )
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