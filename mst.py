'''
I have used Kruskal's algorithm to solve this problem. The basic idea is to sort 
the edges by their weight and start include them edge without causing
a cycle. One way to make sure there are no cycle in the graph is by keep track of 
each vertice in a list of sets. If the new edge will connect two vertices
within the same set, we will not include it. Else, we include the set and take 
union of the sets. This algorithm has may parts. First, generate list of edges will 
take O(E) time. sorting the edges by weight will take O(Elog(E)) 
time. looping through each edges, find the indices, and merge sets 
will take worst case O(E*V) time and O(V) space. we have to convert the edges 
back to the required output graph structure that will take O(E) time and O(V) space. 
Overall my algorithm will take O(E*V) time and O(E) space.
'''

def question3(G):
    # check if G is dictionary
    if type(G) != dict:
        return "Error: G is not dictionary!"

    # check if G has more than one vertices 
    if len(G) < 2:
        return "Error: G lacks enough vertices to form graph"

    # get a set of vertices
    vertices = G.keys()
    # print vertices

    # get unique set of edges
    edges = set()
    for i in vertices:
        for j in G[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))

    # sort edges by weight
    edges = sorted(list(edges))

    # loop through edges and store only the needed ones
    output_edges = []
    vertices = [set(i) for i in vertices]
    # print(vertices)
    for i in edges:
        print(i)
        # get indices of both vertices
        for j in range(len(vertices)):
            if i[1] in vertices[j]:
                i1 = j
            if i[2] in vertices[j]:
                i2 = j
        # print(vertices)


        # store union in the smaller index and pop the larger index
        # also store the edge in output_edges
        if i1 < i2:
            vertices[i1] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i2)
            output_edges.append(i)
        if i1 > i2:
            vertices[i2] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i1)
            output_edges.append(i)

        # terminate early when all vertices are in one graph
        if len(vertices) == 1:
            break
            
    # generate the ouput graph from output_edges
    output_graph = {}
    for i in output_edges:
        if i[1] in output_graph:
            output_graph[i[1]].append((i[2], i[0]))
        else:
            output_graph[i[1]] = [(i[2], i[0])]

        if i[2] in output_graph:
            output_graph[i[2]].append((i[1], i[0]))
        else:
            output_graph[i[2]] = [(i[1], i[0])]
    return output_graph

def test():
    test_graph1 = {'A': [('B', 7), ('D', 5)],
     'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
     'C': [('B', 8), ('E', 5)],
     'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
     'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
     'F': [('D', 6), ('E', 8), ('G', 11)],
     'G': [('E', 9), ('F', 11)]}

    print ( "result of test one")
    question3(test_graph1)

    test_graph2 = []
    print ( "result of test two")
    print(question3(test_graph2))

    test_graph3 = {}
    print ( "result of test three")
    print(question3(test_graph3))

test()
