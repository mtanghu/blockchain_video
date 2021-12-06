from manim import *

class MisconceptionScene1(Scene):
    def construct(self):
        title = Text("First Misconception: Environmental concerns", color=BLUE).scale(.75)
        self.play(FadeIn(title))
        self.wait()

        title.generate_target()
        title.target.move_to(UP * 2.5)

        pow_computer = ImageMobject("./computer.png").scale(0.25)
        pow_computer.move_to((DOWN * 0.6))

        pow_text = Text("Proof of Work").scale(0.35)
        pow_text.next_to(pow_computer.get_bottom(), DOWN, MED_LARGE_BUFF)
        pow = Group(pow_computer, pow_text)

        self.play(MoveToTarget(title), FadeIn(pow))
        self.wait()

        pow_smoke = ImageMobject("./smoke.png").scale(0.25)
        pow_smoke.next_to(pow_computer.get_center(), UP, LARGE_BUFF)

        self.play(Wiggle(pow_computer, num_wiggles=3))
        self.play(FadeOut(pow_smoke, shift=UP))
        self.wait()

        pow.generate_target()
        pow.target.next_to(pow.get_center(), LEFT * 2.)

        pos_computer = ImageMobject("./computer.png").scale(0.25)
        pos_computer.move_to((DOWN * 0.6) + (RIGHT * 2.))

        pos_text = Text("Proof of Stake").scale(0.35)
        pos_text.next_to(pos_computer.get_bottom(), DOWN, MED_LARGE_BUFF)
        pos = Group(pos_computer, pos_text)

        self.play(MoveToTarget(pow), FadeIn(pos))
        self.wait()

        pow_smoke.next_to(pow_computer.get_center(), UP, LARGE_BUFF)

        pos_smoke = ImageMobject("./smoke.png").scale(0.15)
        pos_smoke.next_to(pos_computer.get_center(), UP, LARGE_BUFF)

        self.play(Wiggle(pow_computer, n_wiggles=4))
        self.play(Wiggle(pos_computer, n_wiggles=2))
        self.wait()
        self.play(FadeOut(pow_smoke, shift=UP), FadeOut(pos_smoke, shift=UP))
        self.wait()

        self.play(FadeOut(title), FadeOut(pow), FadeOut(pos))
        self.wait()
