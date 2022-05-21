from manim import *
from constants import *
from graphs.complete import CompleteGraph
import util


class IntroCycle(Scene):
    def construct(self):
        text = """This is a 3-cycle graph.
        It looks like a triangle.
        #
        In this game, the goal is to end
        with a positive triangle,
        #
        having an odd number of positive edges,
        and an even number of negative edges.
        #
        So, it can end with
        two minus signs,
        #
        or none.
        
        """

        g = Graph(CompleteGraph().generate_vertices(3),
                  CompleteGraph().generate_edges(3),
                  layout="kamada_kawai").shift(UP)

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

        text_objects = util.text_generator(text, DOWN)

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

        self.wait(LONG_DWELL_TIME)
