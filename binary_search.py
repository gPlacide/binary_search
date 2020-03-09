#!/bin/python3

import random

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    left = 0
    right = len(xs)-1

    def go(left,right):
        mid = (left+right)//2

        if len(xs) == 0:
            return None
        if xs[left] > 0:
            return left
        if xs[right] < 0:
            return None
        if xs[mid] > 0:
            right = mid -1
        if xs[mid] < 0:
            left = mid+1
        if xs[mid] == 0:
            return mid+1

        return go(left,right)
    return go(left,right)

def _included(xs, x):
    '''
    >>> _included([5,4,3,3,3,3,3,3,3,2,1], 3)
    True
    >>> _included([1,2,3], 4)
    False
    '''
    left =0
    right = len(xs)-1
    
    if len(xs) == 0:
        return False

    def go(left,right):
        mid = (left+right)//2
        
        if right == left and xs[right] != x:
            return False
        if x > xs[mid]:
            right = mid-1
            return go(left,right)
        elif x < xs[mid]:
            left = mid+1
            return go(left,right)
        else:
            return True
    return go(left,right)

def _small_lowest_index(xs,x):
    '''
    >>> _small_lowest_index([5,4,3,3,3,3,3,3,3,2,1], 3)
    2
    >>> _small_lowest_index([1,2,3], 4)
    0
    '''
    left = 0
    right = len(xs)-1
    
    def go(left,right):
        mid = (left+right)//2
        
        if x > xs[mid]:
            right = mid-1
            return go(left,right)
        elif x < xs[mid]:
            left = mid+1
            return go(left,right)
        else:
            right = mid-1
            if xs[mid-1]!=x or mid == 0:
                return mid
            else:
                return go(left,right)
           # return go(left,right)
       # return go(left,right)
    return go(left, right)


def _big_lowest_index(xs,x):
    '''
    >>> _big_lowest_index([5,4,3,3,3,3,3,3,3,2,1], 3)
    8
    >>> _big_lowest_index([1,2,3], 4)
    0
    '''
    left = 0
    right = len(xs)-1
    
    def go(left,right):
        mid = (left+right)//2
        
        if x > xs[mid]:
            right = mid-1
            return go(left,right)

        elif x < xs[mid]:
            left = mid+1
            return go(left,right)
        else:
        
            left = mid+1
            if mid == (len(xs)-1) or  xs[mid+1]!= x:
                return mid
            else:
                return go(left,right)
           # return go(left,right)
       # return go(left,right)
    return go(left, right)
    

def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([1, 2, 3], 4)
    0
    '''
    

    if _included(xs, x):
        high =  _big_lowest_index(xs, x)
        small = _small_lowest_index(xs, x)
        return (high  - small) + 1
    else:
        return 0
 
    


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    
    if abs(hi - lo) < epsilon:
        return (lo+hi)/2
    else:
        m1 = random.uniform(lo, hi)
        m2 = random.uniform(lo, hi)
        
        if f(m1) < f(m2):
            return argmin(f, m1, hi, epsilon)
        else:
            return argmin(f, lo, m2, epsilon)
