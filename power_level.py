from manim import *
from constants import *
from graphs.wheel import WheelGraph
import util


class PowerLevel(Scene):
    wheel = WheelGraph()

    def construct(self):
        text = """Here is a wheel graph,
        <span foreground="red">W<sub>4</sub></span>
        #
        Each vertex is a member of at least 
        1 triangle within the graph.
        #
        An edge is a member to as many triangles
        as its <gradient from="GREEN" to="ORANGE">power level.</gradient> 
        #
        For example, this bottom edge is a 
        member of one triangle,
        #
        but it is also a member of
        this triangle.
        #
        So, this is the <gradient from="GREEN" to="ORANGE">power level</gradient> of
        each edge in this graph. 
        """

        text_objects = util.text_generator(text, DOWN)

        g = Graph(self.wheel.generate_vertices(4),
                  self.wheel.generate_edges(4),
                  layout="planar").shift(UP)

        # Create PL labels (text with circle background)
        edge_labels = [MarkupText("2", font_size=22, color=RED) for _ in range(6)]
        edge_bg = [Circle(0.18, LIGHT_GRAY, fill_opacity=0.8) for _ in range(6)]

        for num, edge in enumerate(g.edges):
            edge_labels[num].move_to(g.edges[edge])
            edge_bg[num].move_to(g.edges[edge])

        # Create and introduce graph
        self.play(Create(g))
        util.bulk_play(self, Create(text_objects[0][0]), Create(text_objects[0][1]))

        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                  ReplacementTransform(text_objects[0][1], text_objects[1][1]))

        # Highlight all triangles
        util.bulk_indicate(self, g, [(0, 1), (0, 3), (1, 3)])
        self.wait(SHORT_DWELL_TIME)
        util.bulk_indicate(self, g, [(0, 2), (0, 3), (2, 3)])
        self.wait(SHORT_DWELL_TIME)
        util.bulk_indicate(self, g, [(1, 2), (1, 3), (2, 3)])
        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]),
                  ReplacementTransform(text_objects[1][1], text_objects[2][1]))

        self.wait(SHORT_DWELL_TIME)

        # Highlight one edge
        self.play(g.edges[(0, 1)].animate(run_time=ANIMATION_TIME).set_color(GREEN))

        # Cycle text
        self.play(ReplacementTransform(text_objects[2][0], text_objects[3][0]),
                  ReplacementTransform(text_objects[2][1], text_objects[3][1]))

        # Point out triangle
        util.bulk_indicate(self, g, [(0, 1), (0, 3), (1, 3)])

        # Cycle text
        self.play(ReplacementTransform(text_objects[3][0], text_objects[4][0]),
                  ReplacementTransform(text_objects[3][1], text_objects[4][1]))

        # Point out other triangle
        util.bulk_indicate(self, g, [(0, 1), (0, 2), (1, 2)])

        # Cycle text
        self.play(ReplacementTransform(text_objects[4][0], text_objects[5][0]),
                  ReplacementTransform(text_objects[4][1], text_objects[5][1]))

        # Show edge labels
        self.play(*[Create(bg) for bg in edge_bg])
        self.play(*[Write(label) for label in edge_labels])

        self.wait(SHORT_DWELL_TIME)

        # Uncreate everything
        util.bulk_play(self,
                       [Uncreate(text_objects[5][0]), Uncreate(text_objects[5][1])],
                       [Uncreate(bg) for bg in edge_bg] + [Uncreate(label) for label in edge_labels],
                       Uncreate(g))

        self.wait(SHORT_DWELL_TIME)
