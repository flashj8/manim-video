from manim import *


class ProofByContradictionTest(Scene):
    """
    Animated proof by contradiction that √2 is irrational.

    Structure:
      1. Title card
      2. State the claim and assumption
      3. Set up the fraction p/q in lowest terms
      4. Square both sides → 2q² = p²
      5. Show p must be even → write p = 2k
      6. Substitute → q must also be even
      7. Contradiction: p/q was in lowest terms!
      8. Conclusion banner
    """

    def construct(self):
        self._title_card()
        self._state_claim()
        self._assume_rational()
        self._algebra()
        self._p_is_even()
        self._q_is_even()
        self._contradiction()
        self._conclusion()

    # ------------------------------------------------------------------ #
    #  helpers                                                             #
    # ------------------------------------------------------------------ #

    def _section_header(self, text: str, color=BLUE_C) -> Mobject:
        """Small coloured label in the top-left corner."""
        label = Text(text, font_size=22, color=color)
        label.to_corner(UL, buff=0.4)
        return label

    def _flash_red(self, mob: Mobject):
        """Brief red flash to highlight a contradiction."""
        self.play(mob.animate.set_color(RED), run_time=0.4)
        self.play(mob.animate.set_color(WHITE), run_time=0.4)

    # ------------------------------------------------------------------ #
    #  scenes                                                             #
    # ------------------------------------------------------------------ #

    def _title_card(self):
        title = Text("Test Proof by Contradiction", font_size=48, weight=BOLD)
        subtitle = Text("√2 is irrational", font_size=32, color=BLUE_C)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

    def _state_claim(self):
        header = self._section_header("Step 1 — Claim")

        claim = MathTex(r"\sqrt{2} \notin \mathbb{Q}", font_size=52)
        claim_words = Text(
            "√2 is not rational  (this is what we want to prove)",
            font_size=24,
            color=GRAY_A,
        )
        claim_words.next_to(claim, DOWN, buff=0.5)

        self.play(FadeIn(header))
        self.play(Write(claim))
        self.play(FadeIn(claim_words, shift=UP * 0.2))
        self.wait(2)
        self.play(FadeOut(header), FadeOut(claim), FadeOut(claim_words))

    def _assume_rational(self):
        header = self._section_header("Step 2 — Assume the opposite", color=YELLOW)

        assume_label = Text(
            "Assume for contradiction that √2 IS rational:",
            font_size=26,
            color=YELLOW,
        )
        assume_label.to_edge(UP, buff=1.2)

        fraction = MathTex(r"\sqrt{2} = \frac{p}{q}", font_size=52)
        condition = MathTex(
            r"\text{where } p, q \in \mathbb{Z},\; q \neq 0,\; \gcd(p,q)=1",
            font_size=32,
            color=GRAY_A,
        )
        condition.next_to(fraction, DOWN, buff=0.5)

        lowest_terms = Text(
            "(fraction already in lowest terms — no common factors)",
            font_size=22,
            color=TEAL_C,
        )
        lowest_terms.next_to(condition, DOWN, buff=0.5)

        self.play(FadeIn(header))
        self.play(Write(assume_label))
        self.play(Write(fraction))
        self.play(FadeIn(condition, shift=UP * 0.2))
        self.play(FadeIn(lowest_terms, shift=UP * 0.2))
        self.wait(2.5)
        self.play(
            FadeOut(header),
            FadeOut(assume_label),
            FadeOut(condition),
            FadeOut(lowest_terms),
            fraction.animate.scale(0.6).to_corner(UL, buff=1.2),
        )

    def _algebra(self):
        header = self._section_header("Step 3 — Algebraic consequences", color=BLUE_C)

        # keep the small fraction in the corner as a reference
        corner_eq = MathTex(r"\sqrt{2} = \frac{p}{q}", font_size=30, color=GRAY_B)
        corner_eq.to_corner(UL, buff=1.2)

        step1 = MathTex(r"2 = \frac{p^2}{q^2}", font_size=48)
        step1_label = Text("square both sides", font_size=22, color=GRAY_A)
        step1_label.next_to(step1, RIGHT, buff=0.5)

        step2 = MathTex(r"2q^2 = p^2", font_size=48)

        step1.shift(UP * 0.5)
        step1_label.shift(UP * 0.5)
        step2.shift(DOWN * 0.8)

        self.play(FadeIn(header), FadeIn(corner_eq))
        self.play(Write(step1), FadeIn(step1_label))
        self.wait(1)
        self.play(
            TransformMatchingTex(step1.copy(), step2),
            FadeOut(step1_label),
        )
        self.wait(1.5)

        highlight = SurroundingRectangle(step2, color=BLUE_C, buff=0.15)
        self.play(Create(highlight))
        self.wait(1)

        key = Text(
            "p² is even  (since 2q² is clearly even)",
            font_size=26,
            color=BLUE_C,
        )
        key.next_to(step2, DOWN, buff=0.8)
        self.play(FadeIn(key, shift=UP * 0.2))
        self.wait(2)
        self.play(
            FadeOut(header),
            FadeOut(corner_eq),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(highlight),
            FadeOut(key),
        )

    def _p_is_even(self):
        header = self._section_header("Step 4 — p must be even", color=GREEN_C)

        logic = BulletedList(
            "If $p^2$ is even, then $p$ itself is even",
            r"(odd $\times$ odd $=$ odd, so odd$^2$ is never even)",
            font_size=28,
        )
        logic[1].set_color(GRAY_A)
        logic.shift(UP * 0.5)

        write_p = MathTex(r"p = 2k \quad (k \in \mathbb{Z})", font_size=44)
        write_p.next_to(logic, DOWN, buff=0.7)

        self.play(FadeIn(header))
        self.play(FadeIn(logic, shift=UP * 0.2))
        self.wait(1.5)
        self.play(Write(write_p))
        self.wait(2)
        self.play(FadeOut(header), FadeOut(logic), FadeOut(write_p))

    def _q_is_even(self):
        header = self._section_header("Step 5 — q must also be even", color=GREEN_C)

        sub = MathTex(r"2q^2 = p^2 = (2k)^2 = 4k^2", font_size=44)
        sub.shift(UP * 1.2)

        simplify = MathTex(r"q^2 = 2k^2", font_size=44)
        simplify.next_to(sub, DOWN, buff=0.7)

        conclusion = Text(
            "So q² is even  →  q is also even",
            font_size=30,
            color=GREEN_C,
        )
        conclusion.next_to(simplify, DOWN, buff=0.7)

        self.play(FadeIn(header))
        self.play(Write(sub))
        self.wait(1)
        self.play(TransformMatchingTex(sub.copy(), simplify))
        self.wait(1)
        self.play(FadeIn(conclusion, shift=UP * 0.2))
        self.wait(2)
        self.play(FadeOut(header), FadeOut(sub), FadeOut(simplify), FadeOut(conclusion))

    def _contradiction(self):
        header = self._section_header("Step 6 — Contradiction!", color=RED)

        both_even = MathTex(
            r"p \text{ is even} \quad \text{and} \quad q \text{ is even}",
            font_size=40,
        )
        both_even.shift(UP * 1.5)

        implies = MathTex(
            r"\Rightarrow \gcd(p,q) \geq 2",
            font_size=40,
            color=RED,
        )
        implies.next_to(both_even, DOWN, buff=0.6)

        contra = Text(
            "But we assumed gcd(p,q) = 1  ✗",
            font_size=30,
            color=RED,
        )
        contra.next_to(implies, DOWN, buff=0.6)

        bang = Text("⚡ Contradiction!", font_size=48, color=RED, weight=BOLD)
        bang.next_to(contra, DOWN, buff=0.7)

        self.play(FadeIn(header))
        self.play(Write(both_even))
        self.wait(0.8)
        self.play(Write(implies))
        self.wait(0.8)
        self.play(FadeIn(contra))
        self.wait(0.8)
        self.play(Write(bang))
        self._flash_red(bang)
        self._flash_red(bang)
        self.wait(2)
        self.play(
            FadeOut(header),
            FadeOut(both_even),
            FadeOut(implies),
            FadeOut(contra),
            FadeOut(bang),
        )

    def _conclusion(self):
        header = self._section_header("Conclusion", color=PURPLE_C)

        box = RoundedRectangle(
            corner_radius=0.3,
            width=9,
            height=3,
            color=PURPLE_C,
            stroke_width=2,
        )

        result = MathTex(r"\therefore \; \sqrt{2} \notin \mathbb{Q}", font_size=52)
        result.move_to(box.get_center() + UP * 0.3)

        caption = Text(
            "Our assumption was false — √2 is irrational.",
            font_size=26,
            color=GRAY_A,
        )
        caption.move_to(box.get_center() + DOWN * 0.5)

        self.play(FadeIn(header))
        self.play(Create(box))
        self.play(Write(result))
        self.play(FadeIn(caption))
        self.wait(3)
        self.play(FadeOut(header), FadeOut(box), FadeOut(result), FadeOut(caption))


# --------------------------------------------------------------------------- #
#  How to render                                                               #
# --------------------------------------------------------------------------- #
#
#   pip install manim
#
#   Low-quality preview (fast):
#     manim -pql proof_by_contradiction.py ProofByContradiction
#
#   High-quality output (1080p):
#     manim -pqh proof_by_contradiction.py ProofByContradiction
#
#   Transparent background (for compositing):
#     manim -pqh --transparent proof_by_contradiction.py ProofByContradiction