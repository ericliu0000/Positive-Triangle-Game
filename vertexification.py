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

        g = Graph(self.wheel.generate_vertices(5),
                  self.wheel.generate_edges(5),
                  layout="kamada_kawai", labels=True).shift(UP)

        self.play(Create(g))

        self.wait(LONG_DWELL_TIME * 3)
