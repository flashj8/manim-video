from manim import *

# ── Palette (3b1b-inspired, white background) ──────────────────────────────
WHITE_BG   = WHITE
INK        = "#1C1C1E"          # near-black for body text
BLUE_H     = "#3B82F6"          # highlight / step labels  (3b1b blue)
GOLD       = "#F59E0B"          # key algebra highlight
GREEN_H    = "#10B981"          # conclusion colour
GREY_SUB   = "#6B7280"          # subtle annotation colour

config.background_color = WHITE_BG

# Inter font stack  ──────────────────────────────────────────────────────────
# Manim uses the system font for Text(); make sure "Inter" is installed,
# or swap to "CMU Serif" for the classic 3b1b look.
FONT       = "Inter"
MATH_FONT  = None               # uses default LaTeX (Computer Modern)


class DirectProof(Scene):
    # ── helpers ────────────────────────────────────────────────────────────
    def label(self, txt, color=BLUE_H, scale=0.38):
        return Text(txt, font=FONT, color=color).scale(scale)

    def body(self, txt, color=INK, scale=0.42):
        return Text(txt, font=FONT, color=color).scale(scale)

    def math(self, tex, color=INK, scale=0.9):
        return MathTex(tex, color=color).scale(scale)

    def underline(self, mob, color=GOLD, buff=0.06):
        return Underline(mob, color=color, buff=buff, stroke_width=2.5)

    # ── scene ──────────────────────────────────────────────────────────────
    def construct(self):

        # ── 0. Title card ──────────────────────────────────────────────────
        title = Text("Direct Proof", font=FONT, color=INK).scale(0.72)
        subtitle = self.body("If n is even, then n² is even.", color=GREY_SUB, scale=0.40)
        VGroup(title, subtitle).arrange(DOWN, buff=0.18).move_to(ORIGIN)

        self.play(FadeIn(title, shift=UP*0.3), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(VGroup(title, subtitle)), run_time=0.5)

        # ── Layout anchor: left-flush column ──────────────────────────────
        LEFT_X  = -5.8
        TOP_Y   =  2.9
        ROW_GAP = 0.82          # vertical spacing between rows

        def row_pos(i):
            return np.array([LEFT_X, TOP_Y - i * ROW_GAP, 0])

        # ── 1. STEP 1 — Start with the definition ─────────────────────────
        step1_lbl  = self.label("Step 1 — Definition", color=BLUE_H)
        step1_body = self.body("If  n  is even, then  n = 2k  for some integer  k.", color=INK)
        step1_math = self.math(r"n = 2k, \quad k \in \mathbb{Z}", color=INK)

        step1_lbl .move_to(row_pos(0), aligned_edge=LEFT)
        step1_body.move_to(row_pos(1), aligned_edge=LEFT)
        step1_math.move_to(row_pos(2), aligned_edge=LEFT)

        self.play(Write(step1_lbl), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(step1_body, shift=RIGHT*0.15), run_time=0.8)
        self.wait(0.4)
        self.play(Write(step1_math), run_time=1.0)

        # Highlight "2k" inside the equation
        rect1 = SurroundingRectangle(step1_math, color=BLUE_H,
                                     buff=0.12, corner_radius=0.08, stroke_width=1.8)
        self.play(Create(rect1), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(rect1), run_time=0.3)

        # ── 2. STEP 2 — Square both sides ─────────────────────────────────
        step2_lbl  = self.label("Step 2 — Square both sides", color=BLUE_H)
        step2_math = self.math(r"n^2 = (2k)^2", color=INK)

        step2_lbl .move_to(row_pos(3.2), aligned_edge=LEFT)
        step2_math.move_to(row_pos(4.2), aligned_edge=LEFT)

        self.play(Write(step2_lbl), run_time=0.6)
        self.wait(0.2)
        self.play(Write(step2_math), run_time=0.9)
        self.wait(0.8)

        # ── 3. STEP 3 — Expand ────────────────────────────────────────────
        step3_lbl  = self.label("Step 3 — Expand", color=BLUE_H)
        step3_math = self.math(r"n^2 = 4k^2", color=INK)

        step3_lbl .move_to(row_pos(5.4), aligned_edge=LEFT)
        step3_math.move_to(row_pos(6.4), aligned_edge=LEFT)

        self.play(Write(step3_lbl), run_time=0.6)
        self.wait(0.2)

        # Transform (2k)² → 4k²  with a colour morph
        step2_copy = step2_math.copy()
        self.play(
            TransformMatchingShapes(step2_copy, step3_math),
            run_time=1.1
        )
        self.wait(0.8)

        # ── 4. STEP 4 — Factor out 2 ──────────────────────────────────────
        # Scroll everything up to make room
        all_so_far = VGroup(
            step1_lbl, step1_body, step1_math,
            step2_lbl, step2_math,
            step3_lbl, step3_math,
        )
        self.play(all_so_far.animate.shift(UP * 2.8), run_time=0.9)

        step4_lbl  = self.label("Step 4 — Factor out 2", color=BLUE_H)
        step4_math = self.math(r"n^2 = 2 \cdot (2k^2)", color=INK)

        step4_lbl .move_to(row_pos(3.4) + UP*2.8 - UP*2.8, aligned_edge=LEFT)
        step4_math.move_to(row_pos(4.4) + UP*2.8 - UP*2.8, aligned_edge=LEFT)
        # re-anchor relative to screen bottom area
        step4_group = VGroup(step4_lbl, step4_math).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        step4_group.move_to(np.array([LEFT_X + 0.0, -0.6, 0]), aligned_edge=LEFT)

        self.play(Write(step4_lbl), run_time=0.6)
        self.wait(0.2)
        self.play(Write(step4_math), run_time=1.0)

        # Brace + annotation on 2k²
        brace = Brace(step4_math, direction=DOWN, color=GREY_SUB)
        brace_lbl = self.body("integer  ⟹  call it  m", color=GREY_SUB, scale=0.36)
        brace_lbl.next_to(brace, DOWN, buff=0.12)
        self.play(GrowFromCenter(brace), FadeIn(brace_lbl), run_time=0.7)
        self.wait(1.0)
        self.play(FadeOut(brace), FadeOut(brace_lbl), run_time=0.4)

        # ── 5. CONCLUSION ─────────────────────────────────────────────────
        conc_lbl  = self.label("Conclusion", color=GREEN_H)
        conc_body = self.body("That's 2 × (an integer) — even by definition. ∎", color=GREEN_H, scale=0.42)
        conc_math = self.math(r"n^2 = 2m, \quad m = 2k^2 \in \mathbb{Z}", color=GREEN_H)

        conc_group = VGroup(conc_lbl, conc_math, conc_body).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        conc_group.move_to(np.array([LEFT_X, -2.5, 0]), aligned_edge=LEFT)

        box = SurroundingRectangle(conc_group, color=GREEN_H,
                                   buff=0.22, corner_radius=0.12, stroke_width=2.2)

        self.play(
            LaggedStart(
                Write(conc_lbl),
                Write(conc_math),
                FadeIn(conc_body, shift=UP*0.1),
                lag_ratio=0.35
            ),
            run_time=1.4
        )
        self.play(Create(box), run_time=0.6)
        self.wait(0.6)

        # Gold underline on the final math
        ul = self.underline(conc_math, color=GOLD)
        self.play(Create(ul), run_time=0.5)
        self.wait(2.0)

        # ── 6. Fade out everything ────────────────────────────────────────
        self.play(
            FadeOut(VGroup(all_so_far, step4_group, conc_group, box, ul)),
            run_time=1.0
        )

        # ── 7. QED card ───────────────────────────────────────────────────
        qed = Text("Q.E.D.", font=FONT, color=INK).scale(1.1)
        sub = self.body("quod erat demonstrandum", color=GREY_SUB, scale=0.38)
        VGroup(qed, sub).arrange(DOWN, buff=0.18)
        self.play(FadeIn(qed, shift=UP*0.2), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(2.5)
        self.play(FadeOut(VGroup(qed, sub)), run_time=0.8)