from manim import *
from constants import *
from graphs.complete import CompleteGraph
import util


class IntroCycle(Scene):
    def construct(self):
        text = """This is 3-cycle graph.
        It looks like a triangle.
        #
        In this game, the goal is to end
        with one triangle with 0 or 2 (-) marks.
        """

        g = Graph(CompleteGraph().generate_vertices(3),
                  CompleteGraph().generate_edges(3),
                  layout="kamada_kawai").shift(UP)

        text_objects = util.text_generator(text, DOWN)

        print(text_objects)

        self.play(Create(g))

        self.play(Create(text_objects[0][0]))
        self.play(Create(text_objects[0][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                  ReplacementTransform(text_objects[0][1], text_objects[1][1]))
        
        self.wait(LONG_DWELL_TIME)


