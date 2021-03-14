
class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    """
    Input file format:
        vertice_src vertice_dest weight
        ...
        node ID of the starting node = 0
        node ID of the destination node = 1
    """
    def read(self):
        E = 0
        edges = []
        edge_index = {}
        neighbors = {}
        with open(self.file_name, "r") as f:
            for line in f.readlines():
                element = line.split()
                v1 = int(element[0])
                v2 = int(element[1])
                w = int(element[2].rstrip())
                edges.append((v1, v2, w, "black"))
                edge_index[(v1, v2)] = E

                if v1 == 0:
                    neighbors.setdefault(v1, ([], "green"))[0].append(v2)
                elif v1 == 1:
                    neighbors.setdefault(v1, ([], "red"))[0].append(v2)
                else:
                    neighbors.setdefault(v1, ([], "grey"))[0].append(v2)

                if v2 == 0:
                    neighbors.setdefault(v2, ([], "green"))[0].append(v1)
                elif v2 == 1:
                    neighbors.setdefault(v2, ([], "red"))[0].append(v1)
                else:
                    neighbors.setdefault(v2, ([], "grey"))[0].append(v1)

                E += 1

        return E, edges, edge_index, neighbors
