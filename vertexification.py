from manim import *
from constants import *
from graphs.wheel import WheelGraph
from graphs.vertexify import Vertexify
import util


class Vertexification(Scene):
    wheel = WheelGraph()
    vertexify = Vertexify()

    def construct(self):
        text = f"""This is a <gradient {VERTEXIFIED_GRADIENT} offset=",1">vertexified</gradient> graph of a wheel graph,
        <span {GRAPH_COLOR}>X(W)<sub>7</sub></span>
        #
        <gradient {VERTEXIFIED_GRADIENT} offset=",1">Vertexified</gradient> graphs have vertices made from
        the edges of the <span {SINGLE_UNDERLINE}>original graph</span>, and
        #
        edges formed between <gradient {MEMBERS_GRADIENT}>members</gradient> of identical
        triangles in the <span {SINGLE_UNDERLINE}>original</span> graph.
        #
        <span {GRAPH_COLOR}>X(W)<sub>7</sub></span> is the <span {SINGLE_UNDERLINE}>original</span> graph,
        and is the source of vertices.
        # 
        These edges are <gradient {MEMBERS_GRADIENT}>members</gradient> of the same 
        triangle in the <span {SINGLE_UNDERLINE}>original</span> graph, 
        #
        so an edge is drawn between them
        in the <gradient {VERTEXIFIED_GRADIENT} offset=",1">vertexified</gradient> graph.
        # 
        Repeating this process, 
        a <gradient {VERTEXIFIED_GRADIENT} offset=",1">vertexification</gradient> is created.
        """

        text_objects = util.text_generator(text, DOWN * 1.5)

        g = Graph(self.wheel.generate_vertices(7),
                  self.wheel.generate_edges(7),
                  layout=W7_LAYOUT).shift(UP + LEFT * 3).scale(1.2)

        xg = Graph(self.vertexify.generate_vertices(g.edges),
                   self.vertexify.generate_edges(g.edges),
                   layout=XW7_LAYOUT).shift(UP).scale(1.2)

        # Make the vertexified graph and text
        self.play(Create(xg))
        util.bulk_play(self, Create(text_objects[0][0]), Create(text_objects[0][1]))

        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                  ReplacementTransform(text_objects[0][1], text_objects[1][1]))

        self.wait(SHORT_DWELL_TIME)

        # Cycle text and reposition graph
        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]),
                  ReplacementTransform(text_objects[1][1], text_objects[2][1]),
                  xg.animate(run_time=ANIMATION_TIME).shift(RIGHT * 3))

        self.wait(SHORT_DWELL_TIME)

        # Cycle text and move in graph
        self.play(ReplacementTransform(text_objects[2][0], text_objects[3][0]),
                  ReplacementTransform(text_objects[2][1], text_objects[3][1]),
                  Create(g))

        self.wait(SHORT_DWELL_TIME)

        # Indicate vertices and edges
        util.bulk_indicate(self, g, g.edges, run_time=SHORT_ANIMATION_TIME, include_vertices=False, rate_func=rate_functions.linear)
        util.bulk_indicate_vertices(self, xg, xg.vertices, run_time=LONG_ANIMATION_TIME, rate_func=rate_functions.there_and_back_with_pause)

        self.wait(SHORT_DWELL_TIME)

        self.play(g.animate(run_time=BRIEF_ANIMATION_TIME).set_color(WHITE))

        # Cycle text
        self.play(ReplacementTransform(text_objects[3][0], text_objects[4][0]),
                  ReplacementTransform(text_objects[3][1], text_objects[4][1]))

        # Show edge and pairings
        util.bulk_indicate(self, g, [(0, 3), (2, 3)], include_vertices=False, run_time=SHORT_ANIMATION_TIME, rate_func=rate_functions.linear)
        util.bulk_indicate_vertices(self, xg, [3, 9], run_time=LONG_ANIMATION_TIME, rate_func=rate_functions.there_and_back_with_pause)

        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[4][0], text_objects[5][0]),
                  ReplacementTransform(text_objects[4][1], text_objects[5][1]))

        # Reset edges, but indicate the resultant edge
        self.play(g.animate(run_time=BRIEF_ANIMATION_TIME).set_color(WHITE))
        util.bulk_indicate(self, xg, [(3, 9)], color=PURE_BLUE, run_time=LONG_ANIMATION_TIME, rate_func=rate_functions.there_and_back_with_pause)
        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[5][0], text_objects[6][0]),
                  ReplacementTransform(text_objects[5][1], text_objects[6][1]))

        self.wait(SHORT_DWELL_TIME)

        # Deconstruct everything
        self.play(Uncreate(text_objects[6][0]), Uncreate(text_objects[6][1]))
        self.play(Uncreate(g), Uncreate(xg))

        self.wait(SHORT_DWELL_TIME)
