from manim import *
from util import *


class Vertexify(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        w = int(input())
        test_edges = Wheel.generate_edges(w)

        # graph layout is finnicky
        graph = Graph(Vertexify.generate_vertices(test_edges),
                Vertexify.generate_edges(test_edges),
                layout="kamada_kawai").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

