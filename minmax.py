from manim import *
from constants import *
from graphs.triangleladder import TriangleLadderGraph
import util


class PlayTypes(Scene):
    ladder = TriangleLadderGraph()

    def construct(self):
        text = f"""This is a triangular ladder graph
        with 9 vertices, <span {GRAPH_COLOR}>T<sub>9</sub></span>.
        #
        Initially, a marked edge makes its member
        triangles <gradient {ONE_COMPLETE_GRADIENT}>1-complete</gradient> during optimal play.
        #
        To <span {DOUBLE_UNDERLINE}>maximize</span> the game's moves, players
        will mark the lowest <gradient {POWER_LEVEL_GRADIENT}>power level</gradient> edges.
        #
        until all triangles in the graph
        are <gradient {ONE_COMPLETE_GRADIENT}>1-complete</gradient>.
        #
        So, 7 triangles are marked using <gradient {POWER_LEVEL_GRADIENT}>PL</gradient>1
        edges, and 2 more moves ends the game.
        #
        To <span {DOUBLE_UNDERLINE}>minimize</span> the game's moves, players
        will mark the highest <gradient {POWER_LEVEL_GRADIENT}>power level</gradient> edges.
        #
        until all triangles in the graph
        are <gradient {ONE_COMPLETE_GRADIENT}>1-complete</gradient>.

        """

        text_objects = util.text_generator(text, DOWN)

        g = Graph(self.ladder.generate_vertices(9),
                    self.ladder.generate_edges(9),
                    layout=self.ladder.generate_layout(9)).shift(UP)

        # Create graph and text
        self.play(Create(g))
        util.bulk_play(Create(text_objects[0][0]), Create(text_objects[0][1]))

        # self.test(text_objects)

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

