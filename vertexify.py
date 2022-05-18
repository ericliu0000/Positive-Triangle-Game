from manim import *
from sys import argv
import itertools
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
        graph = Graph(self.generate_vertices(test_edges),
                      self.generate_edges(test_edges),
                      layout="kamada_kawai").scale(1.5)
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

        print(ordered_edges)

        possibilities = itertools.combinations(range(1, len(edges) + 1), 2)

        for pair in possibilities:
            e1 = list(ordered_edges[pair[0]])
            e2 = list(ordered_edges[pair[1]])

            edge_pack = [ordered_edges[pair[0]][0], ordered_edges[pair[1]]
                         [0], ordered_edges[pair[0]][1], ordered_edges[pair[1]][1]]

            if len(edge_pack) != len(set(edge_pack)):
                common = set(e1).intersection(e2).pop()
                print(f"1: {common}")
                print(f"2: {e1} {e2}")

                # Remove the common vertex
                e1.remove(common)
                e2.remove(common)

                print(f"3: {e1} {e2}")

                # Get expected edge to complete face
                missing = (e1[0], e2[0])
                # missing2 = (e2[0], e1[0])

                print(f"4: {missing in edges or missing[::-1] in edges}\n")

                if missing in edges or missing[::-1] in edges:
                    output.append((pair[0], pair[1]))

                # if (e1[0], e2[0])

            # if any of the edges are the same
            # if e1[0] == e2[0] or e1[0] == e2[1] or e1[1] == e2[0] or e1[1] == e2[1]:
            #     output.append((pair[0], pair[1]))
            # edge_pack = [ordered_edges[pair[0]][0], ordered_edges[pair[1]][0], ordered_edges[pair[0]][1], ordered_edges[pair[1]][1]]

            # # check for duplicates in edge pack
            # if len(edge_pack) != len(set(edge_pack)):
            #     output.append((pair[0], pair[1]))

        print(f"output: {output}")

        return output
