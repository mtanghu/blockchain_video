from manim import *

class Misconception(Scene):
    def construct(self):
        title = Text("Common Misconceptions", color=BLUE)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
