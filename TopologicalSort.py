#!/usr/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Created on December 4, 2017                                 #
#############################################################################################

# Importing modules

from collections import defaultdict, namedtuple
from itertools import islice

# Function Definitions

# Reference : https://stackoverflow.com/questions/15038876/topological-sort-python
Results = namedtuple('Results', ['sorted', 'cyclic'])


def topological_sort(dependency_pairs):
    """Sort values subject to dependency constraints"""
    num_heads = defaultdict(int)   # num arrows pointing in
    tails = defaultdict(list)      # list of arrows going out
    heads = []                     # unique list of heads in order first seen
    for h, t in dependency_pairs:
        num_heads[t] += 1
        if h in tails:
            tails[h].append(t)
        else:
            tails[h] = [t]
            heads.append(h)

    ordered = [h for h in heads if h not in num_heads]
    for h in ordered:
        for t in tails[h]:
            num_heads[t] -= 1
            if not num_heads[t]:
                ordered.append(t)
    cyclic = [n for n, heads in num_heads.items() if heads]
    return Results(ordered, cyclic)


#############################################################################################

# Main Program

if __name__ == '__main__':
    #print("\nResult for a acyclic graph: ")
    #print( topological_sort('aa'.split()), "\n" )
    #print("\nResult for a cyclic graph: ")
    #print(topological_sort('ai bg cf ch dh eb fe fg hd he ib'.split()), "\n")
    print("\nResult for a acyclic graph: ")
    print(topological_sort('ah bg cf ch di ed fb fg hd he ib'.split()), "\n")

#############################################################################################
#                                       End of Program                                      #
#                                     Copyright (c) 2017                                    #
#############################################################################################
