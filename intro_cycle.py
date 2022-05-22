from manim import *
from constants import *
from graphs.complete import CompleteGraph
import util


class IntroCycle(Scene):
    complete = CompleteGraph()

    def construct(self):
        text = f"""This is a 3-cycle graph <span {GRAPH_COLOR}>C<sub>3</sub></span>
        It looks like a triangle.
        #
        In this game, the goal is to end
        with a <span {POSITIVE_TRIANGLE_COLOR}>positive triangle</span>,
        #
        having an <span {SINGLE_UNDERLINE}>odd number</span> of positive edges,
        and an <span {DOUBLE_UNDERLINE}>even number</span> of negative edges.
        #
        So, the game ends with
        two minus signs,
        #
        or no minus signs.
        
        """

        text_objects = util.text_generator(text, DOWN)

        # Make graph
        g = Graph(self.complete.generate_vertices(3),
                  self.complete.generate_edges(3),
                  layout="kamada_kawai").shift(UP)

        # Make signs
        plus_1 = SVGMobject(file_name="res/plus.svg").scale(PLUS_SCALE)
        plus_2 = plus_1.copy()
        plus_3 = plus_1.copy()
        minus_1 = SVGMobject(file_name="res/minus.svg").scale(MINUS_SCALE)
        minus_2 = minus_1.copy()

        # Set positions
        plus_1.move_to((-6, 3, 0))
        plus_2.move_to(g.edges[(0, 2)])
        plus_3.move_to(g.edges[(0, 1)])
        minus_1.next_to(plus_1, RIGHT)
        minus_2.move_to(g.edges[(0, 1)])

        # Create graph
        self.play(Create(g))

        # Create text, round 1
        self.play(Create(text_objects[0][0]),
                  Create(text_objects[0][1]))

        self.wait(SHORT_DWELL_TIME)

        # Swap text
        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                  ReplacementTransform(text_objects[0][1], text_objects[1][1]))

        self.wait(SHORT_DWELL_TIME)

        # Swap text and add signs
        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]),
                  ReplacementTransform(text_objects[1][1], text_objects[2][1]),
                  Create(plus_1),
                  Create(minus_1))

        self.wait(SHORT_DWELL_TIME)

        # Swap text
        self.play(ReplacementTransform(text_objects[2][0], text_objects[3][0]),
                  ReplacementTransform(text_objects[2][1], text_objects[3][1]))

        # Move signs into position
        util.bulk_play(self,
                       plus_1.animate(run_time=ANIMATION_TIME).move_to(g.edges[(1, 2)]),
                       minus_1.animate(run_time=ANIMATION_TIME).move_to(g.edges[(0, 2)]),
                       Create(minus_2))

        # Wipe all signs
        self.play(FadeOut(plus_1), FadeOut(minus_1), FadeOut(minus_2))

        # Swap text and cycle signs into last config
        self.play(ReplacementTransform(text_objects[3][0], text_objects[4][0]),
                  ReplacementTransform(text_objects[3][1], text_objects[4][1]))

        # Show three signs
        plus_1.move_to(g.edges[(1, 2)])
        util.bulk_play(self,
                       Create(plus_1),
                       Create(plus_2),
                       Create(plus_3))

        self.wait(SHORT_DWELL_TIME)

        # Uncreate everything
        util.bulk_play(self,
                       [Uncreate(plus_1), Uncreate(plus_2), Uncreate(plus_3)],
                       [Uncreate(text_objects[4][0]), Uncreate(text_objects[4][1])],
                       Uncreate(g))

        self.wait(SHORT_DWELL_TIME)
