import math

def maxInList(L):
    max = None
    for i in xrange(len(P)):
        if(not max or max < P[i]):
            max = P[i]
    return max

def distribution(P, B, b):
    for i in xrange(len(P)-1):
        #km to the next bar
        km = abs(P[i+1]-P[i])
        #Difference between the desired amount of beer and the amount of beer in the current bar
        d = B[i]-b
        #If the current bar needs beer, then take it from the next bar
        if(d < 0):
            B[i] = b
            #Remove the beers from the next bar + transfer beer cost
            B[i+1] += d - km*2
        #If the current bar doesn't need beer, then try to transfer the remaining beer.
        #But only if the quantity of the remaining beers exceeds the beer transfer cost
        elif (d > km*2):
            B[i+1] += d - km*2
    return (B[-1] >= b)

def optimalDistributionLoop(P, B, b):
    if(distribution(P, B[:], b)):
       return b
    else:
       return max(optimalDistributionLoop(P, B, (b/2.0)), optimalDistributionLoop(P, B, ((3.0*b)/4.0)))

def optimalDistribution(P, B):
    return optimalDistributionLoop(P, B, maxInList(B))

def simon (P, B):
    left = 0;
    right = maxInList(B)
    while (right - left > 1):
        if(distribution(P[:], B[:], (left+right)/2)):
           left = (left+right)/2
        else:
           right = (left+right)/2
    if(distribution(P[:], B[:], right)):
        return right
    else:
        return left

P = [0,5,13,33,36]
B = [20,40,80,10,20]
#print distribution(P,B, 38)
#print B
#print optimalDistribution(P,B)
print simon(P,B)
