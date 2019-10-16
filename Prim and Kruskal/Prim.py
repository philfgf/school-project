def Parent(i):
    return i / 2

def Left(i):
    return 2 * i + 1

def Right(i):
    return 2 * i + 2
    
def Extract_Min(Q):
    heapSize = len(Q) - 1
    if(heapSize < 0):
        print("error heap underflow")
    #Smallest variable and 1st element in list
    s = Q[0]
    Q[0] = Q[heapSize]
    del(Q[0])
    Min_Heapify(Q,0)
    return s

def Build_Heap(Q):
    #For loop that goes from the floor of len S to 0
    for i in range(len(Q) - 1 / 2, -1, -1):
        Min_Heapify(Q,i)
        
def Min_Heapify(Q,i):
    #Declared left and right variables
    l = Left(i)
    r = Right(i)
    
    #Changed the max heapify into a min heap.
    if(l < len(Q) and Q[l] < Q[i]):
        smallest = l
    else:
        smallest = i
    if(r < len(Q) and Q[r] < Q[smallest]):
       smallest = r
    if(smallest != i):
       Q[i], Q[smallest] = Q[smallest], Q[i]
       Min_Heapify(Q,smallest)

def adj(Adj,u):
    #A appends the adjacency from Adj for the vertex we are located in
    A = []
    for x in range(len(Adj)):
        if Adj[u][x] > 0:
            A.append(x)
    return A

def MST_PRIM(G,Ad,r):
    inf = float('inf')
    key = [inf] * len(Ad)
    pi = [None] * len(Ad)
    key[r] = 0
    Q = G
    
    while Q:
        #w is the weight, u is the vertex, and v is the other vertex attatched to the edge
        w,u,v = Extract_Min(Q)
        Adj = adj(Ad,u)
        for v in Adj:
            if (w,u,v) in Q and w < key[v]:
                pi[v-1] = (w,u,v)
                key[v] = w
    #poping off garbage values
    pi.pop(-1)
    key.pop(0)
    print 'verticies with weight:'
    print pi
    print'Edge weights:'
    print key
    return pi

def main():
    #weight is a nested list that appends the weights of each row from value that is
    #read from the file f
    #graph is the list that we will append the tuples of w,u,v
    #r is the root we are starting at
    weight = []
    graph = []
    r = 0
    with open('graph_file.txt', "r") as f:
        for line in f:
            values = line.rstrip().split(" ")
            weight.append(values)
            
    #assign the value of Adj = weight
    Adj = weight

    #Adj will be the assigned in this for loop by checking through the weight
    #hi and low creates duplicates so you only go through one direction
    #graph is a list of tuples containing the weight and verticies in the form w,u,v
    for i in range(len(weight)):
        for j in range(len(weight[i])):      
            if weight[i][j] != 'inf' and weight[i][j] != '0':
                Adj[i][j] = int(Adj[i][j])
                if i >= j:
                    hi = i
                    low = j
                elif j > i:
                    hi = j
                    low = i
                graph.append((int(weight[i][j]),low,hi))
            if weight[i][j] == 'inf'or weight[i][j] == '0':
                Adj[i][j] = 0
                
    #verticies can be only up to 100
    if len(graph) < 100:
        p = MST_PRIM(graph,Adj,r)

    #Initialize the Adjacency matrix to all 0's
    Adjacency = [[0 for i in range(len(p)+1)] for j in range(len(p)+1)]
    
    print ''
    print 'Adjacency matrix ='

    #for loop that uses each tuple to place the weight i in the correct location in the
    #adjacency matrix using the vertecies j and k
    for i,j,k in p:
        Adjacency[j][k] = i
        Adjacency[k][j] = i

    #prints the matrix
    for i in Adjacency:
        print i


        
main()

