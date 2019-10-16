import re

def Parent(i):
    return i // 2

def Left(i):
    return 2 * i

def Right(i):
    return 2 * i + 1

def Build_Heap(S):
    #For loop that goes from the floor of len S to 0
    for i in range(len(S) - 1 // 2, -1, -1):
        Max_Heapify(S,i)
          
def Max_Heapify(S,i):
    l = Left(i)
    r = Right(i)
    if(l < len(S) and S[l] > S[i]):
        largest = l
    else:
        largest = i
    if(r < len(S) and S[r] > S[largest]):
       largest = r
    if(largest != i):
       S[i], S[largest] = S[largest], S[i]
       Max_Heapify(S,largest)

def Insert(S,x):
    heapSize = len(S) - 1
    S.append(x)
    Heap_Increase_Key(S, heapSize, x)

def Heap_Increase_Key(S,i,x):
    if(x > S[i]):
        print("error new key is smaller than current key\n")
    i += 1
    S[i] = x
    while((i > 0) and (S[Parent(i)] < S[i])):
        S[i], S[Parent(i)] = S[Parent(i)], S[i]
        i = Parent(i)
    Build_Heap(S)
    
def Maximum(S):
    return S[0]

def Extract_Max(S):
    heapSize = len(S) - 1
    if(heapSize < 0):
        print("error heap underflow")
    m = S[0]
    S[0] = S[heapSize]
    del(S[0])
    Max_Heapify(S,0)
    return m
          
def main():
    f = open('customers_info.txt', 'r')
    S = []
    B = {}
    A = []
    
    #Creates a list of priority numbers from the file
    for line in f:
        line = (line.rsplit(': ', 1)[1])
        line.replace('\n', '')
        S.append((re.sub(r'[^0-9]', '', line)))

    #Deletes remaing white space in the list
    count = 0
    for l in S:
        if(l == ''):
            del(S[count])
            count += 1
    S = [int(i) for i in S]
    
    f.close()
    f = open('customers_info.txt', 'r')

    #Creates a Dictionary from file key = name and value = priority
    for line in f:
        line = (line.rsplit(': ', 1)[1])
        A.append(line.replace('\n', ''))
    B = {A[i]: A[i+1] for i in range(0, len(A), 2)}
    
    
    Insert(S,1)
    m = Maximum(S)
    print("List of Customers according to their Priority:")
    #Checks to see which priority number is first in the waiting line 
    for name, queue in B.items():
        if(m == int(queue)):
            print(name)
            
    Extract_Max(S)
    m = Maximum(S)

    #Checks to see which priority number is first in the waiting line 
    for name, queue in B.items():
        if(m == int(queue)):
            print(name)
            
    Extract_Max(S) 

main()
