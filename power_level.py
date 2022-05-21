from manim import *
from constants import *
from graphs.wheel import WheelGraph
import util


class PowerLevel(Scene):
    def construct(self):
        text = """Here is a wheel graph,
        W<sub>4</sub>
        #
        Each vertex is a member of at least 
        1 triangle within the graph.
        #
        The number of triangles an edge is 
        a member of is its <gradient from="GREEN" to="ORANGE">power level.</gradient> 
        """

        # create the graph

        # highlight each triangle

        # just create the text

        # show example of an edge

        text_objects = util.text_generator(text, DOWN)

        # cycle through text objects for testing
        self.play(Create(text_objects[0][0]),
                    Create(text_objects[0][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                    ReplacementTransform(text_objects[0][1], text_objects[1][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]),
                    ReplacementTransform(text_objects[1][1], text_objects[2][1]))

        self.wait(SHORT_DWELL_TIME)