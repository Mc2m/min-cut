import random
import copy
from graphgen import graphGen
import math

def contract(graph,mergenode,dropnode):
    for edge in dropnode.edges:
        #edge between mergenode and dropnode means drop edge
        if edge.start == mergenode or edge.end == mergenode:
            mergenode.edges.remove(edge)
            graph[1].remove(edge)
        elif edge.start == dropnode:
            edge.setStart(mergenode)
        else:
            edge.setEnd(mergenode)
    graph[0].remove(dropnode)
    
def randomMinCut(graph):
    iterations = 0
    while len(graph[0]) > 2:
        iterations += 1
        #print("Graph")
        #print("Nodes : %s" % ([str(node) for node in graph[0]]))
        #print("Edges : %s" % ([str(edge) for edge in graph[1]]))
        
        #select edge
        edge = graph[1][random.randint(0,len(graph[1])-1)]
        
        #contract
        if random.randint(0,1) == 1:
            contract(graph, edge.start, edge.end)
        else:
            contract(graph, edge.end, edge.start)
            
    return iterations

def main():
    random.seed(None)
    
    ograph = graphGen()
    
    #print("Original Graph")
    #print("Nodes : %s" % ([str(node) for node in ograph[0]]))
    #print("Edges : %s" % ([str(edge) for edge in ograph[1]]))
    
    numnodes = len(ograph[0])
    numedges = len(ograph[1])
    print("Number of nodes in original graph: %d" % (numnodes))
    print("Number of edges in original graph: %d" % (numedges))
    
    print("Running 100 times the Random Min-Cut Algorithm...\n")
    mincut = None
    miniter = 0
    results={}
    
    for i in range(0,100):
        #print("run %d:" % (i+1))
        
        cutgraph = copy.deepcopy(ograph)
        
        iterations = randomMinCut(cutgraph)
        
        curcut = len(cutgraph[1])
        if mincut == None:
            mincut = curcut
            miniter += iterations
        elif mincut > curcut:
            mincut = curcut
            miniter += iterations
            
        res = results.get(curcut)
        if not res:
            res = 0
        results[curcut] = res+1
        #print("iterations : %d\nprint remaining edges: %d\n" % (iterations, curcut))
    
    print("iterations: %d" % (iterations))
    print("Minimal cut found: %d" % (mincut))
    print("Minimal cut found in %d iterations" % (iterations))
    print("Results found")
    for key,value in results.items():
        print("%d -> %d%%" % (key,value))

if __name__ == '__main__':
    main()
