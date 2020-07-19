#!/usr/bin/python3

class one_D:

    @classmethod
    def dot_prod(cls, m1, m2):
        a1, a2 = m1
        b1, b3 = m2
        return a1 * b1 + a2 * b3

class two_D(one_D):

    @classmethod
    def dot_prod(cls, m1, m2):
        [[a1, a2], [a3, a4]] = m1
        [[b1, b2], [b3, b4]] = m2
        c1 = super().dot_prod([a1, a2], [b1, b3])
        c2 = super().dot_prod([a1, a2], [b2, b4])
        c3 = super().dot_prod([a3, a4], [b1, b3])
        c4 = super().dot_prod([a3, a4], [b2, b4])

        return [[c1, c2], [c3, c4]]

print(two_D.dot_prod([[1,2],[3,4]],
                     [[5,6],[7,8]]))
