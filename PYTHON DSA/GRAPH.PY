'''  _________  GRAPH  _________

* hierarchical data structure
* collection of nodes(vertices) and edges(connects the nodes)
* vertices represents data and edges represents relation b/w vertices
* graphs can be many type 
    directed graph(one node directing to another node in one direction) 
    undirected(nodes are connected but they are not directing to each other)
    weighted(directed graph with addtional values called as weight it can be distance,time etc)

* implementatin of graph -- 
    by an adjacency list( one node -[list of all adjacent nodes])
    by adjacency matrix ( matrix of 2d , if two nodes are adjacent then 1 otherwise 0 )

* traversing/searching of nodes in graphs --
    by BFS -- graph is created and nodes are in levels from (0 to n) or(1 to n)
                traversing of nodes will start from level 0/1 and then it will go to level+1
                from left to right nodes till last node in level 2 and it goes till last level

    by DFS -- in this firstly nodes are traversed in vertical depth nodes are in one straight line 
                after completing one vertical line it back-track and traverse other connected nodes 
                from left to right


'''


# implementing graph

class graph:
    def __init__(self,edges,n):
        self.adjList = [[] for _ in range(n)]

        for (src,dest) in edges:
            self.adjList[src].append(dest)

def printGraph(graph):
    for src in range(len(graph.adjList)):
        for dest in graph.adjList[src]:
            print(f'({src} -> {dest}) ',end='')
        print()

if  __name__ == '__main__':
    edges = [(0,1),(1,2),(2,0),(2,1),(3,2),(4,5),(5,4)]
    n = 6
    Graph = graph(edges,n)
    printGraph(Graph)


















































'''

# implementing graphs
import pprint
'''
# we will create seperate class for vertex , edge , and graph 

# vertex = it will create vertex and add its edge connections to self.connections variable
# edge = it will create edge , as edge is connected by two node it will store from_var and to_var (nodes) values
# graph = it will create graph i.e.. dictionary , will have vertices and its connections values

'''


# creating class vertex for creating node for graph
class vertex:
    # creating instance of the class it will create a node/verex for graph
    
    def __init__(self,name):
        self.name=name # name of the vertex
        self.connections =[] # all connections/edges of the vertex , one vertex can have multiple connections
        
    # creating function add_edges , it will add edges to connections for the node/vertex created before    
    
    def add_edges(self,obj):
        self.connections.append(obj)

# creating class Edge for creating edges for graph 
class Edge:
    def __init__(self):
        self.connections =[]
    
    def add_edge(self,from_ver,to_ver):
        self.connections.append(from_ver.name)
        self.connections.append(to_ver.name)
        
class Graph:
    def __init__(self):
        self.graph  ={}
    
    def add_vertices(self,obj):
        self.graph.update({obj.name:obj.connections})
        
        
        
# testing

# creating vertices
v1 = vertex("1")
v2 = vertex("2")
v3 = vertex("3")
v4 = vertex("4")

# creating edges
e1=Edge()
e1.add_edge(v1,v2)
e2=Edge()
e2.add_edge(v1,v3)
e3=Edge()
e3.add_edge(v2,v3)
e4=Edge()
e4.add_edge(v3,v4)
e5=Edge()
e5.add_edge(v4,v1)

# as edges are created now we need to create connections
v1.add_edges(e1.connections)
v1.add_edges(e2.connections)
v2.add_edges(e3.connections)
v3.add_edges(e4.connections)
v4.add_edges(e5.connections)

# creating graph

g1 = Graph()
g1.add_vertices(v1)
g1.add_vertices(v2)
g1.add_vertices(v3)
g1.add_vertices(v4)

pprint.pprint(g1.graph)

        


'''



# class Graph:
#     def __init__(self,edges):
#         self.edges = edges
#         # creating a dictionary which will define all possible routes from one node to all other nodes
#         self.graph_dict ={}
#         '''
#         login -- 
#         starting from 1st destination to last destination i.e.  start and end in self.edges
#         if start means the departure node(key) is already present in self.graph_dict then add its destination
#         value i.e.. end to the self.graph_dict otherwise
#         '''
#         for start, end in self.edges:
#             if start in self.graph_dict:
#                 # if key is already encountered before then its neighbour node will be append to the list of destination
#                 self.graph_dict[start].append(end)
#             else:
#                 # else new key will be added to the dictionary with its value
#                 self.graph_dict[start] = [end]
#         print(self.graph_dict)


# # this function will get the source to destination all possible routes , start = source , end = destination 
# # path = [path or node to follow to get to the destination]
#     def get_paths(self,start,end,path=[]):
#         path = path + [start] # it will 

#         if start == end:
#             return [path]

#         if start not in self.graph_dict:
#             return[]
        
#         paths = []
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 new_paths=self.get_paths(node,end,path)
#                 for p in new_paths:
#                     paths.append(p)

#         return paths

        
#     def Get_shortest_path(self,start,end , path=[]):
#         path = path +[start]

#         if start ==end:
#             return path
        
#         if start not in self.graph_dict:
#             return None
        
#         shortest_path = None
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 sp = self.Get_shortest_path(node,end,path)
#                 if sp:
#                     if shortest_path is None or len(sp) < len(shortest_path):
#                         shortest_path = sp
#         return shortest_path





# if __name__ == '__main__':
#     routes = [
#         # all this are edges of the graphs will pe passed in graph class and will create all edges and vertices
#         ("Mumbai","Paris"),
#         ("Mumbai","Dubai"),
#         ("Paris","Dubai"),
#         ("Paris","New York"),
#         ("Dubai","New York"),
#         ("New York","Toronto"),
#     ]

#     routes_graph = Graph(routes)
#     print(routes_graph.Get_shortest_path("Mumbai","New York"))