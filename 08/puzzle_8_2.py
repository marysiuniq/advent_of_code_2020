# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 06:46:06 2020

@author: Marysia

Puzzle 8 part 2 from https://adventofcode.com/2020/day/8

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

Fix the program so that it terminates normally by changing exactly one
jmp (to nop) or nop (to jmp). What is the value of the accumulator after the
program terminates?
"""

def check_commands(input_data, ind):
    '''
    Goes through the commands.
    '''
    flag = [0]*len(input_data)
    acc = 0
    ind_nop = []
    ind_jmp = []
    commands = []
    while ind < len(input_data) and not flag[ind]:
        if input_data[ind][0:3] == 'nop':
            ind_nop += [ind]
            flag[ind] = 1
            commands += [input_data[ind]]
            ind += 1
        elif input_data[ind][0:3] == 'acc':
            flag[ind] = 1
            commands += [input_data[ind]]
            acc += int(input_data[ind][4:])
            ind += 1
        elif input_data[ind][0:3] == 'jmp':
            ind_jmp += [ind]
            flag[ind] = 1
            commands += [input_data[ind]]
            if int(input_data[ind][4:]) == 0:
                ind += 1
            else:
                ind += int(input_data[ind][4:])
        else:
            print("Wrong command. Exit.")
            break
    return commands, ind, acc, flag, ind_nop, ind_jmp

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

i = 0
COMMANDS, i, ACC, FLAG, IND_NOP, IND_JMP = check_commands(INPUT, i)

for i_nop in IND_NOP:
    temp_entry = INPUT[i_nop]
    INPUT[i_nop] = INPUT[i_nop].replace('nop', 'jmp')
    i = 0
    COMMANDS, i, ACC, FLAG, _, _ = check_commands(INPUT, i)
    if i == len(INPUT)-1:
        print('index {} changed from nop to jmp.'.format(i_nop))
        break
    INPUT[i_nop] = temp_entry

for i_jmp in IND_JMP:
    temp_entry = INPUT[i_jmp]
    INPUT[i_jmp] = INPUT[i_jmp].replace('jmp', 'nop')
    i = 0
    COMMANDS, i, ACC, FLAG, _, _ = check_commands(INPUT, i)
    if i == len(INPUT):
        print('index {} changed from jmp to nop.'.format(i_jmp))
        break
    INPUT[i_jmp] = temp_entry

print("The value in the accumulator is {}.".format(ACC))
