
class Node(object):
    
    def __init__(self, nodeid):
        self.id = nodeid
        self.edges = []
        
    def addEdge(self, edge):
        self.edges.append(edge)
        
    def __str__(self):
        return "%d" % (self.id)
