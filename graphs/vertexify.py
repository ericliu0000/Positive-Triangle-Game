from manim import *
from sys import argv
import itertools
import complete, wheel, triangleladder


class Vertexify(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        try:
            w = int(argv[-1])
        except ValueError as e:
            w = 4
            print("last argument specifies number of vertices")

        test_edges = complete.CompleteGraph().generate_edges(w)

        graph = Graph(self.generate_vertices(test_edges),
                      self.generate_edges(test_edges),
                      layout="spring").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

    def generate_vertices(self, edges):
        return [i + 1 for i in range(len(edges))]

    def generate_edges(self, edges):
        output = []
        ordered_edges = {}

        for count, edge in enumerate(edges):
            ordered_edges[count + 1] = edge

        # Iterate through every edge possibility
        for pair in itertools.combinations(range(1, len(edges) + 1), 2):
            e1 = list(ordered_edges[pair[0]])
            e2 = list(ordered_edges[pair[1]])

            edge_pack = [ordered_edges[pair[0]][0], ordered_edges[pair[1]]
                         [0], ordered_edges[pair[0]][1], ordered_edges[pair[1]][1]]

            if len(edge_pack) != len(set(edge_pack)):
                common = set(e1).intersection(e2).pop()

                # Remove the common vertex
                e1.remove(common)
                e2.remove(common)

                # Get expected edge to complete face
                missing = (e1[0], e2[0])

                if missing in edges or missing[::-1] in edges:
                    output.append((pair[0], pair[1]))

        return output
