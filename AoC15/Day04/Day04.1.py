#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

Your puzzle input is bgvyzdsv.

Your puzzle answer was 254575.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Now find one that starts with six zeroes.
"""

from hashlib import md5

base = "bgvyzdsv"
i = 0
while True:
    i += 1
    s = base + str(i)
    if md5(s.encode()).hexdigest()[:5] == "00000": print(i)
    if md5(s.encode()).hexdigest()[:6] == "000000": 
        print(i)
        break

# part1:
# 254575
#
# part2:
# 1038736
