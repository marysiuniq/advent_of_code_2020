# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 06:26:38 2020

@author: Marysia
Puzzle 23 part 1 from https://adventofcode.com/2020/day/23

Using your labeling, simulate 100 moves. What are the labels on the cups after
cup 1?
"""

def split(word):
    '''
    Splits string into list of chars.
    '''
    return [int(char) for char in word]

def destination_cup(in_lst, cup):
    '''
    Finds the index of destination cup in in_lst, for current cup cup.
    '''
    def is_in_list(in_lst, cup):
        res = True
        try:
            in_lst.index(cup-1)
        except ValueError:
            res = False
        return res
    if is_in_list(in_lst, cup):
        return in_lst.index(cup-1)
    if cup == min(in_lst):
        cup = max(in_lst)
        return destination_cup(in_lst, cup+1)
    return destination_cup(in_lst, cup-1)

INPUT = split('463528179')
#INPUT = split('389125467')


move = 1
MOVES = 100
LEN = len(INPUT)
print('move ' + str(move))
print('cups: {}'.format(INPUT))
current_cup_ind = 0
current_cup = INPUT[current_cup_ind]
print('current cup: {}'.format(current_cup))
pick_up_len = 3
pick_up = INPUT[current_cup_ind+1:current_cup_ind+pick_up_len+1]
print('pick up: {}'.format(pick_up))
del INPUT[current_cup_ind+1:current_cup_ind+pick_up_len+1]
while move < MOVES+1:
    destination_ind = destination_cup(INPUT, current_cup)
    print('destination: {}'.format(INPUT[destination_ind]))
    if destination_ind < len(INPUT)-1:
        INPUT = INPUT[0:destination_ind+1] + pick_up + INPUT[destination_ind+1:]
    else:
        INPUT += pick_up
    shifted_current_cup_ind = INPUT.index(current_cup)
    difference = shifted_current_cup_ind - current_cup_ind
    if difference:
        INPUT += INPUT[0:difference]
        del INPUT[0:difference]
    current_cup_ind = (current_cup_ind + 1) % LEN
    current_cup = INPUT[current_cup_ind]
    print('move ' + str(move+1))
    print('current cup: {}'.format(current_cup))
    print('cups: {}'.format(INPUT))
    if move == MOVES:
        break
    if current_cup_ind < LEN-pick_up_len-1:
        pick_up = INPUT[current_cup_ind+1:current_cup_ind+pick_up_len+1]
        del INPUT[current_cup_ind+1:current_cup_ind+pick_up_len+1]
    else:
        pick_up = INPUT[current_cup_ind+1:] + INPUT[0:(current_cup_ind+pick_up_len+1)%LEN]
        del INPUT[current_cup_ind+1:]
        del INPUT[0:(current_cup_ind+pick_up_len+1)%LEN]
    move += 1
    print('pick up: {}'.format(pick_up))


print(INPUT)
RESULT = ''.join(str(_) for _ in INPUT)
print('The answer is: {}{}'.format(RESULT[RESULT.find('1')+1:], RESULT[0:RESULT.find('1')]))
