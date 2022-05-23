from manim import *
from constants import *
from graphs.triangleladder import TriangleLadderGraph
import util


class PlayTypes(Scene):
    ladder = TriangleLadderGraph()

    def construct(self):
        text = f"""This is a triangular ladder graph
        with 9 vertices, <span {GRAPH_COLOR}>TL<sub>9</sub></span>.
        #
        Initially, a marked edge makes its <gradient {MEMBERS_GRADIENT}>member</gradient>
        triangles <gradient {ONE_COMPLETE_GRADIENT}>1-complete</gradient> during optimal play.
        #
        To <span {DOUBLE_UNDERLINE}>maximize</span> the game's moves, players
        will mark the lowest <gradient {POWER_LEVEL_GRADIENT}>power level</gradient> edges.
        #
        until all triangles in the graph
        are <gradient {ONE_COMPLETE_GRADIENT}>1-complete</gradient>.
        #
        So, 7 triangles are marked using <gradient {POWER_LEVEL_GRADIENT}>PL1</gradient>
        edges, and 2 more moves end the game.
        #
        To <span {DOUBLE_UNDERLINE}>minimize</span> the game's moves, players
        will mark the highest <gradient {POWER_LEVEL_GRADIENT}>power level</gradient> edges.
        #
        until all triangles in the graph
        are <gradient {ONE_COMPLETE_GRADIENT}>1-complete</gradient>.
        #
        In this case, 3 <gradient {POWER_LEVEL_GRADIENT}>PL2</gradient> edges are marked,
        making 6 triangles <gradient {ONE_COMPLETE_GRADIENT}>1-complete</gradient>.
        # 
        Marking one more <gradient {POWER_LEVEL_GRADIENT}>PL1</gradient> edge makes all
        triangles <gradient {ONE_COMPLETE_GRADIENT}>1-complete</gradient>,
        # 
        and two more moves end the game.

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

        self.wait(LONG_DWELL_TIME)

        # Cycle text and mark one edge
        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                  ReplacementTransform(text_objects[0][1], text_objects[1][1]),
                  Create(plus_1))

        util.bulk_indicate(self, g, [(1, 2), (1, 8), (2, 8)], run_time=LONG_ANIMATION_TIME)

        self.wait(LONG_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]),
                  ReplacementTransform(text_objects[1][1], text_objects[2][1]))

        util.bulk_indicate(self, g, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (1, 9)], run_time=LONG_ANIMATION_TIME)

        # Create all plus objects sequentially
        util.bulk_play(self, *[Create(obj, run_time=BRIEF_ANIMATION_TIME) for obj in [plus_2, plus_3, plus_4, plus_5, plus_6, plus_7]])

        # Cycle text
        self.play(ReplacementTransform(text_objects[2][0], text_objects[3][0]),
                  ReplacementTransform(text_objects[2][1], text_objects[3][1]))

        self.wait(LONG_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[3][0], text_objects[4][0]),
                  ReplacementTransform(text_objects[3][1], text_objects[4][1]))

        self.wait(LONG_DWELL_TIME)

        # Mark the minus edges and indicate positive triangle
        util.bulk_play(self, Create(minus_1), Create(minus_2))
        util.bulk_indicate(self, g, [(4, 5), (4, 6), (5, 6)], run_time=LONG_ANIMATION_TIME)

        self.wait(LONG_DWELL_TIME)

        # Deconstruct everything
        self.play(Uncreate(text_objects[4][0]), Uncreate(text_objects[4][1]))
        util.bulk_play(self, *[FadeOut(obj, run_time=SHORT_ANIMATION_TIME) for obj in [plus_1, plus_2, plus_3, plus_4, plus_5, plus_6, plus_7, minus_1, minus_2]])

        # Shift signs into new positions
        plus_1.move_to(g.edges[(1, 8)])
        plus_2.move_to(g.edges[(2, 7)])
        plus_3.move_to(g.edges[(3, 6)])
        plus_4.move_to(g.edges[(4, 5)])

        minus_1.move_to(g.edges[(4, 6)])
        minus_2.move_to(g.edges[(5, 6)])

        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[4][0], text_objects[5][0]),
                  ReplacementTransform(text_objects[4][1], text_objects[5][1]))

        util.bulk_indicate(self, g, [(1, 8), (2, 8), (2, 7), (3, 7), (3, 6), (4, 6)], run_time=LONG_ANIMATION_TIME)
        self.wait(LONG_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[5][0], text_objects[6][0]),
                  ReplacementTransform(text_objects[5][1], text_objects[6][1]))

        # Mark signs
        util.bulk_play(self, *[Create(obj, run_time=BRIEF_ANIMATION_TIME) for obj in [plus_1, plus_2, plus_3]])
        self.wait(LONG_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[6][0], text_objects[7][0]),
                  ReplacementTransform(text_objects[6][1], text_objects[7][1]))

        self.wait(LONG_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[7][0], text_objects[8][0]),
                  ReplacementTransform(text_objects[7][1], text_objects[8][1]))

        # Add PL1 edge to 1-complete
        self.play(Create(plus_4))
        self.wait(LONG_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[8][0], text_objects[9][0]),
                  ReplacementTransform(text_objects[8][1], text_objects[9][1]))

        # Add final moves
        util.bulk_play(self, Create(minus_1), Create(minus_2))

        self.wait(LONG_DWELL_TIME)

        # Indicate positive triangle
        util.bulk_indicate(self, g, [(4, 5), (4, 6), (5, 6)], run_time=LONG_ANIMATION_TIME)

        self.wait(LONG_DWELL_TIME)

        # Final deconstruction
        self.play(Uncreate(text_objects[9][0]), Uncreate(text_objects[9][1]))
        util.bulk_play(self, *[Uncreate(obj, run_time=SHORT_ANIMATION_TIME) for obj in [plus_1, plus_2, plus_3, plus_4, minus_1, minus_2]])
        self.play(Uncreate(g))

        self.wait(SHORT_DWELL_TIME)
