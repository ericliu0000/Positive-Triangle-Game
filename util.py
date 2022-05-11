import itertools

class Complex:
    def generate_vertices(n):
        return [i for i in range(n)]

    def generate_edges(n):
        edges = []

        # Draw edge between evey vertex
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    continue
                edges.append((i, j))

        return edges


class Wheel:
    def generate_vertices(n):
        return [i for i in range(n)]

    def generate_edges(n):
        edges = [(1, n - 1)]

        # Generate outer cycles
        for i in range(1, n - 1):
            edges.append((i, i + 1))

        # Generate "spokes"
        for i in range(1, n):
            edges.append((0, i))

        return edges


class TriangleLadder:
    def generate_vertices(n):
        if (n % 2): return
        return [i + 1 for i in range(n)]

    def generate_edges(n: int):
        if (n % 2): return
        edges = [(1, n)]

        # Generate outer cycle
        for i in range(1, n):
            edges.append((i, i + 1))

        # Generate vertical spokes
        if n >= 6:
            for i in range(2, int(n / 2), 2):
                edges.append((i, n - i + 1))

        # Generate diagonals
        if n >= 4:
            for i in range(1, int(n / 2)):
                edges.append((i, n - i))
        
        print(edges)
        return edges

class StrangeDual:
    def generate_vertices(edges):
        return [i + 1 for i in range(len(edges))]

    def generate_edges(edges):
        ordered_edges = {}

        for count, edge in enumerate(edges):
            ordered_edges[count + 1] = edge

        print(ordered_edges)

        possibilities = itertools.combinations(range(1, len(edges) + 1), 2)

        for pair in possibilities:
            edge_pack = [ordered_edges[pair[0]][0], ordered_edges[pair[1]][0], ordered_edges[pair[0]][1], ordered_edges[pair[1]][1]]
            print(edge_pack)
            print(set(edge_pack))
            print(list(set(edge_pack)) != edge_pack)
            print("\n")
            # Assuming there no self edges, 
            # check for duplicates in edge pack
            # if set(edge_pack) != edge_pack:


if __name__ == "__main__":

    test_graph = Wheel.generate_edges(4)

    # print(StrangeDual.generate_vertices(test_graph))
    # print("\n\n\n")
    print(StrangeDual.generate_edges(test_graph))
    


    x = itertools.combinations(range(1, 7), 2)
    for i in x:
        print(i)
