#takes two sets A and B, and returns the set A-B
def setDiff(A, B):
    result = []
    for i in xrange(len(A)):
        found = False
        for ii in xrange(len(B)):
            a = A[i]
            b = B[ii]
            ax = a[0]
            ay = a[1]
            bx = b[0]
            by = b[1]
            if((ax == bx and ay == by) or (ax == by and ay == bx)):
                found = True
                break
        if(not found):
            result.append(a)
    return result

#Find the intersection between set A and B
def intersection(A, B):
    result = []
    for i in xrange(len(A)):
        found = False
        for ii in xrange(len(B)):
            a = A[i]
            b = B[ii]
            ax = a[0]
            ay = a[1]
            bx = b[0]
            by = b[1]
            if((ax == bx and ay == by) or (ax == by and ay == bx)):
                found = True
                break
        if(found):
            result.append(b)
    return result

#Unlinks a graph representet by V vertexes and E edgets
#and returns the number of components for each U unlink operation
def offlineUnlink(E, U):
    #list to hold the result
    result = []
    #be sure that the unlink operations are legal
    U = intersection(E, U)
    diff = setDiff(E, U)
    for i in xrange(len(U)-1):
        result.append(len(E)-len(diff))
        diff.append(U[len(U)-1-i])
    return result

def offlineUnlink2(E, U):
    #list to hold the result
    result = []
    #be sure that the unlink operations are legal
    U = intersection(E, U)
    U1 = []
    n = len(E)
    for i in xrange(len(U)):
        U1.append(U[i])
        diff = setDiff(E, U1)
        result.append(n-len(diff))
    return result

E = [[1,3],[4,3],[5,3],[7,3],[5,6],[6,7],[7,2]]
U = [[1,3],[7,6],[2,7],[3,5]]
print offlineUnlink2(E, U)
