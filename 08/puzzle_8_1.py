# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 06:05:26 2020

@author: Marysia
Puzzle 8 part 1 from https://adventofcode.com/2020/day/8

The boot code is represented as a text file with one instruction per line of
text. Each instruction consists of an operation (acc, jmp, or nop) and an
argument (a signed number like +4 or -20).

acc - increases or decreases a single global value called the accumulator by the
value given in the argument. For example, acc +7 would increase the accumulator
by 7. The accumulator starts at 0. After an acc instruction, the instruction
immediately below it is executed next.
jmp - jumps to a new instruction relative to itself. The next instruction to
execute is found using the argument as an offset from the jmp instruction;
for example, jmp +2 would skip the next instruction, jmp +1 would continue
to the instruction immediately below it, and jmp -20 would cause the instruction
20 lines above to be executed next.
nop - stands for No OPeration - it does nothing. The instruction immediately
below it is executed next.

Run your copy of the boot code. Immediately before any instruction is executed
a second time, what value is in the accumulator?
"""

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

FLAG = [0]*len(INPUT)
i = 0
ACC = 0
while not FLAG[i]:
    if INPUT[i][0:3] == 'nop':
        FLAG[i] = 1
        i += 1
    elif INPUT[i][0:3] == 'acc':
        FLAG[i] = 1
        ACC += int(INPUT[i][4:])
        i += 1
    elif INPUT[i][0:3] == 'jmp':
        FLAG[i] = 1
        i += int(INPUT[i][4:])
    else:
        print("Wrong command. Exit.")
        break

print("The value in the accumulator is {}.".format(ACC))
