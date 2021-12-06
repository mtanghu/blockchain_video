from manim import *

class Trust(Scene):
    def construct(self):
        title = MarkupText("This system relies on trust.", color=BLUE, font_size=40)
        self.play(Write(title))
        self.wait(3)