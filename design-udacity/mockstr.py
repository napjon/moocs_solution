def _unmockstr(x):
    "Secret function to convert mockstr back to str; leaves other objects unchanged."
    return str.__str__(x) if isinstance(x, mockstr) else x

class mockstr(str):
    """An object that looks and acts like a str, but counts comparisons and accesses.
    Obeys two rules:
    (1) Any piece of a mockstr that is returned must be a mockstr (not a str)
    (2) Any comparison or access increments num_comparisons or num_accesses
    Despite these precautions, the class is Not secure against many simple attacks,
    including map(ord, s) or str.__str__(s).
    """

    ## Track total number of comparisons and accesses to any mockstr objects
    num_comparisons, num_accesses = 0, 0

    def __getitem__(self, i):
        "s[i] counts as 1 access."
        mockstr.num_accesses += 1
        return mockstr(_unmockstr(self)[i])

    def __getslice__(self, start, end):
        "s[i:i+n] counts as n accesses."
        end = min(len(self), end)
        mockstr.num_accesses += (end - start)
        return mockstr(_unmockstr(self)[start:end])

    ## s1 == s2 counts as len(s1) comparisons (so s[i] == s[j] counts as 1).
    def __eq__(self, other): return self._c() == _unmockstr(other)
    def __ne__(self, other): return self._c() != _unmockstr(other)
    def __ge__(self, other): return self._c() >= _unmockstr(other)
    def __le__(self, other): return self._c() <= _unmockstr(other)
    def __gt__(self, other): return self._c() >  _unmockstr(other)
    def __lt__(self, other): return self._c() <  _unmockstr(other)

    def _c(self):
        "Secret method to convert to str, incrementing num_comparisons by len(self)."
        mockstr.num_comparisons += len(self)
        return _unmockstr(self)

    def _a(self):
        "Secret method to convert to str, incrementing accesses by len(self)."
        mockstr.num_accesses += len(self)
        return _unmockstr(self)

    ## Any piece of self returned by normal methods should be a mockstr, not a str.
    def upper(self):        return mockstr(self._a().upper())
    def lower(self):        return mockstr(self._a().lower())
    def title(self):        return mockstr(self._a().title())
    def capitalize(self):   return mockstr(self._a().capitalize())
    def swapcase(self):     return mockstr(self._a().swapcase())
    def strip(self):        return mockstr(self._a().strip())
    def lstrip(self):       return mockstr(self._a().lstrip())
    def rstrip(self):       return mockstr(self._a().rstrip())
    def split(self, *args): return map(mockstr, self._a().split(*args))
    def rsplit(self, *args):return map(mockstr, self._a().rsplit(*args))
    def join(self, *args):  return mockstr(self._a().join(*args))
    def __mod__(self, tup): return mockstr(self._a() % tup)

    def __str__(self):
        return '<mockstr %r of len %d at 0x%x>' % (_unmockstr(self), len(self), id(self))

    __repr__ = __str__

    @staticmethod
    def reset(verbose=True):
        "Reset counts to zero, and optionally, before resetting, print the counts."
        if verbose: print 'mockstr: %d accesses and %d comparisons' % (
                mockstr.num_accesses, mockstr.num_comparisons)
        mockstr.num_accesses, mockstr.num_comparisons = 0, 0

##############################################################################

class test_mockstr:
    """## You can run this test with: python -m doctest mockstr.py
>>> s = mockstr('0123456789')
>>> len(s)
10
>>> s[0] == '0'
True
>>> s[-1] == '9'
True
>>> s.reset()
mockstr: 2 accesses and 2 comparisons
>>> s[0] == s[1]
False
>>> s.reset()
mockstr: 2 accesses and 1 comparisons

>>> sum(a == b for a in s for b in s)
10
>>> s.reset()
mockstr: 121 accesses and 100 comparisons

>>> items = list(s)
>>> sum(a == b for a in items for b in items)
10
>>> s.reset()
mockstr: 11 accesses and 100 comparisons

>>> s1, s2 = mockstr('this THAT').split()
>>> s.reset()
mockstr: 9 accesses and 0 comparisons
>>> s1[0] == s2[0]
False
>>> s.reset()
mockstr: 2 accesses and 1 comparisons
>>> s1[0].upper() == s2[0].upper()
True
>>> s.reset()
mockstr: 4 accesses and 1 comparisons
"""