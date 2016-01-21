def hand_rank(hand):
    "Return a value indicating how high the hand ranks."
    #counts is the count of each ranks; ranks lists corresponding ranks
#E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7,10,9)# if it same count, ordered highest
    groups = group(['--23456789TJKA'.index(r) for r,s in hand])# we make 1 group of ranks
    counts, ranks= unzip(groups)#we divide groups into two parameter that defined above
    if ranks == (14,5,4,3,2):#We also set a special unique case in straight
        ranks = (5,4,3,2,1)
    straight = len(set(ranks)) == 5 and max(ranks)-min(ranks) == 4#we define a function for straight
    flush = len(set(([s for r,s in hand]))) == 1
    return (9 if (5,)== counts else
            8 if straight and flush else
            7 if (4,1) == counts else
            6 if (3,2) == counts else
            5 if flush else
            4 if straight else
            3 if (3,1,1) == counts else
            2 if (2,2,1) == counts else
            1 if (2,1,1,1) == counts else
            0), ranks
#in this example before we see that actually hand_ranks consist of 5  ranks
#and from 5 ranks in one hand, we could have 7 possible ways to define this combination
#the partition of the 5 ranks actually like above, where set of element that sum up to that integer
#and also we implement lexiographic, where we compared the highest, if not then go to lower and
#so on
#Also this is what we called  REFACTORING.Where we define repeated statement to one simpler
#explanation


def group(items):
    "Return a list of [(count, x)....] highest count first, then highest x first."
    #Groups will receive list as input, count every element, store it to counts
    #and  the second one is ranks, which reprent by x,set of items
    #This will output a list of pairs, a pair of count and it's ranks
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups,reverse = True)

def unzip(pairs):return zip(*pairs)
#Now the unzip function is use to unzip it so the counts and ranks make a 2 separated groups


#Also the hand_rank definition can be used even simpler with the code below
def hand_rank(hand):
    groups = group(['--23456789TJKA'.index(r) for r,s in hand])
    counts, ranks= unzip(groups)
    if ranks == (14,5,4,3,2):
        ranks = (5,4,3,2,1)
    straight = len(set(ranks)) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set(([s for r,s in hand]))) == 1
    return max(count_rankings[counts], 4*straight + 5*flush), ranks

count_rankings = {(5,):10, (4,1):7, (3.2):6, (3,1,1):3, (2,2,1):2,
                  (2,1,1,1):1, (1,1,1,1,1):0}

#Now we are mapping the result that we have into the dictionary.
#This makes the return not to  use 9 lines of code, but just one line of code
#4*straight means to convert boolean to integers. if not straight than 4*0 is 0.
#That also means to flush, if flush, 5*1 equal 5.
#While the dictionary ranking return a ranking based on counts, the other get handled
#by  4*straight + 5*flush
#Now as we now, straight flush in previous return 8, but still ok if its nine.
#We make that because we simply would want to add straight and flush, thus to 9
#We just bump the impossible which is 9 before, to 10. So 8 considered unavailable


#It's up to you, whether want to make concise and nice, or explicitly