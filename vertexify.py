from manim import *
from sys import argv
import wheel


class Vertexify(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        try:
            w = int(argv[-1])
        except ValueError as e:
            w = 4
            print("last argument specifies number of vertices")

        test_edges = wheel.WheelGraph().generate_edges(w)

        # graph layout is finnicky
        graph = Graph(Vertexify.generate_vertices(test_edges),
                      Vertexify.generate_edges(test_edges),
                      layout="kamada_kawai").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))
