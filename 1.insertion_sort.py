#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Apr 13, 2014 '
__author__= 'samuel'

def insertion_sort(A):
    n = len(A)
    if n == 1:
        return A
    for key,i in [(A[j], j-1) for j in xrange(1,n)]:
        print '%s@[%s]' % (key, i+1),
        while i>0 and A[i] > key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key
        print '%s->[%s]' % (key, i+1),
        print A
    return A

def main():
    A = [1,2,3,9,6,10,5,31,8]
    B = insertion_sort(A)
    print ''
    print B

if __name__ == '__main__':
    main()
