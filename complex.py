from manim import *
from util import *


class ComplexGraph(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        w = int(input())

        graph = Graph(Complex.generate_vertices(w),
                Complex.generate_edges(w),
                layout="kamada_kawai").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

