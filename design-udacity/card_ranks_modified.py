#What would we do if one special case, which is A-5 straight comes up
#The one that we should modify is card_ranks function


def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ['--23456789TJKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks