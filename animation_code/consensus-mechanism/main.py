from manim import *
import numpy as np

class ConsensusMechanism(Scene):
    def construct(self):
        chain = self.get_block_chain(2)

        users = VGroup(*[
            SVGMobject("./user.svg").scale(0.85) for _ in range(3)
        ])
        users.arrange(RIGHT, buff=SMALL_BUFF)
        users.move_to(UP * 2.5)

        hacker = ImageMobject("./new.png")
        hacker.move_to(DOWN * 2.5).scale(0.5)

        self.play(FadeIn(chain, users, hacker))
        self.wait()

        users_block = self.get_block(3)
        users_block.next_to(users.get_right(), RIGHT, SMALL_BUFF)

        hacker_block = self.get_block(3, color=RED)
        hacker_block.next_to(hacker.get_right(), RIGHT, SMALL_BUFF)

        self.play(FadeIn(users_block, hacker_block))
        self.wait()

        users_block.generate_target()
        users_block.target.next_to(chain.get_right(), RIGHT + (UP * 0.5), LARGE_BUFF)

        hacker_block.generate_target()
        hacker_block.target.next_to(chain.get_right(), RIGHT + (DOWN * 0.5), LARGE_BUFF)

        self.play(MoveToTarget(users_block), MoveToTarget(hacker_block))
        self.wait()

        users_start_arrow = Arrow(chain.get_right(), users_block.get_left())
        hacker_start_arrow = Arrow(chain.get_right(), hacker_block.get_left())
        self.play(FadeIn(users_start_arrow, hacker_start_arrow))


        users_chain = VGroup(users_block)
        hacker_chain = VGroup(hacker_block)
        conflict_chain = VGroup(chain, users_block, hacker_block, users_start_arrow, hacker_start_arrow)
        conflict_chain.generate_target()
        conflict_chain.target.move_to(LEFT)
        self.play(MoveToTarget(conflict_chain))
        self.wait()

        last_block = users_block
        for i in range(4, 6):
            users_block = self.get_block(i)
            users_block.next_to(users.get_right(), RIGHT, SMALL_BUFF)

            self.play(FadeIn(users_block))
            users_block.generate_target()
            users_block.target.next_to(conflict_chain.get_right(), RIGHT + (UP * 0.5), LARGE_BUFF)

            self.play(MoveToTarget(users_block))

            users_arrow = Arrow(last_block.get_right(), users_block.get_left())
            self.play(FadeIn(users_arrow))

            users_chain = VGroup(users_chain, users_block, users_arrow)
            conflict_chain = VGroup(conflict_chain, users_block, users_arrow)
            if i < 5:
                conflict_chain.generate_target()
                conflict_chain.target.move_to(LEFT)
                self.play(MoveToTarget(conflict_chain))
            last_block = users_block
            self.wait()
        
        users_block = self.get_block(6)
        users_block.next_to(users.get_right(), RIGHT, SMALL_BUFF)

        last_hacker_block = hacker_block
        hacker_block = self.get_block(4, color=RED)
        hacker_block.next_to(hacker.get_right(), RIGHT, SMALL_BUFF)

        self.play(FadeIn(users_block, hacker_block))

        users_block.generate_target()
        users_block.target.next_to(last_block.get_right(), RIGHT, LARGE_BUFF)

        hacker_block.generate_target()
        hacker_block.target.next_to(last_hacker_block.get_right(), RIGHT, LARGE_BUFF)

        self.play(MoveToTarget(users_block), MoveToTarget(hacker_block))
        
        users_arrow = Arrow(last_block.get_right(), users_block.get_left())
        hacker_arrow = Arrow(last_hacker_block.get_right(), hacker_block.get_left())
        self.play(FadeIn(users_arrow, hacker_arrow))

        users_chain = VGroup(users_chain, users_block, users_arrow)
        hacker_chain = VGroup(hacker_chain, hacker_block, hacker_arrow)

        users_chain.generate_target()
        users_chain.target.next_to(chain, RIGHT, LARGE_BUFF)
        
        self.play(FadeOut(users_start_arrow, hacker_start_arrow, hacker_chain), MoveToTarget(users_chain))

        users_arrow = Arrow(chain.get_right(), users_chain.get_left())
        self.play(FadeIn(users_arrow))

        final_chain = VGroup(users_chain, users_arrow, chain)
        final_chain.generate_target()
        final_chain.target.move_to(np.array([0., 0., 0.]))
        
        self.play(MoveToTarget(final_chain))
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
        
        
    