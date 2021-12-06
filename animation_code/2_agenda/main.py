from manim import *

class Agenda(Scene):
    def construct(self):
        title = Text("Agenda", color=BLUE, font_size=80)
        self.play(FadeIn(title))
        self.wait()

        title.generate_target()
        title.target.move_to(UP * 2.5)

        agenda = Group(
            Text("Inner-Workings of Blockchain", font_size=40, color=YELLOW),
            Text("Applications", font_size=40, color=YELLOW),
            Text("Common Misconceptions", font_size=40, color=YELLOW)
        )
        agenda.arrange(DOWN)

        self.play(AnimationGroup(MoveToTarget(title), *[FadeIn(i) for i in agenda], lag_ratio=1))
        self.wait(3)


        self.play(AnimationGroup(FadeOut(title), *[FadeOut(i) for i in agenda], lag_ratio=1))
        self.wait()
