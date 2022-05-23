from manim import *


class Scratchpad(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        g = Graph([1, 2, 3, 4, 5],
                  [(1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5)], 
                  layout={1: (-1, 0, 0), 2: (0, 3, 0), 3: (0, 1, 0), 4: (0, 2, 0), 5: (1, 0, 0)}).scale(1.5).shift(DOWN)

        g.set_color(BLACK)

        self.add(g)
