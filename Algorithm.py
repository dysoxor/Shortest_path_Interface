from FileHandler import FileHandler
from View import View


class Algorithm:

    def __init__(self, dataset):
        fh = FileHandler(dataset)
        self.E, self.edges, self.edge_index, self.nodes = fh.read()
        # E is total number of edges
        # edges is a list of tuples (source, destination, weight, color)
        # nodes is a dictionary that stores the index of each edges in the list above
        # nodes is a dictionary where we can get direct neighbors of each nodes and the color assigned to each node

        # if you want to solve before visualizing the process you can do it here, or you can solve during the
        # visualization in the update function

        # you can delete this it is for the example presented in the update function below
        self.color = ["blue", "red", "green", "m"]
        self.counter = 0

        self.view = View(self, label_edges=True, speed=20)

    def getEdges(self):
        return self.edges

    def setEdgeColor(self, src, dest, color):
        if (src, dest) in self.edge_index:
            index = self.edge_index[(src, dest)]
            self.edges[index] = self.edges[index][0], self.edges[index][1], self.edges[index][2], color
        elif (dest, src) in self.edge_index:
            index = self.edge_index[(dest, src)]
            self.edges[index] = self.edges[index][0], self.edges[index][1], self.edges[index][2], color

    def getNeighbors(self, v):
        return self.nodes[v]

    def update(self):
        """
        updated constantly during each refresh of the view
        :return: void
        """
        # example where one edge is changing color every tick
        self.setEdgeColor(1, 2, self.color[self.counter%4])
        self.counter += 1


algorithm = Algorithm("datasets/example")
