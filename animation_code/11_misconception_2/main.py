from manim import *

class MisconceptionScene2(Scene):
    def construct(self):
        title = Text("Second Misconception: Privacy", color=BLUE).scale(.75)
        self.play(FadeIn(title))
        self.wait()

        title.generate_target()
        title.target.move_to(UP * 2.5)

        chain_blocks = self.get_block_chain(4)
        chain_text = Text("Blockchain").scale(0.35)
        chain_text.next_to(chain_blocks.get_center(), DOWN, LARGE_BUFF)
        chain = Group(chain_blocks, chain_text)

        self.play(MoveToTarget(title), FadeIn(chain))
        self.wait()

        m_glass = ImageMobject("./magnifying-glass.png").scale(0.6)
        m_glass.move_to(LEFT * 5 + DOWN * 5)

        m_glass.generate_target()
        m_glass.target.move_to(chain_blocks.get_left() + (RIGHT * 0.65) + (DOWN * 0.4))
        self.play(MoveToTarget(m_glass))
        self.wait()

        m_glass.target.move_to(chain_blocks.get_center() + (RIGHT * 1.15) + (DOWN * 0.4))
        self.play(MoveToTarget(m_glass))
        self.wait()

        m_glass.target.move_to(chain_blocks.get_right() + (LEFT * 0.05) + (DOWN * 0.4))
        self.play(MoveToTarget(m_glass))
        self.wait()

        self.play(FadeOut(title), FadeOut(chain), FadeOut(m_glass))
        self.wait()

    def get_block_chain(self, num):
        blocks = VGroup(*[
            self.get_block(x + 1) for x in range(num)
        ])
        blocks.arrange(RIGHT, buff=LARGE_BUFF)
        arrows = VGroup()

        for b1, b2 in zip(blocks, blocks[1:]):
            arrow = Arrow(b1.get_right(), b2.get_left())
            arrows.add(arrow)
        
        block_chain = VGroup(blocks, arrows)
        block_chain.block = blocks
        block_chain.arrows = arrows
        return block_chain
    
    def get_block(self, id, color=YELLOW):
        block = Rectangle(
            color = WHITE,
            height = 0.8,
            width = 0.8
        )

        block.add(MarkupText(f'Tx. #{id}', font_size=12, color=color))
        
        return block