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
