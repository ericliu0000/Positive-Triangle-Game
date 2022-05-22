from manim import *
from constants import *
from graphs.amendedladder import TriangleLadderGraph
import util


class PlayTypes(Scene):
    ladder = TriangleLadderGraph()

    def construct(self):
        text = """This is an amended ladder graph
        with 9 vertices
        """

        text_objects = util.text_generator(text, DOWN)

