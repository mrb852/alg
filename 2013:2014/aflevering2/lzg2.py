def same(a, b):
    return a < 0 and b < 0 or a == b or a > 0 and b > 0

def lzg(a, n):
    q1 = 0
    c = 1
    for i in xrange(1, n):
        q = a[i-1] - a[i]
        if not(same(q, q1)) and q != 0:
            c = c + 1
        q1 = q
    return c

a = [6,1,7,7,2,4,7,1,2,3]
print lzg(a, len(a))
