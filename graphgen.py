import random
import edge
import node

def linkEdges(edge, nodes):
    node = nodes[random.randint(0,len(nodes)-1)]
        
    if not (edge.end or edge.start):
        edge.setEnd(node) if random.randint(0,1) == 1 else edge.setStart(node)
        return True
    elif edge.start != node and edge.start:
        for nedge in node.edges:
            if nedge.start == edge.start or nedge.end == edge.start:
                return False
                
        edge.setEnd(node)
        return True
    elif edge.end and edge.end != node:
        for nedge in node.edges:
            if nedge.start == edge.end or nedge.end == edge.end:
                return False
        
        edge.setStart(node)
        return True
    
    return False


def manualGen(nodes,edges):
    answer = raw_input("how many nodes do you want ? ")
    try:
        answer = int(answer)
    except:
        print("Nodes couldn't be created. Wrong input...")
        
    assert(answer >= 4)
    for i in range(0,int(answer)):
        nodes.append(node.Node(i+1))
        
    print("Node list: %s" % ([str(curnode) for curnode in nodes]))
    
    answer = raw_input("Set an edge by providing two integers\nseparated by spaces then pressing Enter\nTo cancel, write anything else\nExample: \"1 2\"?\n")

    try:
        while True:
            split = answer.split(' ')
            start,end = int(split[0]),int(split[1])
            
            if (start > 0 and start-1 < len(nodes) and end > 0 and end-1 < len(nodes)):
                curedge = edge.Edge()
                edges.append(curedge)
                curedge.setStart(nodes[start-1])
                curedge.setEnd(nodes[end-1])
            else:
                print("Wrong nodes, Retry")
            
            answer = raw_input("Add an edge or exit by writing anything else:\n")
    except:
        pass
        
def autoGen(nodes,edges):
    for i in range(1,random.randint(10,100)):
        
        curedge = edge.Edge()
        edges.append(curedge)
        
        if len(edges) == 1:
            curnode = node.Node(len(nodes)+1)
            nodes.append(curnode)
            curedge.setStart(curnode)
            
            curnode = node.Node(len(nodes)+1)
            nodes.append(curnode)
            curedge.setEnd(curnode)
        else:
            linkEdges(curedge,nodes)
            
            if not(curedge.start or curedge.end):
                print("fail")
                
            linked = False
        
            while not linked:
                if random.randint(0,1) == 1:
                    linked = linkEdges(curedge,nodes)
                else:
                    curnode = node.Node(len(nodes)+1)
                    nodes.append(curnode)
                    curedge.setEnd(curnode) if curedge.start else curedge.setStart(curnode)
                    linked = True
                
            if not curedge.start or not curedge.end:
                print("fail")
                
def graphCheck(graph):
    edges = []
    nodes = []
    for curedge in graph[1]:
        if not isinstance(curedge.start,node.Node) or not isinstance(curedge.end,node.Node) or curedge.end == curedge.start:
            print("Removing edge %s" % (str(curedge)))
        else:
            edges.append(curedge)
            
    for curnode in graph[0]:
        if len(curnode.edges) == 0:
            print("Removing node %s" % (str(curnode)))
        else:
            nodes.append(curnode)
            
    graph = (nodes,edges)

def graphGen():
    nodes = []
    edges = []
    graph = (nodes,edges)
    
    answer = raw_input("do you want to set a graph manually (Y/n) ? ")
    if answer == 'Y' or answer == 'y':
        manualGen(nodes,edges)
        graphCheck(graph)
    else:
        autoGen(nodes,edges)

    return graph
    