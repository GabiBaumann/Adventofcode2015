#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

Your puzzle answer was 141.

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

"""

from copy import copy

def followup(places, here, miles):
    dmin = 999999999999
    dmax = 0
    places.remove(here)
    if len(places) == 0: return miles, miles
    for there in places:
        rmin, rmax = followup(copy(places), there, miles + atlas[here][there])
        dmin = min(dmin, rmin)
        dmax = max(dmax, rmax)
    return dmin, dmax

atlas = {}
destinations = {}
places = []
lp1 = []
lp2 = []
ldist = []

with open('input') as file:
    for line in file:
        p1, p2, dist = line.split()[::2]
        lp1.append(p1)
        lp2.append(p2)
        ldist.append(int(dist))
        if p1 not in places: places.append(p1)
        if p2 not in places: places.append(p2)

for i in places: atlas[i] = {}

for i in range(len(ldist)):
    atlas[lp1[i]][lp2[i]] = ldist[i]
    atlas[lp2[i]][lp1[i]] = ldist[i]

dmin = 999999999999
dmax = 0
for start in places:
    rmin, rmax = followup(copy(places), start, 0)
    dmin = min(dmin, rmin)
    dmax = max(dmax, rmax)

print(dmin, dmax)

# 141 736
