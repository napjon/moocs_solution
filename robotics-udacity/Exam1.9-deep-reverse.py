# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list,
# and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any
# of those elements are lists themselves, reverses all the elements
# in the inner list, all the way down.

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(l):
    c = []
    i = 1
    if is_list(l) == False:
        return []
    else:
        while i < len(l)+1:
            a = l[-i]
            if is_list(a):
                c.append(deep_reverse(a))
            else:
                c.append(a)
            i+=1
    return c







#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]
