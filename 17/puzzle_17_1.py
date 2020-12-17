# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 05:53:52 2020

@author: Marysia
Puzzle 17 part 1 from https://adventofcode.com/2020/day/17

The pocket dimension contains an infinite 3-dimensional grid. At every integer
3-dimensional coordinate (x,y,z), there exists a single cube which is either
active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive.
The only exception to this is a small flat region of cubes (your puzzle input);
the cubes in this region start in the specified active (#) or inactive (.) state.
During a cycle, all cubes simultaneously change their state according to the
following rules:

- If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube
remains active. Otherwise, the cube becomes inactive.
- If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes
active. Otherwise, the cube remains inactive.

Starting with your given initial configuration, simulate six cycles. How many
cubes are left in the active state after the sixth cycle?
"""
import itertools
from copy import copy
import numpy as np

def split(word):
    '''
    Splits string into list of chars.
    '''
    return [char for char in word]

def check_neighbours(cube_in, _i, _j, _k):
    '''
    Checks the sum of neighbour's values.
    '''
    suma = 0
    for case in POSITIONS_TO_CHECK:
        suma += cube_in[_i+case[0], _j+case[1], _k+case[2]]
    return suma

with open('test.txt', 'r') as file:
    INPUT = file.readlines()

INPUT = [split(x.strip()) for x in INPUT]
INPUT = np.array(INPUT) # convert to array
INPUT = np.where(INPUT == '#', 1, INPUT) # convert '#' to 1
INPUT = np.where(INPUT == '.', 0, INPUT) # convert '.' to 0
DIM_INPUT = len(INPUT[0, :])

MAX_CYCLE = 6

POSITIONS_TO_CHECK = [p for p in itertools.product([1, 0, -1], repeat=3)]
POSITIONS_TO_CHECK.remove(POSITIONS_TO_CHECK[POSITIONS_TO_CHECK.index((0, 0, 0))])

N = DIM_INPUT+2+MAX_CYCLE*2 + DIM_INPUT % 2 + 1 # 27 minimum dimension of final cube
cube = np.array([[[0 for k in range(N)] for j in range(N)] for i in range(N)])

# the middle of a grid has the coordinates [5][5][5]=[n_mid][n_mid][n_mid] n_mid=(n-1)/2
N_MID = int((N-1)/2)
DIM1 = N_MID - int(len(INPUT[0, :])/2)
DIM2 = N_MID + int(len(INPUT[0, :])/2) + DIM_INPUT % 2

cube[DIM1:DIM2, DIM1:DIM2, N_MID] = INPUT
cube_tmp = copy(cube)

cycle = 0
while cycle < MAX_CYCLE:
    # screw the beauty
    for i in range(DIM1-1-cycle, DIM2+cycle+1):
        for j in range(DIM1-1-cycle, DIM2+cycle+1):
            for k in range(N_MID-1-cycle, N_MID+2+cycle):
                number_of_active = check_neighbours(cube, i, j, k)
                if cube[i, j, k] == 1 and number_of_active not in (2, 3):
                    cube_tmp[i, j, k] = 0
                elif cube[i, j, k] == 0 and number_of_active == 3:
                    cube_tmp[i, j, k] = 1
    cube = copy(cube_tmp)
    cycle += 1

SUM = 0
for i in range(0, N):
    for j in range(0, N):
        for k in range(0, N):
            SUM += cube[i, j, k]

print(SUM)
