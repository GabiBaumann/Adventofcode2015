#!/usr/bin/env python
# SPDX-License-Identifier: GPL-3.0-only

"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?
Your puzzle answer was 377891.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""

from copy import copy

out = brightness = 0
light = []
line = []
hue = []
ints = []
for x in range(1000): 
    line.append(False)
    ints.append(0)
for x in range(1000): 
    light.append(copy(line))
    hue.append(copy(ints))

with open('input') as file:
    for line in file:
        cmd, x0, y0, x1, y1 = line.replace('turn ', '').replace('through ', '').replace(',', ' ').split()
        for y in range(int(y0), int(y1)+1):
            for x in range(int(x0), int(x1)+1):
                if cmd == 'off': 
                    light[y][x] = False
                    hue[y][x] = max(0, hue[y][x]-1)
                elif cmd == 'on': 
                    light[y][x] = True
                    hue[y][x] += 1
                else: 
                    light[y][x] = not light[y][x]
                    hue[y][x] += 2

for y in range(1000):
    for x in range(1000):
        if light[y][x]: out += 1
        brightness += hue[y][x]

print(out, brightness)

# part1: first try!
# 377891
#
# part2: first try!
# 14110788
