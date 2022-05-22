from manim import *
from constants import *
from graphs.wheel import WheelGraph
import util


class WheelPlay(Scene):
    wheel = WheelGraph()

    def construct(self):
        text = f"""<span {DOUBLE_UNDERLINE}>Maximal</span> optimal play on <span {GRAPH_COLOR}>W<sub>7</sub></span>.
        #
        <span {SINGLE_UNDERLINE}>Minimal</span> optimal play on <span {GRAPH_COLOR}>W<sub>7</sub></span>
        """

        # Make text and graph
        text_objects = util.text_generator(text, DOWN * 2.2)

        g = Graph(self.wheel.generate_vertices(7),
                    self.wheel.generate_edges(7),
                    layout="kamada_kawai").shift(UP * 0.8).scale(1.5)

        # Make sign objects -- minus is intentionally used for contrast in signs
        minus_1 = SVGMobject(file_name="res/minus.svg").scale(MINUS_SCALE)
        minus_2, minus_3, minus_4, minus_5, minus_6, minus_7 = [minus_1.copy() for _ in range(6)]

        plus_1 = SVGMobject(file_name="res/plus.svg").scale(PLUS_SCALE)

        # Set positions
        minus_1.move_to(g.edges[(1, 2)])
        minus_2.move_to(g.edges[(2, 3)])
        minus_3.move_to(g.edges[(3, 4)])
        minus_4.move_to(g.edges[(4, 5)])
        minus_5.move_to(g.edges[(5, 6)])
        minus_6.move_to(g.edges[(1, 6)])
        minus_7.move_to(g.edges[(0, 1)])

        plus_1.move_to(g.edges[(0, 6)])

        # Create graph and label
        self.play(Create(g))
        self.play(Create(text_objects[0][0]))

        self.wait(SHORT_DWELL_TIME)

        # Highlight PL1 edges
        util.bulk_indicate(self, g, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 6)])

        self.wait(SHORT_DWELL_TIME)

        # Create PL1 signs
        util.bulk_play(self, *[Create(obj, run_time=BRIEF_ANIMATION_TIME) for obj in [minus_1, minus_2, minus_3, minus_4, minus_5, minus_6]])

        self.wait(SHORT_DWELL_TIME)

        # Last two moves
        self.play(Create(minus_7))
        self.play(Create(plus_1))

        # Indicate positive triangle
        util.bulk_indicate(self, g, [(0, 1), (0, 6), (1, 6)], run_time=LONG_ANIMATION_TIME)

        self.wait(LONG_DWELL_TIME)

        # Fade all signs out
        self.play(*[FadeOut(obj, run_time=SHORT_ANIMATION_TIME) for obj in [minus_1, minus_2, minus_3, minus_4, minus_5, minus_6, minus_7, plus_1]])

        self.wait(SHORT_DWELL_TIME)

        # Cycle text and shift positions
        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]))

        minus_1.move_to(g.edges[(0, 1)])
        minus_2.move_to(g.edges[(0, 3)])
        minus_3.move_to(g.edges[(0, 5)])
        minus_4.move_to(g.edges[(0, 6)])
        plus_1.move_to(g.edges[(5, 6)])

        # Highlight PL2 edges
        util.bulk_indicate(self, g, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])

        self.wait(SHORT_DWELL_TIME)

        # Play PL2 signs
        util.bulk_play(self, *[Create(obj, run_time=BRIEF_ANIMATION_TIME) for obj in [minus_1, minus_2, minus_3]])

        self.wait(SHORT_DWELL_TIME)

        # Last two moves
        self.play(Create(plus_1))
        self.play(Create(minus_4))

        # Indicate positive triangle
        util.bulk_indicate(self, g, [(0, 5), (0, 6), (5, 6)], run_time=LONG_ANIMATION_TIME)

        self.wait(LONG_DWELL_TIME)

        # Deconstruct everything
        self.play(*[Uncreate(obj, run_time=SHORT_ANIMATION_TIME) for obj in [minus_1, minus_2, minus_3, minus_4, plus_1]])
        self.play(Uncreate(g), Uncreate(text_objects[1][0]))

        self.wait(SHORT_DWELL_TIME)


        
    def test(self, text_objects):
        self.play(Create(text_objects[0][0]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]))

        self.wait(SHORT_DWELL_TIME)