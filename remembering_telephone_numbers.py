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

Overview:
#import -- we'll need accumulate and permutations
from itertools import*

unordered_partitions = [[3,2,2,2,2],[4,3,2,2],[3,3,3,2],[4,4,3]]

#we don't need to take the set.union in the golf as we iterate over each element
ordered_partitions = set.union(*({*permutations(unordered_partition)}
                                for unordered_partition in unordered_partitions))

#we use accumulate to give our start and end indices for each grouping
slicings_for_partition = [[0]+[accumulate(partition)]
                          for partition in ordered_partitions]

#all the possible groupings of the phone_number
possible_groupings = [phone_number[i:j]
                      for i,j in zip(slicings_for_partition[:-1],
                                     slicings_for_partition[1:])]

#count the number of leading zeros in each grouping
number_of_leading_zeros = sum(not int(group[0]) for group in possible_groupings)

#sort by leading_zeros and then by length of list
best_grouping = sorted((number_of_leading_zeros, len(grouping),
                        grouping for grouping in possible_groupings))[0][2]

#add spaces between the groups
Then we return " ".join(best_grouping)
"""
from itertools import*;p=lambda h:" ".join(sorted((sum(not int(f[0])for f in g),len(g),g)for g in[[h[d:e]for d,e in zip(c[:-1],c[1:])]for c in[[0]+[*accumulate(b)]for a in[[3,2,2,2,2],[4,3,2,2],[3,3,3,2],[4,4,3]]for b in{*permutations(a)}]])[0][2])
