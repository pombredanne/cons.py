class Cons:
    '''
    A cons cell
    '''
    def __init__(self, value, point = None):
        '''
        >>> Cons(3, None)
        3

        >>> Cons(4)
        4

        >>> Cons(4, Cons(8))
        4, 8
        '''
        if point == None:
            pass
        elif not isinstance(point, Cons):
            raise TypeError('point must be a Cons')

        self.value = value
        self._next = point

    def __repr__(self):
        '''
        >>> Cons(3, Cons(8, None))
        3, 8
        '''

        if self._next == None:
            return '%s' % self.value
        else:
            return '%s, %s' % (self.value, self._next)

#   def __getitem_pythonic__(self, i):
#       '''
#       >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[2]
#       3

#       >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[-2]
#       8

#       >>> [0 for cons in Cons(3, Cons(5))]
#       [0, 0]

#       >>> map(str, Cons(3, Cons(5)))
#       ['3', '5']
#       '''
#       if i == 0:
#           return self.value
#       elif i < 0:
#           return self.init().__getitem__(len(self) + i)
#       elif i > 0:
#           if self.tail() == None:
#               raise IndexError('list index out of range')
#           else:
#               return self.tail().__getitem__(i - 1)

    def __getitem__(self, i):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[0]
        98

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[1]
        2, 3, 8, 2
        '''
        if i == 0:
            return self.value
        elif i == 1:
            return self._next

    def __iter__(self):
        '''
        >>> [0 for cons in Cons(3, Cons(5))]
        [0, 0]

        >>> map(str, Cons(3, Cons(5)))
        ['3', '5']
        '''
        self = self._next
        return self

    def next(self):
        if self._next == None:
            raise StopIteration
        else:
            return self.value

    def __getslice__(self, i, j):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[1:4]
        2, 3, 8

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[:4]
        98, 2, 3, 8

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[1:]
        2, 3, 8, 2

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[:-2]
        98, 2, 3
        '''
        # Switch this to __getitem__ with slices
        # http://www.siafoo.net/article/57
        # http://docs.python.org/release/2.3.5/whatsnew/section-slices.html
        if j > 0:
            return self.drop(i).take(j - i)
        elif j == 0:
            return None

    def take(self, n):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).take(1)
        98

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).take(0)

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).take(2)
        98, 2
        '''
        if n == 0:
            return None
        elif self._next == None:
            return self
        elif n == 1:
            return Cons(self.value, None)
        else:
            return Cons(self.value, self._next.take(n - 1))

    def drop(self, n):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).drop(1)
        2, 3, 8, 2

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).drop(0)
        98, 2, 3, 8, 2

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).drop(23)
        '''
        if self._next == None:
            return None
        elif n == 0:
            return self
        elif n == 1:
            return self.tail()
        else:
            return self.tail().drop(n - 1)

    def head(self):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).head()
        98
        '''
        return self.value

    def tail(self):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).tail()
        2, 3, 8, 2

        >>> Cons(2, None).tail()
        '''
        return self._next

    def last(self):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).last()
        2

        >>> Cons(2, None).last()
        2
        '''
        if self._next == None:
            return self
        else:
            return self._next.last()

    def init(self):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).init()
        98, 2, 3, 8

        >>> Cons(2, None).init()
        '''
        if self._next == None:
            return None
        else:
            return Cons(self.value, self._next.init())

    def insert(cons, value, i):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).insert(42, 1)
        98, 42, 2, 3, 8, 2
        '''
        return cons[:i] +  Cons(value, cons[i:])

    def remove(cons, i):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).remove(2)
        98, 2, 8, 2

        >>> Cons(2, None).remove(0)
        '''
        if i == 0:
            return None
        else:
            return cons[:i] + cons[(i+1):]

    def __len__(self):
        '''
        >>> len(Cons(8, Cons(2, Cons(3, Cons(8)))))
        4
        '''
        return reduce(lambda a,b:a+1, self, 0)

    def __add__(a, b):
        '''
        >>> Cons(98, Cons(2, Cons(3, None))) + Cons(7, Cons(8, Cons(2, None)))
        98, 2, 3, 7, 8, 2
        '''
        if a._next == None:
            return Cons(a.value, b)
        else:
            return Cons.__add__(a.init(), Cons.__add__(a.last(), b))

    def __contains__(container, member):
        '''
        >>> 2 in Cons(98, Cons(2, Cons(3, None)))
        True

        >>> 32 in Cons(98, Cons(2, Cons(3, None)))
        False
        '''
        return (container.value == member) or \
            (container._next != None and member in container._next)

def l(*args):
    '''
    A linked list
    >>> l(3, 5, 9)
    3, 5, 9
    '''
    if len(args) > 0:
        return Cons(args[0], l(*args[1:]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    xs = Cons(98, Cons(2, Cons(3, Cons(8, Cons(2)))))
    ys = l(8, 5, 2, 9, 4)
