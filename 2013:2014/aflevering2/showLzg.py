def showLzg(a):
    #laengden af listen a
    n = len(a)
    #hvis a er tom, er den trivielle loesning den tomme liste
    if(n == 0):
        return []
    lastDiff = None
    #vi starter med et trivielt gyldigt element i listen
    l = [a[0]]
    for i in xrange(n-1):
        diff = a[i] - a[i+1]
        #Vi tilfoejer det i+1 element til vores liste hvis:
        #1 vi er i vores foerste iteration og a[0] og a[1] ikke er ens
        #2 Der er sket et zigzag
        if((lastDiff is None and diff != 0) or (diff < 0 and lastDiff > 0) or (diff > 0 and lastDiff < 0)):
           lastDiff = diff
           l.append(a[i+1])
        #Hvis differencen er absolut stoerre end den sidste
        #saa set lastDiff til den nuvaerende diff for at komme uden om det lokale maksimum
        elif(lastDiff is None or abs(lastDiff) < abs(diff)):
            lastDiff = diff
            l[len(l)-1] = a[i+1]
    return l
