class Complex:
    def generate_vertices(self, n):
        return [i for i in range(n)]

    def generate_edges(self, n):
        edges = []

        # Draw edge between evey vertex
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    continue
                edges.append((i, j))

        return edges


class Wheel:
    def generate_vertices(self, n):
        return [i for i in range(n)]

    def generate_edges(self, n):
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
    def generate_vertices(self, edges):
        return [i for i in range(len(edges))]

    def generate_edges(self, edges):
        pass


