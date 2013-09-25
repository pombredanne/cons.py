class Cons:
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
        self.next = point

    def __repr__(self):
        '''
        >>> Cons(3, Cons(8, None))
        3, 8
        '''

        if self.next == None:
            return '%s' % self.value
        else:
            return '%s, %s' % (self.value, self.next)

    def __getitem__(self, i):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[2]
        3

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[-2]
        8
        '''
        current = self
        for _ in range(i):
            current = current.next
        return Cons(current.value, None)

    def __getslice__(self, i, j):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[1:4]
        2, 3, 8

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[:4]
        98, 2, 3, 8

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[1:]
        2, 3, 8, 2

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None)))))[:-2]
        98, 2, 3, 8
        '''
        return self.drop(i).take(j - i)

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
        elif self.next == None:
            return self
        elif n == 1:
            return Cons(self.value, None)
        else:
            return Cons(self.value, self.next.take(n - 1))

    def drop(self, n):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).drop(1)
        2, 3, 8, 2

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).drop(0)
        98, 2, 3, 8, 2

        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).drop(23)
        '''
        if self.next == None:
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
        return self.next

    def last(self):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).last()
        2

        >>> Cons(2, None).last()
        2
        '''
        if self.next == None:
            return self
        else:
            return self.next.last()

    def init(self):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).init()
        98, 2, 3, 8

        >>> Cons(2, None).init()
        '''
        if self.next == None:
            return None
        elif self.next.next == None:
            return Cons(self.value, None)
        else:
            return Cons(self.value, self.next.init())

    def insert(cons, value, i):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).insert(42, 1)
        98, 42, 2, 3, 8, 2
        '''
        return cons[:i] +  Cons(value, cons[i:])

    def __delitem__(cons, i):
        '''
        >>> Cons(98, Cons(2, Cons(3, Cons(8, Cons(2, None))))).__delitem__(2)
        98, 2, 8, 2

        >>> Cons(2, None).__delitem__(0)
        '''
        if i == 0:
            return None
        else:
            return cons[:i] + cons[(i+1):]

    def foldl(self, f, init):
        '''
        >>> Cons(8, Cons(2, Cons(3, Cons(8)))).foldl(lambda a,b:a+b, 0)
        21

        >>> Cons(8, Cons(2, Cons(3, Cons(-7)))).foldl(lambda a,b:b, -7)
        -7
        '''
        if self.next == None:
            return f(init, self.value)
        else:
            return self.next.foldl(f, f(init, self.value))

    def foldr(self, f, init):
        '''
        >>> Cons(8, Cons(2, Cons(3, Cons(8)))).foldl(lambda a,b:a+b, 0)
        21

        >>> Cons(8, Cons(2, Cons(3, Cons(-7)))).foldl(lambda a,b:a, 23)
        23

        This implementation is super inefficient.
        '''
        if self.init() == None:
            return f(self.value, init)
        else:
            return self.init().foldr(f, f(self.value, init))

    def __len__(self):
        '''
        >>> len(Cons(8, Cons(2, Cons(3, Cons(8)))))
        4
        '''
        return self.foldl(lambda a,b:a+1, 0)

    def __add__(a, b):
        '''
        >>> Cons(98, Cons(2, Cons(3, None))) + Cons(7, Cons(8, Cons(2, None)))
        98, 2, 3, 7, 8, 2
        '''
        if a.next == None:
            return Cons(a.value, b)
        else:
            return Cons.__add__(a.init(), Cons.__add__(a.last(), b))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    l = Cons(98, Cons(2, Cons(3, Cons(8, Cons(2)))))

