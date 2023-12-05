#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

Your puzzle answer was 956.

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

"""

from copy import copy

def toint(w):
    out = 0
    for i in range(16):
        if w[i]: out += 2 ** (15-i)
    return out

def tobool(d):
    b = []
    for i in range(16):
        b.insert(0, True if d%2 else False)
        d = d // 2
    return b

def op_not(w):
    b = []
    for i in w: b.append(not i)
    return b

def op_and(w,x):
    b = []
    for i in range(16): b.append(True if w[i]==x[i]==True else False)
    return b

def op_or(w,x):
    b = []
    for i in range(16): b.append(True if w[i] or x[i] else False)
    return b

def op_lshift(w,s):
    b = w[s:]
    for i in range(s): b.append(False)
    return b

def op_rshift(w,s):
    b = w[:16-s]
    for i in range(s): b.insert(0, False)
    return(b)

todo = [] 
wires = { 'b':tobool(956) }
shadow = {}
wire0 = [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]

with open('input') as file:
    doing = file.readlines()
    while doing:
        print("New round")
        for line in doing:
            #print(line)
            call, wire = line.rstrip().split(' -> ')
            if 'AND' in call:
                w1, op, w2 = call.split()
                if w1[0].isalpha():
                    try: o1 = wires[w1]
                    except:
                        todo.append(line)
                        continue
                else: o1 = tobool(int(w1))
                if w2[0].isalpha():
                    try: o2 = wires[w2]
                    except:
                        todo.append(line)
                        continue
                else: o2 = tobool(int(w2))
                wires[wire] = op_and(copy(o1), copy(o2))
            elif 'OR' in call:
                w1, op, w2 = call.split()
                if w1[0].isalpha():
                    try: o1 = wires[w1]
                    except:
                        todo.append(line)
                        continue
                else: o1 = tobool(int(w1))
                if w2[0].isalpha():
                    try: o2 = wires[w2]
                    except:
                        todo.append(line)
                        continue
                else: o2 = tobool(int(w2))
                wires[wire] = op_or(copy(o1), copy(o2))
            elif 'LSHIFT' in call:
                w1, op, w2 = call.split()
                if w1[0].isalpha():
                    try: o1 = wires[w1]
                    except:
                        todo.append(line)
                        continue
                else: o1 = tobool(int(w1))
                wires[wire] = op_lshift(copy(o1), int(w2))
            elif 'RSHIFT' in call:
                w1, op, w2 = call.split()
                if w1[0].isalpha():
                    try: o1 = wires[w1]
                    except:
                        todo.append(line)
                        continue
                else: o1 = tobool(int(w1))
                wires[wire] = op_rshift(copy(o1), int(w2))
            elif 'NOT' in call:
                op, w1 = call.split()
                if w1[0].isalpha():
                    try:  o1 = wires[w1]
                    except:
                        todo.append(line)
                        continue
                else: o1 = tobool(int(w1))
                wires[wire] = op_not(copy(o1))
            else: # wire gets value
                if call.isalpha():
                    try: o1 = wires[call]
                    except:
                        todo.append(line)
                        continue
                else: 
                    o1 = tobool(int(call))
                    if wire == 'b': o1 = tobool(956)
                wires[wire] = copy(o1)
        doing = copy(todo)
        #print(doing)
        todo = []
            
for wire in wires:
    print(wire, toint(wires[wire]))

print(toint(wires['a']))

# pt1: (first try)
# 956 
#
# pt2:
# 33706 is too low.
# 40149  -- yes. needed to keep b constant.
