#!/usr/bin/env python
# -*- coding: cp932 -*-
def levenshtein_distance(a , b):
    """
        >>> import levenshtein
        >>> levenshtein.levenshtein_distance('bcd','efg')
        3
        >>> levenshtein.levenshtein_distance('abc', 'abc')
        0
        >>> levenshtein.levenshtein_distance('kitten', 'sitting')
        3
        >>> levenshtein.levenshtein_distance('smei', 'mei')
        1
        >>> levenshtein.levenshtein_distance('12345', '234')
        2
        >>> levenshtein.levenshtein_distance('������', '�߂���')
        3
        >>> levenshtein.levenshtein_distance('�Ɩ�', '�Ɩ�')
        0
        >>> levenshtein.levenshtein_distance('������', '������')
        1
        >>> levenshtein.levenshtein_distance('�������̂���', '����')
        4
        >>> levenshtein.levenshtein_distance('CD�V���b�v', 'C�V���b�N')
        2
        >>> levenshtein.levenshtein_distance('�Ύ�', '�ԉ�')
	2
    """

    m = [ [0] * (len(b) + 1) for i in range(len(a) + 1) ]

    for i in xrange(len(a) + 1):
        m[i][0] = i

    for j in xrange(len(b) + 1):
        m[0][j] = j

    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                x = 0
            else:
                x = 1
            m[i][j] = min(m[i - 1][j] + 1, m[i][ j - 1] + 1, m[i - 1][j - 1] + x)
    # print m
    return m[-1][-1]

#import sys

#s1 = sys.argv[1]
#s2 = sys.argv[2]

#print levenshtein_distance(s1, s2)
#print levenshtein_distance(unicode(s1, sys.stdin.encoding), unicode(s2, sys.stdin.encoding))
def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
