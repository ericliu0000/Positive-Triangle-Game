import itertools
import wheel


class Vertexify:
    def generate_vertices(edges):
        return [i + 1 for i in range(len(edges))]

    def generate_edges(edges):
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
                print(common)
                print(e1, e2)
                e1.remove(common)
                e2.remove(common)
                print(e1, e2, "\n")

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


if __name__ == "__main__":

    test_graph = wheel.WheelGraph().generate_edges(4)

    # print(StrangeDual.generate_vertices(test_graph))
    # print("\n\n\n")
    print(Vertexify.generate_edges(test_graph))

    # x = itertools.combinations(range(1, 7), 2)
    # for i in x:
    #     print(i)

    # adjacency in the wheel graph: reject if there is no such edge between two edges that share a vertex but for which there is no edge between the non shared edges