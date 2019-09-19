#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:59:15 2019
@author: salt

From python discord:
    you are trying to remember phone numbers but cant remember the long number!
    in order to fix this you have decided to split the phone number into
    smaller numbers. however its hard to remember numbers that start with a
    leading zero. so you split them into groups of 2-4 digits with as few
    leading zeros as possible.
    e.g. 01365400606 >> 0136 5400 606

My golf attempt uses the knowledge that all the un-ordered legal partitions of
an 11-digit number are [[3,2,2,2,2],[4,3,2,2],[3,3,3,2],[4,4,3]].
"""
from itertools import*
def f(n):
    m=e=6
    for k in[[n[v:k]for v,k in zip(t[:-1],t[1:])]
             for t in[[0]+[*accumulate(j)]
                      for r in[[3,2,2,2,2],[4,3,2,2],[3,3,3,2],[4,4,3]]
                      for j in{*permutations(r)}]]:
        a=sum(not int(l[0]) for l in k);b=len(k)
        if(a==m and b<e)or a<m:e=b;m=a;p=k
    return " ".join(p)
