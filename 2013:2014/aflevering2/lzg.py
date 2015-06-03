def lzg(a):
    #Laengen af listen a
    n = len(a)
    #Hvis a er tom, er den trivielle loesning 0
    if(n == 0):
        return 0
    lastDiff = None
    #Hvis a ikke er tom, saa er loesningen trivielt minimum 1
    c = 1
    for i in xrange(n-1):
        diff = a[i] - a[i+1]
        #Tael op hvis:
        #1: Det er den foerste iteration og a[0] og a[1] ikke er ens
        #2: Der er sket et zigzag
        if((lastDiff is None and diff != 0) or (diff < 0 and lastDiff > 0) or (diff > 0 and lastDiff < 0)):
           c += 1
           lastDiff = diff
        #Hvis differencen er absolut stoerre end den sidste
        #saa set lastDiff til den nuvaerende diff for at komme uden om det lokale maksimum
        elif(lastDiff is None or abs(lastDiff) < abs(diff)):
            lastDiff = diff
    return c
