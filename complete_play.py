from manim import *
from constants import *
from graphs.complete import CompleteGraph
import util


class CompletePlay(Scene):
    complete = CompleteGraph()

    def construct(self):
        text = f"""This is complete graph <span {GRAPH_COLOR}>K<sub>5</sub></span>
        #
        Every vertex has a <gradient {POWER_LEVEL_GRADIENT}>power level</gradient> of 3.
        #
        Optimal play with <span {GRAPH_COLOR}>K<sub>5</sub></span>
        """

        text_objects = util.text_generator(text, DOWN * 2.5)

        # Make graph
        g = Graph(self.complete.generate_vertices(5),
                  self.complete.generate_edges(5),
                  layout=K5_LAYOUT).shift(UP * 0.5).scale(2)

        # Make signs
        plus_1 = SVGMobject(file_name="res/plus.svg").scale(PLUS_SCALE)
        plus_2, plus_3 = plus_1.copy(), plus_1.copy()

        minus_1 = SVGMobject(file_name="res/minus.svg").scale(MINUS_SCALE)

        # Set positions
        plus_1.move_to(g.edges[(0, 4)])
        plus_2.move_to(g.edges[(0, 1)])
        plus_3.move_to(g.edges[(1, 4)])
        minus_1.move_to(g.edges[(2, 3)])

        # Create graph and text
        self.play(Create(g), Create(text_objects[0][0]))

        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]))

        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]))

        self.wait(SHORT_DWELL_TIME)

        # Mark minus
        self.play(Create(minus_1))

        # Color 1-complete triangles
        util.bulk_indicate(self, g, [(1, 2), (1, 3), (2, 3)])
        util.recolor(self, g, [(1, 2), (1, 3), (2, 3)], BLUE_D)

        util.bulk_indicate(self, g, [(0, 2), (0, 3)])
        util.recolor(self, g, [(0, 2), (0, 3)], TEAL_B)

        util.bulk_indicate(self, g, [(2, 4), (3, 4)])
        util.recolor(self, g, [(2, 4), (3, 4)], PURE_RED)

        self.wait(LONG_DWELL_TIME)

        # Mark plus
        self.play(Create(plus_1))

        # Color 1-complete triangles
        util.bulk_indicate(self, g, [(0, 1), (0, 4), (1, 4)])
        util.recolor(self, g, [(0, 1), (0, 4), (1, 4)], LIGHT_PINK)

        self.wait(LONG_DWELL_TIME)

        # Finish game and indicate positive triangle
        self.play(Create(plus_2))
        self.play(Create(plus_3))

        self.wait(SHORT_DWELL_TIME)
        util.bulk_indicate(self, g, [(0, 1), (0, 4), (1, 4)], run_time=LONG_ANIMATION_TIME)

        self.wait(SHORT_DWELL_TIME)

        # Deconstruct everything
        self.play(Uncreate(text_objects[2][0]), *[Uncreate(obj) for obj in [plus_1, plus_2, plus_3, minus_1]])
        self.play(Uncreate(g))

        self.wait(SHORT_DWELL_TIME)

    def test(self, text_objects):
        self.play(Create(text_objects[0][0]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]))
