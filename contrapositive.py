from manim import *

# ─── Config ────────────────────────────────────────────────────────────────
config.background_color = WHITE

# Palette
BLACK      = "#1A1A1A"
BLUE_D     = "#1565C0"
BLUE_L     = "#42A5F5"
GREEN_D    = "#2E7D32"
RED_D      = "#C62828"
GOLD       = "#F9A825"
GREY_L     = "#EEEEEE"
GREY_M     = "#BDBDBD"

FONT = "Inter"

def t(text, **kw):
    """Shorthand for Text with defaults."""
    kw.setdefault("font", FONT)
    kw.setdefault("color", BLACK)
    return Text(text, **kw)

def mt(tex, **kw):
    kw.setdefault("color", BLACK)
    return MathTex(tex, **kw)


# ═══════════════════════════════════════════════════════════════════════════
class ContrapositiveProof(Scene):
    # ── helpers ──────────────────────────────────────────────────────────
    def pill(self, mob, color=BLUE_L, opacity=0.15, buff=0.18, radius=0.18):
        box = SurroundingRectangle(
            mob, buff=buff, corner_radius=radius,
            color=color, fill_color=color, fill_opacity=opacity,
            stroke_width=2,
        )
        return box

    def section_title(self, text, color=BLUE_D):
        bar = Line(LEFT * 6.5, RIGHT * 6.5, color=color, stroke_width=2)
        bar.to_edge(UP, buff=0.3)
        label = t(text, font_size=26, weight=BOLD, color=color)
        label.next_to(bar, DOWN, buff=0.18)
        return VGroup(bar, label)

    def fade_replace(self, old, new, run_time=0.5):
        self.play(FadeOut(old, shift=UP * 0.15),
                  FadeIn(new,  shift=UP * 0.15),
                  run_time=run_time)

    # ── scenes ───────────────────────────────────────────────────────────
    def construct(self):
        self.s1_key_fact()
        self.s2_example()
        self.s3_statement()
        self.s4_direct_struggle()
        self.s5_contrapositive()
        self.s6_proof()
        self.s7_conclusion()

    # ── Scene 1 : The Key Fact ────────────────────────────────────────────
    def s1_key_fact(self):
        title = t("The Key Fact", font_size=44, weight=BOLD, color=BLUE_D)
        title.to_edge(UP, buff=0.7)

        arrow_label = mt(r"p \Rightarrow q", font_size=42, color=BLACK)
        equiv       = mt(r"\iff", font_size=42, color=GOLD)
        contra      = mt(r"\lnot q \Rightarrow \lnot p", font_size=42, color=BLACK)

        row = VGroup(arrow_label, equiv, contra).arrange(RIGHT, buff=0.5)
        row.next_to(title, DOWN, buff=0.7)

        p1 = self.pill(arrow_label, BLUE_L)
        p2 = self.pill(contra, GREEN_D, opacity=0.12)

        subtitle = t(
            "These two statements are logically identical.\n"
            "Proving one is the same as proving the other.",
            font_size=24, line_spacing=1.5,
        )
        subtitle.next_to(row, DOWN, buff=0.55)

        self.play(Write(title), run_time=0.9)
        self.wait(0.3)
        self.play(FadeIn(p1), Write(arrow_label), run_time=0.7)
        self.wait(0.2)
        self.play(Write(equiv), run_time=0.4)
        self.play(FadeIn(p2), Write(contra), run_time=0.7)
        self.wait(0.5)
        self.play(FadeIn(subtitle, shift=DOWN * 0.1))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [title, p1, arrow_label, equiv,
                                          p2, contra, subtitle]])

    # ── Scene 2 : Motivating Example ─────────────────────────────────────
    def s2_example(self):
        head = t("A Motivating Example", font_size=38, weight=BOLD, color=BLUE_D)
        head.to_edge(UP, buff=0.6)

        original = t('"If I have bad grades,\nthen I will fail this class."',
                     font_size=26, line_spacing=1.45, slant=ITALIC)
        original.next_to(head, DOWN, buff=0.55)
        orig_box = self.pill(original, BLUE_L, opacity=0.12, buff=0.28)

        arrow_down = Arrow(
            original.get_bottom() + DOWN * 0.1,
            original.get_bottom() + DOWN * 0.65,
            color=GOLD, stroke_width=3, max_tip_length_to_length_ratio=0.25,
        )
        equiv_label = t("Logically equivalent  (contrapositive)",
                        font_size=21, color=GOLD)
        equiv_label.next_to(arrow_down, RIGHT, buff=0.22)

        contra = t('"If I pass this class,\nthen I have good grades."',
                   font_size=26, line_spacing=1.45, slant=ITALIC)
        contra.next_to(arrow_down, DOWN, buff=0.1)
        contra_box = self.pill(contra, GREEN_D, opacity=0.10, buff=0.28)

        note = t("Proving either statement proves both.",
                 font_size=23, color=GREY_M)
        note.next_to(contra, DOWN, buff=0.5)

        self.play(Write(head))
        self.play(FadeIn(orig_box), Write(original), run_time=0.9)
        self.wait(1)
        self.play(GrowArrow(arrow_down), FadeIn(equiv_label))
        self.play(FadeIn(contra_box), Write(contra), run_time=0.9)
        self.wait(1)
        self.play(FadeIn(note, shift=DOWN * 0.1))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [head, orig_box, original,
                                          arrow_down, equiv_label,
                                          contra_box, contra, note]])

    # ── Scene 3 : The Statement to Prove ──────────────────────────────────
    def s3_statement(self):
        head = t("What We Want to Prove", font_size=38, weight=BOLD, color=BLUE_D)
        head.to_edge(UP, buff=0.6)

        claim = mt(
            r"\text{If } n^2 \text{ is odd, then } n \text{ is odd.}",
            font_size=42,
        )
        claim.next_to(head, DOWN, buff=0.8)
        claim_box = self.pill(claim, BLUE_L, opacity=0.13, buff=0.35, radius=0.22)

        p_label = t("p", font_size=22, color=BLUE_D, weight=BOLD)
        q_label = t("q", font_size=22, color=GREEN_D, weight=BOLD)

        p_brace = Brace(claim[0][4:14], DOWN, color=BLUE_D, buff=0.06)   # "n² is odd"
        q_brace = Brace(claim[0][20:],  DOWN, color=GREEN_D, buff=0.06)  # "n is odd"

        p_label.next_to(p_brace, DOWN, buff=0.08)
        q_label.next_to(q_brace, DOWN, buff=0.08)

        note = t(
            "Strategy: prove the contrapositive instead.",
            font_size=25, color=RED_D,
        )
        note.next_to(claim, DOWN, buff=1.1)

        self.play(Write(head))
        self.play(FadeIn(claim_box), Write(claim), run_time=1.0)
        self.wait(0.5)
        self.play(
            GrowFromCenter(p_brace), FadeIn(p_label),
            GrowFromCenter(q_brace), FadeIn(q_label),
        )
        self.wait(1.2)
        self.play(FadeIn(note, shift=DOWN * 0.1))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [head, claim_box, claim,
                                          p_brace, q_brace,
                                          p_label, q_label, note]])

    # ── Scene 4 : Why Direct Is Awkward ───────────────────────────────────
    def s4_direct_struggle(self):
        head = t("Direct Proof — Why It's Awkward",
                 font_size=34, weight=BOLD, color=RED_D)
        head.to_edge(UP, buff=0.6)

        attempt = VGroup(
            t("Assume n² is odd.", font_size=27),
            t('Write  n² = 2k + 1  for some integer k.', font_size=27),
            t("Now solve for n … but that gives n = √(2k+1).", font_size=27),
            t("√ of an odd number — is that always odd?  🤔", font_size=27, color=RED_D),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        attempt.next_to(head, DOWN, buff=0.55)

        cross = Cross(attempt, color=RED_D, stroke_width=3)

        redirect = t(
            "The negation of the hypothesis doesn't give us a clean\n"
            "algebraic foothold.  The contrapositive does.",
            font_size=23, line_spacing=1.5, color=BLUE_D,
        )
        redirect.next_to(attempt, DOWN, buff=0.55)

        self.play(Write(head))
        for line in attempt:
            self.play(FadeIn(line, shift=RIGHT * 0.1), run_time=0.55)
            self.wait(0.25)
        self.wait(0.8)
        self.play(Create(cross), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(redirect, shift=DOWN * 0.1))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [head, attempt, cross, redirect]])

    # ── Scene 5 : Forming the Contrapositive ──────────────────────────────
    def s5_contrapositive(self):
        head = t("Forming the Contrapositive",
                 font_size=36, weight=BOLD, color=BLUE_D)
        head.to_edge(UP, buff=0.6)

        orig = mt(
            r"n^2 \text{ odd} \;\Rightarrow\; n \text{ odd}",
            font_size=36, color=BLACK,
        )
        orig.next_to(head, DOWN, buff=0.6)
        orig_label = t("Original", font_size=19, color=GREY_M)
        orig_label.next_to(orig, LEFT, buff=0.4)

        arrow = mt(r"\Big\Updownarrow", font_size=36, color=GOLD)
        arrow.next_to(orig, DOWN, buff=0.28)
        equiv_txt = t("logically equivalent", font_size=19, color=GOLD)
        equiv_txt.next_to(arrow, RIGHT, buff=0.2)

        contra = mt(
            r"n \text{ even} \;\Rightarrow\; n^2 \text{ even}",
            font_size=36, color=BLACK,
        )
        contra.next_to(arrow, DOWN, buff=0.28)
        contra_label = t("Contrapositive", font_size=19, color=GREEN_D, weight=BOLD)
        contra_label.next_to(contra, LEFT, buff=0.4)
        contra_box = self.pill(contra, GREEN_D, opacity=0.13, buff=0.28, radius=0.2)

        note = t(
            "¬(n is odd)  =  n is even\n"
            "¬(n² is odd) = n² is even\n"
            "Both negations are clean — perfect for algebra.",
            font_size=22, line_spacing=1.5, color=BLACK,
        )
        note.next_to(contra, DOWN, buff=0.55)
        note_bg = self.pill(note, GOLD, opacity=0.10, buff=0.28)

        self.play(Write(head))
        self.play(Write(orig), FadeIn(orig_label))
        self.wait(0.5)
        self.play(Write(arrow), FadeIn(equiv_txt))
        self.play(FadeIn(contra_box), Write(contra), FadeIn(contra_label))
        self.wait(0.8)
        self.play(FadeIn(note_bg), FadeIn(note, shift=DOWN * 0.1))
        self.wait(2.8)

        self.play(*[FadeOut(m) for m in [head, orig, orig_label, arrow,
                                          equiv_txt, contra_box, contra,
                                          contra_label, note_bg, note]])

    # ── Scene 6 : The Proof ───────────────────────────────────────────────
    def s6_proof(self):
        head = t("The Direct Proof  (of the Contrapositive)",
                 font_size=33, weight=BOLD, color=GREEN_D)
        head.to_edge(UP, buff=0.5)

        steps = [
            (r"\textbf{Assume: } n \text{ is even.}", BLACK),
            (r"\text{Then } n = 2k \text{ for some integer } k.", BLACK),
            (r"n^2 = (2k)^2 = 4k^2 = 2(2k^2)", BLUE_D),
            (r"\text{Since } 2k^2 \text{ is an integer, } n^2 = 2(\cdot)\text{ is even.}", GREEN_D),
            (r"\therefore\; n^2 \text{ is even.} \quad \blacksquare", RED_D),
        ]

        step_mobs = VGroup(*[
            mt(s, font_size=30, color=c) for s, c in steps
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        step_mobs.next_to(head, DOWN, buff=0.55)

        boxes = [
            self.pill(step_mobs[2], BLUE_L, opacity=0.13),
            self.pill(step_mobs[3], GREEN_D, opacity=0.10),
            self.pill(step_mobs[4], RED_D,   opacity=0.10),
        ]

        self.play(Write(head))
        for i, mob in enumerate(step_mobs):
            if i >= 2:
                self.play(FadeIn(boxes[i - 2]))
            self.play(Write(mob), run_time=0.75)
            self.wait(0.5 if i < 4 else 1.2)

        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [head, step_mobs, *boxes]])

    # ── Scene 7 : Conclusion ──────────────────────────────────────────────
    def s7_conclusion(self):
        head = t("Conclusion", font_size=42, weight=BOLD, color=BLUE_D)
        head.to_edge(UP, buff=0.6)

        chain = VGroup(
            mt(r"n \text{ even} \;\Rightarrow\; n^2 \text{ even}", font_size=34,
               color=GREEN_D),
            mt(r"\Big\Updownarrow", font_size=34, color=GOLD),
            mt(r"n^2 \text{ odd} \;\Rightarrow\; n \text{ odd}", font_size=34,
               color=BLUE_D),
        ).arrange(DOWN, buff=0.28)
        chain.next_to(head, DOWN, buff=0.6)
        chain_box = self.pill(chain, BLUE_L, opacity=0.10, buff=0.4, radius=0.25)

        proved_tag = t("✓  Proved!", font_size=28, weight=BOLD, color=GREEN_D)
        proved_tag.next_to(chain_box, RIGHT, buff=0.45)

        takeaway = t(
            "The contrapositive is most powerful\n"
            "when the negation of the conclusion\n"
            "gives you something concrete to work with.",
            font_size=23, line_spacing=1.55, color=BLACK,
        )
        takeaway.next_to(chain, DOWN, buff=0.65)
        take_box = self.pill(takeaway, GOLD, opacity=0.10, buff=0.3)

        self.play(Write(head))
        self.play(FadeIn(chain_box))
        for mob in chain:
            self.play(Write(mob), run_time=0.65)
            self.wait(0.25)
        self.wait(0.4)
        self.play(FadeIn(proved_tag, scale=1.15))
        self.wait(0.6)
        self.play(FadeIn(take_box), FadeIn(takeaway, shift=DOWN * 0.1))
        self.wait(3.5)

        self.play(*[FadeOut(m) for m in
                    [head, chain_box, *chain, proved_tag, take_box, takeaway]])
        self.wait(0.3)