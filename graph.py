class Node:
    def get_id(self):
        """
        Returns a unique identifier for the node (for example, the name, the hash value of the contents, etc.), used to compare two nodes for equality.
        """
        return ""
    def get_neighbors(self):
        """
        Returns all neighbors of a node, and how to reach them. The result is a list Edge objects, each of which contains 3 attributes: target, cost and name, 
        where target is a Node object, cost is a numeric value representing the distance between the two nodes, and name is a string representing the path taken to the neighbor.
        """
        return []
    def __eq__(self, other):
        return self.get_id() == other.get_id()
        
class Edge:
    """
    Abstraction of a graph edge. Has a target (Node that the edge leads to), a cost (numeric) and a name (string), which can be used to print the edge.
    """
    def __init__(self, target, cost, name):
        self.target = target 
        self.cost = cost
        self.name = name

class GeomNode(Node):
    """
    Representation of a finite graph in which all nodes are kept in memory at all times, and stored in the node's neighbors field.
    """
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def get_neighbors(self):
        return self.neighbors
    def get_id(self):
        return self.name
        
class InfNode(Node):
    """
    Infinite graph, in which every node represents an integer, and neighbors are generated on demand. Note that Nodes are not cached, i.e. if you
    request the neighbors of node 1, and the neighbors of node 3, both will contain the node 2, but they will be using two distinct objects. 
    """
    def __init__(self, nr):
        self.nr = nr
    def get_neighbors(self):
        result = [Edge(InfNode(self.nr-1),1,("%d - -1 - %d"%(self.nr,self.nr-1))), Edge(InfNode(self.nr+1),1,("%d - +1 - %d"%(self.nr,self.nr+1))), Edge(InfNode(self.nr*2),1,("%d - *2 - %d"%(self.nr,self.nr*2)))]
        if self.nr%2 == 0:
            result.append(Edge(InfNode(self.nr//2),1,("%d - /2 - %d"%(self.nr,self.nr//2))))
        return result
    def get_id(self):
        return self.nr


def make_geom_graph(nodes, edges):
    """
    Given a list of nodes and edges (with distances), creates a dictionary of Node objects 
    representing the graph. Note that the resulting graph is directed, but each edge will be 
    replaced with *two* directed edges (to and from).
    """
    result = {}
    for c in nodes:
        result[c] = GeomNode(c)
    for (a,b,d) in edges:
        result[a].neighbors.append(Edge(result[b], d, "%s - %s"%(a,b)))
        result[b].neighbors.append(Edge(result[a], d, "%s - %s"%(b,a)))
    return result
    
Austria = make_geom_graph(
    ["Graz", "Vienna", "Salzburg", "Innsbruck", "Munich", "Bregenz", "Linz", "Eisenstadt", "Klagenfurt", "Lienz", "Bruck"],
    [("Graz", "Bruck", 55.0),
     ("Graz", "Klagenfurt", 136.0),
     ("Graz", "Vienna", 200.0),
     ("Graz", "Eisenstadt", 173.0),
     ("Bruck", "Klagenfurt", 152.0),
     ("Bruck", "Salzburg", 215.0),
     ("Bruck", "Linz", 195.0),
     ("Bruck", "Vienna", 150.0),
     ("Vienna", "Eisenstadt", 60.0),
     ("Vienna", "Linz", 184.0),
     ("Linz", "Salzburg", 123.0),
     ("Salzburg", "Munich", 145.0),
     ("Salzburg", "Klagenfurt", 223.0),
     ("Klagenfurt", "Lienz", 145.0),
     ("Lienz", "Innsbruck", 180.0),
     ("Munich", "Innsbruck", 151.0),
     ("Munich", "Bregenz", 180.0),
     ("Innsbruck", "Bregenz", 190.0)])
     
AustriaHeuristic = { 
   "Graz":       {"Graz": 0.0,   "Vienna": 180.0, "Eisenstadt": 150.0, "Bruck": 50.0,  "Linz": 225.0, "Salzburg": 250.0, "Klagenfurt": 125.0, "Lienz": 270.0, "Innsbruck": 435.0, "Munich": 375.0, "Bregenz": 450.0},
   "Vienna":     {"Graz": 180.0, "Vienna": 0.0,   "Eisenstadt": 50.0,  "Bruck": 126.0, "Linz": 175.0, "Salzburg": 285.0, "Klagenfurt": 295.0, "Lienz": 400.0, "Innsbruck": 525.0, "Munich": 407.0, "Bregenz": 593.0},
   "Eisenstadt": {"Graz": 150.0, "Vienna": 50.0,  "Eisenstadt": 0.0,   "Bruck": 171.0, "Linz": 221.0, "Salzburg": 328.0, "Klagenfurt": 335.0, "Lienz": 437.0, "Innsbruck": 569.0, "Munich": 446.0, "Bregenz": 630.0},
   "Bruck":      {"Graz": 50.0,  "Vienna": 126.0, "Eisenstadt": 171.0, "Bruck": 0.0,   "Linz": 175.0, "Salzburg": 201.0, "Klagenfurt": 146.0, "Lienz": 287.0, "Innsbruck": 479.0, "Munich": 339.0, "Bregenz": 521.0},
   "Linz":       {"Graz": 225.0, "Vienna": 175.0, "Eisenstadt": 221.0, "Bruck": 175.0, "Linz": 0.0,   "Salzburg": 117.0, "Klagenfurt": 311.0, "Lienz": 443.0, "Innsbruck": 378.0, "Munich": 265.0, "Bregenz": 456.0},
   "Salzburg":   {"Graz": 250.0, "Vienna": 285.0, "Eisenstadt": 328.0, "Bruck": 201.0, "Linz": 117.0, "Salzburg": 0.0,   "Klagenfurt": 201.0, "Lienz": 321.0, "Innsbruck": 265.0, "Munich": 132.0, "Bregenz": 301.0},
   "Klagenfurt": {"Graz": 125.0, "Vienna": 295.0, "Eisenstadt": 335.0, "Bruck": 146.0, "Linz": 311.0, "Salzburg": 201.0, "Klagenfurt": 0.0,   "Lienz": 132.0, "Innsbruck": 301.0, "Munich": 443.0, "Bregenz": 465.0},
   "Lienz":      {"Graz": 270.0, "Vienna": 400.0, "Eisenstadt": 437.0, "Bruck": 287.0, "Linz": 443.0, "Salzburg": 321.0, "Klagenfurt": 132.0, "Lienz": 0.0,   "Innsbruck": 157.0, "Munich": 298.0, "Bregenz": 332.0},
   "Innsbruck":  {"Graz": 435.0, "Vienna": 525.0, "Eisenstadt": 569.0, "Bruck": 479.0, "Linz": 378.0, "Salzburg": 265.0, "Klagenfurt": 301.0, "Lienz": 157.0, "Innsbruck": 0.0,   "Munich": 143.0, "Bregenz": 187.0},
   "Munich":     {"Graz": 375.0, "Vienna": 407.0, "Eisenstadt": 446.0, "Bruck": 339.0, "Linz": 265.0, "Salzburg": 132.0, "Klagenfurt": 443.0, "Lienz": 298.0, "Innsbruck": 143.0, "Munich": 0.0,   "Bregenz": 165.0},
   "Bregenz":    {"Graz": 450.0, "Vienna": 593.0, "Eisenstadt": 630.0, "Bruck": 521.0, "Linz": 456.0, "Salzburg": 301.0, "Klagenfurt": 465.0, "Lienz": 332.0, "Innsbruck": 187.0, "Munich": 165.0, "Bregenz": 0.0}}

China=make_geom_graph(
    ["Beijing","Hainan","Changsha","Wuhan","Guangzhou","Hubei","Xiamen","Guangxi","Hunan","Shanghai"],
    [("Beijing","Changsha",50.0),
     ("Beijing","Hainan",70.0),
     ("Changsha","Guangzhou",105.0),
     ("Changsha","Wuhan",100.0),
     ("Hainan","Guangzhou",80.0),
     ("Hainan","Xiamen",120.0),
     ("Guangzhou","Hubei",40.0),
     ("Guangzhou","Xiamen",140.0),
     ("Wuhan","Shanghai",200.0),
     ("Wuhan","Hubei",45.0),
     ("Hubei","Xiamen",80.0),
     ("Hubei","Hunan",175.0),
     ("Xiamen","Guangxi",200.0),
     ("Guangxi","Hunan",100.0),
     ("Hunan","Shanghai",125.0)])

ChinaHeruistic={
"Beijing":  {"Beijing":0.0, "Hainan": 60.0, "Changsha":40.0, "Wuhan": 130.0,"Guangzhou":70.0, "Hubei":130.0,"Xiamen": 140.0,"Guangxi":450.0,"Hunan": 420.0, "Shanghai":440.0},
"Hainan":   {"Beijing":60.0, "Hainan": 0.0, "Changsha":100.0, "Wuhan": 160.0,"Guangzhou":50.0, "Hubei":110.0,"Xiamen": 120.0,"Guangxi":350.0,"Hunan": 320.0, "Shanghai":340.0},
"Changsha": {"Beijing":40.0, "Hainan": 90.0, "Changsha":0.0, "Wuhan": 100.0,"Guangzhou":40.0, "Hubei":100.0,"Xiamen": 130.0,"Guangxi":400.0,"Hunan": 370.0, "Shanghai":320.0},
"Wuhan":    {"Beijing":120.0, "Hainan": 110.0, "Changsha":100.0, "Wuhan": 0.0,"Guangzhou":40.0, "Hubei":45.0,"Xiamen": 100.0,"Guangxi":280.0,"Hunan": 250.0, "Shanghai":200.0},
"Guangzhou":{"Beijing":70.0, "Hainan": 80.0, "Changsha":40.0, "Wuhan": 40.0,"Guangzhou":0.0, "Hubei":40.0,"Xiamen": 90.0,"Guangxi":220.0,"Hunan": 250.0, "Shanghai":280.0},
"Hubei":    {"Beijing":120.0, "Hainan": 110.0, "Changsha":100.0, "Wuhan": 45.0,"Guangzhou":40.0, "Hubei":0.0,"Xiamen": 80.0,"Guangxi":125.0,"Hunan": 100.0, "Shanghai":150.0},
"Xiamen":   {"Beijing":140.0, "Hainan": 120.0, "Changsha":130.0, "Wuhan": 100.0,"Guangzhou":90.0, "Hubei":80.0,"Xiamen": 0.0,"Guangxi":150.0,"Hunan": 200.0, "Shanghai":250.0},
"Guangxi":  {"Beijing":450.0, "Hainan": 35.0, "Changsha":400.0, "Wuhan": 280.0,"Guangzhou":220.0, "Hubei":125.0,"Xiamen": 120.0,"Guangxi":0.0,"Hunan": 100.0, "Shanghai":200.0},
"Hunan":    {"Beijing":420.0, "Hainan": 320.0, "Changsha":370.0, "Wuhan": 250.0,"Guangzhou":250.0, "Hubei":125.0,"Xiamen": 200.0,"Guangxi":100.0,"Hunan": 0.0, "Shanghai":100.0},
"Shanghai": {"Beijing":440.0, "Hainan": 340.0, "Changsha":320.0, "Wuhan": 200.0,"Guangzhou":280.0, "Hubei":150.0,"Xiamen": 250.0,"Guangxi":200.0,"Hunan": 100.0, "Shanghai":0.0}

}


