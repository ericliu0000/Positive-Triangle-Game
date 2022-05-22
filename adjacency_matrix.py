from manim import *
from constants import *
from graphs.wheel import WheelGraph
import util


class MatrixTest(Scene):
    wheel = WheelGraph()

    def construct(self):
        text = f"""
        """

        text_objects = util.text_generator(text, DOWN)

        g = Graph(self.wheel.generate_vertices(5),
                    self.wheel.generate_edges(5),
                    layout="kamada_kawai").shift(UP + LEFT * 3)

        m = Matrix([0 for _ in range(5)] for _ in range(5)).shift(UP + RIGHT * 3.25)

        self.play(Create(g), Create(m))

        self.wait(LONG_DWELL_TIME * 3)
