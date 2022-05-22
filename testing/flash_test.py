from manim import *


class FlashTest(Scene):
    def construct(self):
        g = Graph([1, 2, 3, 4, 5],
                  [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)],
                  layout="kamada_kawai")

        self.play(Create(g))

        self.wait(1)

        self.play(ShowPassingFlash(g.copy()))

        self.wait(3)