# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 05:50:55 2020

@author: Marysia

Puzzle 11 part 1 from https://adventofcode.com/2020/day/11
--- Day 11: Seating System ---
Now, you just need to model the people who will be arriving shortly. Fortunately,
people are entirely predictable and always follow a simple set of rules. All
decisions are based on the number of occupied seats adjacent to a given seat (one
of the eight positions immediately up, down, left, right, or diagonal from the seat).
The following rules are applied to every seat simultaneously:
- If a seat is empty (L) and there are no occupied seats adjacent to it, the seat
  becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also occupied,
  the seat becomes empty.
- Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

Simulate your seating area by applying the seating rules repeatedly until no seats
change state. How many seats end up occupied?
"""
def check_sum_arround_occupied(seats, rule):
    '''
    1 indicates the change of state
    0 indicates no change of state
    '''
    suma = 0
    for line in seats:
        for char in line:
            if char == '#':
                suma += 1
        if suma > rule:
            return 1
    return 0

def check_seats_arround_empty(seats):
    '''
    Checks if any visible seat is occupied.
    '''
    for line in seats:
        for char in line:
            if char == '#':
                return 0
    return 1

def check_seat(seat_check, window_seat, rule_number):
    '''
    Changes the seat state if applicable.
    '''
    if seat_check == 'L' and check_seats_arround_empty(window_seat):
        return '#'
    if seat_check == '#' and check_sum_arround_occupied(window_seat, rule_number):
        return 'L'
    return seat_check

with open('input.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [list(x.strip()) for x in INPUT]

TMP = [x[:] for x in INPUT]

RULE_NUMBER = 4

CHANGED = 1
while CHANGED:
    COUNTER = 0
    CHANGED = 0
    for i, row in enumerate(INPUT):
        for j, seat in enumerate(row):
            if 0 < i < (len(INPUT)-1) and 0 < j < (len(row)-1):
                window = [line[j-1:j+2] for line in INPUT[i-1:i+2]]
                TMP[i][j] = check_seat(seat, window, RULE_NUMBER)
            elif j == 0:
                window = [line[j:j+2] for line in INPUT[i-1:i+2]]
                TMP[i][j] = check_seat(seat, window, RULE_NUMBER)
            elif j == len(row)-1:
                window = [line[j-1:j+1] for line in INPUT[i-1:i+2]]
                TMP[i][j] = check_seat(seat, window, RULE_NUMBER)
            elif i == 0:
                window = [line[j-1:j+2] for line in INPUT[i:i+2]]
                TMP[i][j] = check_seat(seat, window, RULE_NUMBER)
            elif i == len(INPUT)-1:
                window = [line[j-1:j+2] for line in INPUT[i-1:i+1]]
                TMP[i][j] = check_seat(seat, window, RULE_NUMBER)
            if TMP[i][j] == '#':
                COUNTER += 1
            if not TMP[i][j] == INPUT[i][j]:
                CHANGED = 1
    INPUT = [x[:] for x in TMP]

print("The number of occupied seats is {}.".format(COUNTER))
