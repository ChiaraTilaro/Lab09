import networkx as nx
from networkx.algorithms import threshold

from database.DAO import DAO


class Model:
    def __init__(self):
        self.edges = None
        self.nodes = None
        self.g = nx.Graph()
        self.idMap = {}

    def grafo(self, distanza_minima):
        self.g.clear()
        self.nodes = DAO.getTuttiAeroporti()
        self.fillIdMap()
        self.g.add_nodes_from(self.nodes)
        self.edges = DAO.getTutteRotte()

        for edge in self.edges:
            w = edge.avgDistance
            a1Object = self.idMap[edge.a1]
            a2Object = self.idMap[edge.a2]
            if w > threshold:
                self.g.add_edge(a1Object , a2Object , weight = w)

    def getNumEdges(self):
        return self.g.number_of_edges()

    def getNumNodes(self):
        return self.g.number_of_nodes()

    def getAllEdges(self):
        return self.g.edges

    def getAvgDist(self, v1, v2):
        data =  self._grafo.get_edge_data(v1, v2)
        return data["weight"]

    def fillIdMap(self):
        for n in self.nodes:
            self.idMap[n.ID] = n
