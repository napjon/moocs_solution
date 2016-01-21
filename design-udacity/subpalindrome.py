# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!
import string

def substract(n):
    (a,b) = n
    return abs(a-b)


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    if text == '':
        return (0,0)
    st = string.lower(text)
    stt = set(st)
    f = []
    g = []
    for i in stt:#Takes i and j in stt
        s = i
        r = i
        closed = []
        for j in st:
            if j+s+j in st:
                s = j+s+j
                closed.append(j)
                je = st.find(j)
                f.append((je, je+len(s)))
            #This is the exception when palindrome is not obvious in the text
            if len(set(r+j)) == 1 and r+j in st:
                r+=j
                je = st.find(r)
                g.append((je, je+len(s)+1))
    try:
        return max(f, key = substract)
    except ValueError:
        return max(g, key=substract)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

L = longest_subpalindrome_slice
#print L('racecar')
#print L('Racecar')
#print L('RacecarX')
#print L('Race carr')
#print L('')
#print L('something rac e car going')
#print L('Mad am I ma dam.')
#print L('xxxxx')
#print longest_subpalindrome_slice('something rac e car going')


def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

print timedcall(test)