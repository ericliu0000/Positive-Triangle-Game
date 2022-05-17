from multiprocessing.sharedctypes import Value
from manim import *
from util import *
from sys import argv


class Ladder(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        try: 
            w = int(argv[-1])
        except ValueError as e:
            w = 4
            print("last argument specifies number of vertices")


        # TODO: layout is ugly. please fix
        graph = Graph(TriangleLadder.generate_vertices(w),
                TriangleLadder.generate_edges(w),
                layout="spring").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

