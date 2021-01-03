# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 10:13:01 2020

@author: Marysia (after an advice of Piotr to use a dictionary)
Puzzle 23 part 2 from https://adventofcode.com/2020/day/23

Determine which two cups will end up immediately clockwise of cup 1. What do
you get if you multiply their labels together?
"""

def play_the_game(with_bitch, num_times, that_long):
    '''
    Returns the next two numbers after label 1, after num_times turns.
    with_buth - input initial string of labels
    that_long - the number of cups in game
    '''
    label_dict = {int(with_bitch[i]):int(with_bitch[(i+1)%len(with_bitch)]) \
                  for i in range(len(with_bitch))}
    for _ in range(len(with_bitch), that_long):
        label_dict[_] = _+1
    if that_long > len(with_bitch):
        label_dict[that_long] = int(with_bitch[0])
    move = 0
    min_val = min(label_dict.keys())
    max_val = max(label_dict.keys())
    current_cup = int(with_bitch[0])
    while move < num_times:
        key1 = label_dict[current_cup]
        key2 = label_dict[key1]
        key3 = label_dict[key2]
        label_dict[current_cup] = label_dict[key3]
        for key in [key1, key2, key3]:
            del label_dict[key]
        dest_cup = current_cup-1
        while not dest_cup in label_dict:
            dest_cup -= 1
            if dest_cup < min_val:
                dest_cup = max_val
        tmp = label_dict[dest_cup]
        label_dict[dest_cup] = key1
        label_dict[key1] = key2
        label_dict[key2] = key3
        label_dict[key3] = tmp

        current_cup = label_dict[current_cup]
        move += 1

    return label_dict[1], label_dict[label_dict[1]]

INPUT = '463528179'
#INPUT = '389125467'

LEN = 10**6
LABEL_1, LABEL_2 = play_the_game(INPUT, 10**7, LEN)
print(LABEL_1 * LABEL_2)
