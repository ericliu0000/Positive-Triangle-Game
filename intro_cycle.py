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
        with a positive triangle.
        #
        So, the game can end in these 
        configurations after 3 moves:
        #
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
        plus_2.next_to(g.edges[(0, 2)], DOWN)
        plus_3.next_to(g.edges[(0, 1)], UP)
        minus_1.next_to(plus_1, RIGHT)
        minus_2.next_to(g.edges[(0, 1)], UP)

        text_objects = util.text_generator(text, DOWN)

        # Create graph
        self.play(Create(g))

        # Create text, round 1
        self.play(Create(text_objects[0][0]))
        self.play(Create(text_objects[0][1]))

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

        # Swap text and move signs into position
        self.play(ReplacementTransform(text_objects[2][0], text_objects[3][0]),
                    ReplacementTransform(text_objects[2][1], text_objects[3][1]),
                    plus_1.animate(run_time=ANIMATION_TIME).next_to(g.edges[(1, 2)], LEFT * 1.5),
                    minus_1.animate(run_time=ANIMATION_TIME).next_to(g.edges[(0, 2)], DOWN),
                    Create(minus_2))

        self.wait(SHORT_DWELL_TIME)

        # Swap text and cycle signs into last config
        self.play(ReplacementTransform(text_objects[3][0], text_objects[4][0]),
                    ReplacementTransform(text_objects[3][1], text_objects[4][1]),
                    ReplacementTransform(minus_1, plus_2),
                    ReplacementTransform(minus_2, plus_3))

        self.wait(LONG_DWELL_TIME)


