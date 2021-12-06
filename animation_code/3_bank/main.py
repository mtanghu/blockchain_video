from manim import *

class Bank(Scene):
    def construct(self):
        bank = ImageMobject("./bank.png").scale(0.75)
        self.play(FadeIn(bank))
        self.wait(1.5)

        bank.generate_target()
        bank.target.move_to(LEFT * 2.)

        card = ImageMobject("./card.png").scale(0.35)
        card.move_to((RIGHT * 3) + (UP * 1.5))  

        reader = ImageMobject("./reader.png").scale(1.25)
        reader.move_to(RIGHT * 2.)

        ledger_box = Rectangle(
            color = WHITE,
            height = 2.25,
            width = 1.5
        )

        ledger_entries = Group(
            MarkupText("<u>Bank Ledger</u>", font_size=12, color=BLUE),
            MarkupText("Sally has $100", font_size=12, color=YELLOW)
        )
        ledger_entries.arrange(DOWN)
        ledger_entries.next_to(ledger_box.get_top(), DOWN, SMALL_BUFF)

        ledger = Group(ledger_box, ledger_entries)
        ledger.next_to(bank.target.get_left(), LEFT)

        self.play(MoveToTarget(bank), FadeIn(card), FadeIn(reader), FadeIn(ledger))
        self.wait()

        card.generate_target()
        card.target.move_to((RIGHT * 3) + (DOWN * 1.5))

        reader_notif = Circle(0.02, color=GREEN, fill_opacity=1)
        reader_notif.next_to(reader.get_center(), (RIGHT * 0.4) + (UP * 0.75))

        self.play(AnimationGroup(MoveToTarget(card), FadeIn(reader_notif, scale=0.1), lag_ratio=0.1))

        block = self.get_block("Sally spent $100")
        block.next_to(reader.get_top(), UP)

        self.play(FadeIn(block), FadeOut(reader_notif))
        self.wait(1.5)

        block.generate_target()
        block.target.next_to(bank.get_top(), UP)

        self.play(MoveToTarget(block))
        self.wait()

        self.play(FadeOut(block, shift=DOWN))

        ledger_update = Text("Sally has $0", font_size=12, color=RED)
        ledger_update.next_to(ledger_entries.get_bottom(), DOWN, SMALL_BUFF)
        ledger.add(ledger_update)

        self.play(Write(ledger_update))
        self.wait(2.0)

        self.play(FadeOut(bank), FadeOut(ledger), FadeOut(card), FadeOut(reader))
        self.wait()
    
    def get_block(self, text, color=YELLOW):
        block = Rectangle(
            color = WHITE,
            height = 0.8,
            width = 1.5
        )

        block.add(MarkupText(text, font_size=12, color=color))
        
        return block
        
