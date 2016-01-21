def shuffle(deck):
    """Knuth's Algorithm P."""
    N = len(deck)
    for i in rang(N-1):
        swap(deck, i, random.randrange(i,N))

def swap(deck,i,j):
    """Swap elements i and j of a collections"""
    print 'swap',i,j
    deck[i],deck[j] = deck[j], deck[i]

def test_shuffler(shuffler, deck = 'abcd', n=10000 ):
    counts = defaultdict(int)#keep record of shuffling, and it's always start with zero
    for _ in range(n):#This makes shuffling in range to 10000(n)
        input = list(deck)#Now we want to assign input with list of deck, in this case 'abcd
        shuffler(input)#Use shuffler function as input to shuffle the list input
        counts[''.join(input)] +=1#Now we would want to join all elements of the list as a single string
        e = n*1./factorial(len(deck))#now we would want to assign all elements with equal probability
                                    #So we make expected value(Ex)."n*1." so n can turn into decimal value

        ok = all((0.9 <= counts[item]/e<=1.1)#"ok" will raised if we inspect every element in a list
                for item in counts)#in range that we expect."all" is a built-in function that return
                #True if every element return True
        name = shuffler.__name__#assign name of function to 'name'
        print '%s(%s)%s' % (name, deck,('ok' if ok else '***BAD***'))#Now this line is used-
        print ' ',#to reformat name, deck, and boolean 'ok' to match %s(string)
        for item,count in sorted(counts,items()):#Now this to count each of items with possible-
            print "%s:%4.1f" % (item,count*100/n)#results

def



