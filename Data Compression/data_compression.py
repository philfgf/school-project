import re

class node:
    
    def left(self, left):
        self.left = left
        return self.left
    def right(self, right):
        self.right = right
        return self.right
    def freq(self, frequency):
        self.frequency = frequency
        return self.frequency
    
def Parent(i):
    return i // 2

def Left(i):
    return 2 * i

def Right(i):
    return 2 * i + 1

def Huffman(C):
    n = abs(len(C))
    Q = C
    z = node()
    
    for i in range(0, (n - 1), 1):
        x = Extract_Min(Q)
        print x
        #z.left(x)
        #y = Extract_Min(Q)
        # print y
        #z.right(y)
        #z.freq(x.freq() + y.freq())
        #Insert(Q,z)
        print Q
    return Extract_Min(Q)

def main():
    C = []
    a,b,c,d,e,f = 0,0,0,0,0,0
    files = open('char_info.txt', 'r')
    for line in files:
        line = line.strip('\r')
        for i in line:
            if(i == 'a'):
                a += 1
            if(i == 'b'):
                b += 1
            if(i == 'c'):
               c += 1 
            if(i == 'd'):
                d += 1
            if(i == 'e'):
                e += 1
            if(i == 'f'):
                f += 1
    
    Insert(C,a)
    Insert(C,b)
    Insert(C,c)
    Insert(C,d)
    Insert(C,e)
    Insert(C,f)
    print(C)
    m = Huffman(C)
    print m
    
def Heap_Decrease_Key(Q,i,x):
    if(x > Q[i]):
        print("error new key is smaller than current key\n")
    #print i
    i += 1
    Q[i] = x
    while((i > 0) and (Q[Parent(i)] > Q[i])):
        Q[i], Q[Parent(i)] = Q[Parent(i)], Q[i]
        i = Parent(i)
    Build_Heap(Q)
    
def Extract_Min(Q):
    heapSize = len(Q) - 1
    if(heapSize < 0):
        print("error heap underflow")
    s = Q[0]
    Q[0] = Q[heapSize]
    del(Q[0])
    Min_Heapify(Q,0)
    return s

def Build_Heap(Q):
    #For loop that goes from the floor of len S to 0
    for i in range(len(Q) - 1 // 2, -1, -1):
        Min_Heapify(Q,i)
        
def Min_Heapify(Q,i):
    l = Left(i)
    r = Right(i)
    if(l < len(Q) and Q[l] < Q[i]):
        smallest = l
    else:
        smallest = i
    if(r < len(Q) and Q[r] < Q[smallest]):
       smallest = r
    if(smallest != i):
       Q[i], Q[smallest] = Q[smallest], Q[i]
       Min_Heapify(Q,smallest)

def Insert(Q,x):
    heapSize = len(Q) - 1
    print len(Q)
    Q.append(x)
    Heap_Decrease_Key(Q,heapSize,x)

main()
