from manim import *

# ── Palette (3b1b-inspired, white background) ──────────────────────────────
BG        = WHITE
INK       = "#1C1C1E"          # near-black for body text
BLUE      = "#3B82F6"          # highlight / formula accent
GREEN     = "#16A34A"          # ✓ check-mark colour
ORANGE    = "#EA580C"          # inductive-step accent
PURPLE    = "#7C3AED"          # k+1 emphasis


def ink(opacity=1):
    return ManimColor(INK).from_hex(INK)


# ── Font helper ────────────────────────────────────────────────────────────
FONT = "Inter"          # install via `pip install manim` + Inter on system
                        # fall back to "sans-serif" if unavailable


def Txt(s, size=32, color=INK, weight=NORMAL, **kw):
    return Text(s, font=FONT, font_size=size, color=color,
                weight=weight, **kw)


def Eq(s, color=INK, size=36, **kw):
    return MathTex(s, color=color, font_size=size, **kw)


# ══════════════════════════════════════════════════════════════════════════
class InductionProof(Scene):
    """
    Proof by induction that  1+2+…+n = n(n+1)/2.
    White background, Inter font, 3Blue1Brown style.
    """

    def setup(self):
        self.camera.background_color = BG

    # ── helpers ────────────────────────────────────────────────────────────
    def section_title(self, label: str, color=INK):
        bar  = Line(LEFT * 6, RIGHT * 6, stroke_width=1.5, color=color)
        text = Txt(label, size=28, color=color, weight=BOLD)
        grp  = VGroup(text, bar).arrange(DOWN, buff=0.12)
        return grp

    def fade_in_down(self, *mobjects, lag=0.08):
        anims = []
        for m in mobjects:
            m.shift(UP * 0.3)
            anims.append(AnimationGroup(
                FadeIn(m, shift=DOWN * 0.3)))
        return LaggedStart(*anims, lag_ratio=lag)

    # ── main ───────────────────────────────────────────────────────────────
    def construct(self):
        self._scene_title()
        self._scene_base_case()
        self._scene_inductive_step()
        self._scene_conclusion()

    # ══════════════════════════════════════════════════════════════════════
    # 0 ▸ Opening statement
    # ══════════════════════════════════════════════════════════════════════
    def _scene_title(self):
        claim_lbl = Txt("Claim", size=22, color=BLUE, weight=BOLD)
        formula   = Eq(
            r"1 + 2 + \cdots + n \;=\; \frac{n(n+1)}{2}",
            size=42, color=INK)
        for_all   = Txt("for every positive integer  n", size=24, color=INK)

        block = VGroup(claim_lbl, formula, for_all).arrange(DOWN, buff=0.35)
        block.move_to(ORIGIN)

        # decorative bracket lines
        left_line  = Line(UP * 1.2, DOWN * 1.2,
                          stroke_width=3, color=BLUE).next_to(block, LEFT, buff=0.25)
        right_line = Line(UP * 1.2, DOWN * 1.2,
                          stroke_width=3, color=BLUE).next_to(block, RIGHT, buff=0.25)

        self.play(self.fade_in_down(claim_lbl))
        self.play(Write(formula), run_time=1.6)
        self.play(FadeIn(for_all, shift=UP * 0.2))
        self.play(GrowFromCenter(left_line),
                  GrowFromCenter(right_line), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(VGroup(block, left_line, right_line)))

    # ══════════════════════════════════════════════════════════════════════
    # 1 ▸ Base Case  (n = 1)
    # ══════════════════════════════════════════════════════════════════════
    def _scene_base_case(self):
        title = self.section_title("Base Case:  n = 1", color=BLUE)
        title.to_edge(UP, buff=0.55)
        self.play(Write(title), run_time=0.9)
        self.wait(0.3)

        # LHS
        lhs_lbl = Txt("Sum:", size=24, color=INK)
        lhs_eq  = Eq(r"1", size=44, color=INK)
        lhs_grp = VGroup(lhs_lbl, lhs_eq).arrange(RIGHT, buff=0.2)

        # RHS
        rhs_lbl = Txt("Formula:", size=24, color=INK)
        rhs_eq  = Eq(
            r"\frac{1\cdot(1+1)}{2} = \frac{2}{2} = 1",
            size=44, color=INK)
        rhs_grp = VGroup(rhs_lbl, rhs_eq).arrange(RIGHT, buff=0.2)

        body = VGroup(lhs_grp, rhs_grp).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        body.move_to(ORIGIN + DOWN * 0.2)

        self.play(self.fade_in_down(lhs_grp))
        self.wait(0.4)
        self.play(self.fade_in_down(rhs_grp))
        self.wait(0.6)

        # Highlight the matching "1"s
        box_lhs = SurroundingRectangle(lhs_eq,  color=GREEN, buff=0.12, stroke_width=2)
        box_rhs = SurroundingRectangle(
            rhs_eq[-1],  # the trailing "1"
            color=GREEN, buff=0.12, stroke_width=2)

        self.play(Create(box_lhs), Create(box_rhs), run_time=0.7)

        check = Txt("✓", size=52, color=GREEN)
        check.next_to(body, RIGHT, buff=0.5)
        self.play(FadeIn(check, scale=1.4))
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, body, box_lhs, box_rhs, check)))

    # ══════════════════════════════════════════════════════════════════════
    # 2 ▸ Inductive Step
    # ══════════════════════════════════════════════════════════════════════
    def _scene_inductive_step(self):
        title = self.section_title("Inductive Step", color=ORANGE)
        title.to_edge(UP, buff=0.55)
        self.play(Write(title), run_time=0.9)

        # ── 2a  Inductive hypothesis ──────────────────────────────────────
        hyp_lbl = Txt("Assume for  n = k:", size=24, color=INK)
        hyp_eq  = Eq(
            r"1 + 2 + \cdots + k \;=\; \frac{k(k+1)}{2}",
            size=38, color=INK)
        hyp_box = SurroundingRectangle(
            hyp_eq, color=ORANGE, buff=0.18, stroke_width=2,
            corner_radius=0.1)
        hyp_grp = VGroup(hyp_lbl, VGroup(hyp_eq, hyp_box)).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        hyp_grp.next_to(title, DOWN, buff=0.55).to_edge(LEFT, buff=0.8)

        self.play(self.fade_in_down(hyp_lbl))
        self.play(Write(hyp_eq), run_time=1.2)
        self.play(Create(hyp_box), run_time=0.5)
        self.wait(0.8)

        # ── 2b  Goal ──────────────────────────────────────────────────────
        goal_lbl = Txt("Show for  n = k + 1:", size=24, color=PURPLE, weight=BOLD)
        goal_eq  = Eq(
            r"1 + 2 + \cdots + k + (k+1) \;=\; \frac{(k+1)(k+2)}{2}",
            size=34, color=PURPLE)
        goal_grp = VGroup(goal_lbl, goal_eq).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        goal_grp.next_to(hyp_grp, DOWN, buff=0.45).to_edge(LEFT, buff=0.8)

        self.play(self.fade_in_down(goal_lbl, goal_eq))
        self.wait(0.7)

        self.play(FadeOut(VGroup(title, hyp_grp, goal_grp)))

        # ── 2c  Algebraic chain ───────────────────────────────────────────
        self._scene_algebra()

    def _scene_algebra(self):
        title2 = self.section_title("Inductive Step  —  algebra", color=ORANGE)
        title2.to_edge(UP, buff=0.45)
        self.play(Write(title2), run_time=0.7)

        # Step labels + equations, built as a vertical chain
        steps = [
            (Txt("Start:", size=22, color=INK),
             Eq(r"1 + 2 + \cdots + k + (k+1)", size=34, color=INK)),

            (Txt("Apply inductive hypothesis:", size=22, color=ORANGE),
             Eq(r"= \;\frac{k(k+1)}{2} + (k+1)", size=34, color=INK)),

            (Txt("Factor out  (k+1):", size=22, color=INK),
             Eq(r"= \;(k+1)\!\left(\frac{k}{2} + 1\right)", size=34, color=INK)),

            (Txt("Simplify:", size=22, color=INK),
             Eq(r"= \;\frac{(k+1)(k+2)}{2}", size=34, color=BLUE)),
        ]

        group_rows = []
        for lbl, eq in steps:
            row = VGroup(lbl, eq).arrange(RIGHT, buff=0.3)
            group_rows.append(row)

        chain = VGroup(*group_rows).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        chain.next_to(title2, DOWN, buff=0.45).to_edge(LEFT, buff=0.7)

        for i, row in enumerate(group_rows):
            if i == 0:
                self.play(self.fade_in_down(row))
            else:
                arrow = Tex(r"$\downarrow$", color=INK, font_size=30)
                arrow.next_to(group_rows[i - 1], DOWN, buff=0.05).align_to(
                    group_rows[i - 1], LEFT)
                self.play(FadeIn(arrow))
                self.play(self.fade_in_down(row))
            self.wait(0.6)

        # Highlight final result
        final_box = SurroundingRectangle(
            group_rows[-1][1], color=BLUE, buff=0.15,
            stroke_width=2.5, corner_radius=0.1)
        self.play(Create(final_box))
        self.wait(0.4)

        check = Txt("✓", size=52, color=GREEN)
        check.next_to(final_box, RIGHT, buff=0.3)
        self.play(FadeIn(check, scale=1.4))
        self.wait(1.8)

        self.play(FadeOut(VGroup(title2, chain, final_box, check)))

    # ══════════════════════════════════════════════════════════════════════
    # 3 ▸ Conclusion
    # ══════════════════════════════════════════════════════════════════════
    def _scene_conclusion(self):
        # Domino metaphor — simple rectangles falling
        dominos = self._build_dominos(n=7)
        dominos.move_to(ORIGIN + DOWN * 0.5)

        conclusion = Txt(
            "Every domino falls.", size=38, color=INK, weight=BOLD)
        conclusion.to_edge(UP, buff=1.1)

        formula_final = Eq(
            r"1 + 2 + \cdots + n \;=\; \frac{n(n+1)}{2}",
            size=36, color=BLUE)
        formula_final.next_to(conclusion, DOWN, buff=0.4)

        qed_dot = Eq(r"\blacksquare", size=30, color=INK)
        qed_dot.to_corner(DR, buff=0.5)

        # show standing dominos
        self.play(LaggedStart(
            *[GrowFromEdge(d, DOWN) for d in dominos],
            lag_ratio=0.12), run_time=1.2)
        self.wait(0.3)

        # topple them left→right
        self.play(LaggedStart(
            *[d.animate.rotate(-PI / 2, about_edge=DOWN).set_color(BLUE)
              for d in dominos],
            lag_ratio=0.14), run_time=1.6)
        self.wait(0.4)

        self.play(Write(conclusion))
        self.play(Write(formula_final), run_time=1.2)
        self.play(FadeIn(qed_dot, scale=1.3))
        self.wait(2.5)

    # ── domino builder ─────────────────────────────────────────────────────
    @staticmethod
    def _build_dominos(n=7, width=0.28, height=0.85, gap=0.18):
        dominos = VGroup()
        x = 0
        for _ in range(n):
            rect = Rectangle(
                width=width, height=height,
                fill_color=INK, fill_opacity=1,
                stroke_color=INK, stroke_width=0)
            rect.move_to(RIGHT * x + DOWN * (height / 2 - height / 2))
            dominos.add(rect)
            x += width + gap
        dominos.center()
        return dominos