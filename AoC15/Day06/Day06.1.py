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

"""

from copy import deepcopy as cp

for x in range(1000):
    for y in range(1000):
# look up grid init

with open('input') as file:
    for line in file:
        cmd, x0, y0, x1, y1 = line.replace('turn ', '').replace('through ', '').replace(',', ' ').split()
        #print(cmd, x0, y0, x1, y1)
        #x0 = int(x0)
        #x1 = int(x1)
        #y0 = int(y0)
        #y1 = int(y1)
        for x in range(int(x0), int(x1)+1):
            for y in range(int(y0), int(y1)+1):
                if cmd = 'off': light[x][y] = False
                elif cmd = 'on': light[x][y] = True
                else: light[x][y] = not light[x][y]
