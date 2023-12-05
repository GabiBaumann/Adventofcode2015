#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

code = chars = newenc = 0
with open('input') as file:
    for line in file:
        ll = len(line.strip())
        code += ll
        #pt2
        i = 0
        while i < ll:
            if line[i] == '"':
                newenc += 1
            elif line[i] == '\\':
                newenc += 2
                i+=1
                if line[i] == 'x':
                    newenc += 2
                    i+=2
                elif line[i] == '"':
                    newenc += 1
                elif line[i] == '\\':
                    newenc += 1
            newenc += 1
            i+=1
        newenc += 2
        #print(newenc)    
        #pt1
        i = 1
        while i < ll-1:
            if line[i] == '\\': 
                i+=1
                if line[i] == 'x':
                    i+=2
            i += 1
            chars += 1
print(code, chars, code - chars)
print(code, newenc, newenc - code)

# 6195 4845 1350
# 6195 8280 2085

# pt1: (first try)
# 1350
#
# pt2: (first try)
# 2085
