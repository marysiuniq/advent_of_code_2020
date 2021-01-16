# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 05:51:05 2020

@author: Marysia

Puzzle 11 part 2 from https://adventofcode.com/2020/day/11
--- Day 11: Seating System ---
Now, instead of considering just the eight immediately adjacent seats, consider
the first seat in each of those eight directions.
It now takes five or more visible occupied seats for an occupied seat to become empty.
"""

import itertools

def sum_arround_occupied(i_seat, j_seat, whole_table):
    '''
    Returns the sum of visible occupied sits arround whole_table[i_seat][j_seat]
    '''
    suma = 0
    for case in POSITIONS_TO_CHECK:
        r_seat = i_seat + case[0]
        c_seat = j_seat + case[1]
        while whole_table[r_seat][c_seat] == '.':
            r_seat += case[0]
            c_seat += case[1]
        if whole_table[r_seat][c_seat] == '#':
            suma += 1
    return suma

def check_seats_arround_empty(i_seat, j_seat, whole_table):
    '''
    Checks if any visible seat is occupied.
    '''
    for case in POSITIONS_TO_CHECK:
        r_seat = i_seat + case[0]
        c_seat = j_seat + case[1]
        while whole_table[r_seat][c_seat] == '.':
            r_seat += case[0]
            c_seat += case[1]
        if whole_table[r_seat][c_seat] == '#':
            return 0
    return 1


def check_seat(seat_check, i_seat, j_seat, whole_table, rule_number):
    '''
    Changes the seat state if applicable.
    '''
    if seat_check == 'L' and check_seats_arround_empty(i_seat, j_seat, whole_table):
        return '#'
    if seat_check == '#' and sum_arround_occupied(i_seat, j_seat, whole_table) >= rule_number:
        return 'L'
    return seat_check

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [list(x.strip()) for x in INPUT]
INPUT = [['L']+_+['L'] for  _ in INPUT]
EMPTY_ROW = ['L']*len(INPUT[0])
INPUT = [EMPTY_ROW] + INPUT + [EMPTY_ROW]
POSITIONS_TO_CHECK = [p for p in itertools.product([1, 0, -1], repeat=2)]
POSITIONS_TO_CHECK.remove(POSITIONS_TO_CHECK[POSITIONS_TO_CHECK.index((0, 0))])

TMP = [x[:] for x in INPUT]

RULE_NUMBER = 5

CHANGED = 1
while CHANGED:
    COUNTER = 0
    CHANGED = 0
    for i, row in enumerate(INPUT[1:-1]):
        for j, seat in enumerate(row[1:-1]):
            TMP[i+1][j+1] = check_seat(seat, i+1, j+1, INPUT, RULE_NUMBER)
            if TMP[i+1][j+1] == '#':
                COUNTER += 1
            if not TMP[i+1][j+1] == INPUT[i+1][j+1]:
                CHANGED = 1
    INPUT = [x[:] for x in TMP]

print("The number of occupied seats is {}.".format(COUNTER))
