# Usage: 
# 
#    $python prob1.py [kmax] [Nmax]
#
# Where kmax is the max length of cycles you want, and Nmax is the max alphabet size.


#
# I am writing inefficient code because the problem is small.
#
# We are concerned about two things: 
#     strings which are multiples of smaller strings, or 
#     rotations of strings the same length.
#
# We will build a 'bad' list parallel to a good one.

import math
import sys
from copy import deepcopy


if len(sys.argv) < 2:
    kmax = 5
else:
    kmax = int(sys.argv[1])

if len(sys.argv) < 3:
    Nmax = 5
else:
    Nmax = int(sys.argv[2])



alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def sequences(i, N=2):
    if i == 0:
        return ['']
    else:
        s = sequences(i - 1, N)
        r = []
        for sub in s:
            for j in range(N):
                r.append(sub + alphabet[j])
        return r

def rotations(s):
    r = set([])
    for i in range(len(s)):
        r.add(s)
        s = s[1:] + s[0]
    return r

def multiples_rotations(s, m=kmax):
    r = []
    for i in range(1 + m/len(s)):
        r.append(s*i)
    r2 = set([])
    for t in r:
        for t2 in rotations(t):
            r2.add(t2)
    return r2



def unique_orbits_up_to(k, N=2):
    if k == 0:
        return []
    else:
        g = unique_orbits_up_to(k - 1, N)
        s = sequences(k, N)
        b = set(deepcopy(g))
        for t in g:
            b = b.union(multiples_rotations(t, k))
        for t in s:
            if t not in b:
                g.append(t)
                b = b.union(multiples_rotations(t, k))
        return g

def display_all():
    for N in range(2, Nmax + 1):
        print "N = " + str(N) + ":"
        solutions = unique_orbits_up_to(kmax, N)
        for i in range(1, kmax+1):
            print "\n\nLength " + str(i) + ":\n"
            for t in [s for s in solutions if len(s) == i]:
                print t
        print "\n\n-----------------------------------------\n\n\n"



display_all()
