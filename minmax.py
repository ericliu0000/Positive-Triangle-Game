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
                  layout=self.ladder.generate_layout(9)).shift(UP).scale(1.5)

        # Create signs
        plus_1 = SVGMobject(file_name="res/plus.svg").scale(PLUS_SCALE)
        plus_2, plus_3, plus_4, plus_5, plus_6, plus_7 = [plus_1.copy() for _ in range(6)]

        minus_1 = SVGMobject(file_name="res/minus.svg").scale(MINUS_SCALE)
        minus_2 = minus_1.copy()

        # Set positions
        plus_1.move_to(g.edges[(1, 2)])
        plus_2.move_to(g.edges[(2, 3)])
        plus_3.move_to(g.edges[(3, 4)])
        plus_4.move_to(g.edges[(5, 6)])
        plus_5.move_to(g.edges[(6, 7)])
        plus_6.move_to(g.edges[(7, 8)])
        plus_7.move_to(g.edges[(8, 9)])

        minus_1.move_to(g.edges[(4, 5)])
        minus_2.move_to(g.edges[(4, 6)])

        # Create graph and text
        self.play(Create(g))
        util.bulk_play(self, Create(text_objects[0][0]), Create(text_objects[0][1]))

        # Cycle text and mark one edge
        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                  ReplacementTransform(text_objects[0][1], text_objects[1][1]),
                  Create(plus_1))

        util.bulk_indicate(self, g, [(1, 2), (1, 8), (2, 8)])

        #

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
