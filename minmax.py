from manim import *
from constants import *
from graphs.triangleladder import TriangleLadderGraph
import util


class PlayTypes(Scene):
    ladder = TriangleLadderGraph()

    def construct(self):
        text = """This is a triangular ladder graph
        with 9 vertices, <span foreground="red">T<sub>9</sub></span>.
        #
        Initially, a marked edge makes its member
        triangles 1-complete during optimal play.
        #
        To <span underline="double" underline_color="red">maximize</span> the game's moves, players
        will mark the lowest power level edges.
        #
        until all triangles in the graph
        are 1-complete.
        #
        So, 7 triangles are marked using PL1
        edges, and 2 more moves ends the game.
        """

        text_objects = util.text_generator(text, DOWN)

        self.test(text_objects)

        self.wait(SHORT_DWELL_TIME * 3)


    def test(self, text_objects):
        self.play(Create(text_objects[0][1]), Create(text_objects[0][0]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                    ReplacementTransform(text_objects[0][1], text_objects[1][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]),
                    ReplacementTransform(text_objects[1][1], text_objects[2][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[2][0], text_objects[3][0]),
                    ReplacementTransform(text_objects[2][1], text_objects[3][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[3][0], text_objects[4][0]),
                    ReplacementTransform(text_objects[3][1], text_objects[4][1]))

        self.wait(SHORT_DWELL_TIME)

