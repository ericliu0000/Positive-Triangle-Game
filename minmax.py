from manim import *
from constants import *
from graphs.triangleladder import TriangleLadderGraph
import util


class PlayTypes(Scene):
    ladder = TriangleLadderGraph()

    def construct(self):
        text = """This is a triangular ladder graph
        with 9 vertices, T
        """

        text_objects = util.text_generator(text, DOWN)

