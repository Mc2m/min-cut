
class Edge(object):
    
    def __init__(self):
        self.start = None
        self.end = None
        
    def setStart(self, node):
        self.start = node
        node.addEdge(self)
        
    def setEnd(self, node):
        self.end = node
        node.addEdge(self)
        
    def getStart(self):
        return self.start
        
    def getEnd(self):
        return self.end
    
    def __str__(self):
        return "Edge:" \
               " Start node: %s" \
               " End node: %s" % (str(self.start), str(self.end))
