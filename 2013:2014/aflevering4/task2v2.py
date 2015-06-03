class set:
    brewery = None
    rank = 0
    p = None

def makeSet(x):
    a = set();
    a.rank = 0
    a.p = a
    a.brewery = x
    return a

def link(x, y):
    if(x.rank > y.rank):
        y.p = x
    else:
        x.p = y
        if(x.rank == y.rank):
            y.rank = y.rank + 1

def union(x, y):
    link(findSet(x), findSet(y))

def findSet(x):
    if(x.p != x):
        x.p = findSet(x.p)
    return x.p

def connectedComponents(L):
    for l in L:
        x = l[0]
        y = l[1]
        if(findSet(x) != findSet(y)):
            union(x, y)

def query(x, y):
    return findSet(x) == findSet(y)

def countComponent(V, E):
    vertexes = len(V)
    connectedComponents(E)
    components = []
    for(e in E):
        set = findSet(e)
        found = False
        for c in components:
            if (c == set):
                found = True
                vertexes -= 1
                break
        if(not found):
            components.append(set)

def unlink(V, E, U):
    connectedComponents(U)
    count = 0
    for e in E:
        if(query(e[0], e[1])):
            count +=1
    print count

b1 = makeSet(1)
b2 = makeSet(2)
b3 = makeSet(3)
b4 = makeSet(4)
b5 = makeSet(5)
b6 = makeSet(6)
b7 = makeSet(7)

V = [b1,b2,b3,b4,b5,b6,b7]
E = [[b1,b3],[b4,b3],[b5,b3],[b7,b3],[b5,b6],[b6,b7],[b7,b2]]
U = [[b1,b3]]#,[b7,b6],[b2,b7],[b3,b5]]

unlink(V, E, U)
