def ex_prob(array,n):
    d = {}
    array.sort()
    i = 1
    r = 0.
    for e in array[::-1]:
        d[e] = i
        i+=1
    print d
    r = d[n]/(len(d)+1.)
    return r


a = [4,2,5,3]
print ex_prob(a,4)