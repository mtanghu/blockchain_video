from manim import *

class Opener(Scene):
    def construct(self):
        self.wait(1.5)
        title = Text("Cryptocurrency", color=BLUE, font_size=100)
        self.play(Write(title))
        self.wait(1.5)
        self.play(Unwrite(title))
        self.wait()

        elon = ImageMobject("./elon.jpg").scale(0.2)
        elon.move_to(LEFT * 3)

        doge = ImageMobject("./doge.png")

        btc = SVGMobject("./btc.svg")
        btc.move_to(RIGHT * 3)

        self.play(AnimationGroup(FadeIn(elon), FadeIn(doge), FadeIn(btc), lag_ratio=0.75))
        self.wait()
