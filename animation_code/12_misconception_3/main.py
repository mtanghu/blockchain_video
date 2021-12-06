from manim import *

class MisconceptionScene3(Scene):
    def construct(self):
        title = Text("Third Misconception: Intrinsic value", color=BLUE).scale(.75)
        self.play(FadeIn(title))
        self.wait()

        title.generate_target()
        title.target.move_to(UP * 2.5)

        dollar = ImageMobject("./dollar.png").scale(0.5)
        dollar.move_to(LEFT * 2)

        gold = ImageMobject("./gold.png").scale(0.8)
        gold.move_to(RIGHT * 2)

        self.play(MoveToTarget(title), FadeIn(dollar), FadeIn(gold))
        self.wait()

        gold.generate_target()
        gold.target.next_to(gold.get_center(), DOWN * 20)

        self.play(MoveToTarget(gold))
        self.wait()

        btc = SVGMobject("./btc.svg")
        btc.move_to(RIGHT * 2)

        self.play(FadeIn(btc))
        self.wait()

        gov = ImageMobject("./government.png").scale(0.2)
        gov.next_to(dollar.get_bottom(), DOWN)

        math = ImageMobject("./math.png").scale(0.75)
        math.next_to(btc.get_bottom(), DOWN * 0.6)

        self.play(FadeIn(gov), FadeIn(math))
        self.wait()

        self.play(FadeOut(title), FadeOut(dollar), FadeOut(btc), FadeOut(gov), FadeOut(math))
        self.wait()