from manim import *
from constants import *
from graphs.wheel import WheelGraph
from graphs.vertexify import Vertexify
import util


class Vertexification(Scene):
    wheel = WheelGraph()
    vertexify = Vertexify()

    def construct(self):
        text = f"""
        #
        """

        text_objects = util.text_generator(text, DOWN * 1.5)

        g = Graph(self.wheel.generate_vertices(7),
                  self.wheel.generate_edges(7),
                  layout=W7_LAYOUT, labels=False).shift(UP + LEFT * 3).scale(1.2)

        xg = Graph(self.vertexify.generate_vertices(g.edges),
                     self.vertexify.generate_edges(g.edges),
                    layout=XW7_LAYOUT, labels=False).shift(UP + RIGHT * 3).scale(1.2)

        self.play(Create(xg), Create(g))

        self.wait(LONG_DWELL_TIME * 3)
