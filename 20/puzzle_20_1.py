# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 06:58:54 2020

@author: Marysia (thanks to help of Piotr Idzik)
Puzzle 20 part 1 from https://adventofcode.com/2020/day/20

--- Day 20: Jurassic Jigsaw ---

A tile edges order is defined as:
   1
  ###
2 ### 0
  ###
   3
   
Assemble the tiles into an image. What do you get if you multiply together
the IDs of the four corner tiles?
"""
from copy import deepcopy

def get_data():
    '''
    Loads the data from input.txt.
    '''
    with open('input.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')

def split(word):
    '''
    Splits string into list of chars.
    '''
    return [char for char in word]

def rotate_90(tile):
    '''
    Assigns the new order of edges as if the tile was rotated.
    '''
    tile_rotated = [[] for _ in range(4)]
    tile_rotated[1] = tile[0]
    tile_rotated[2] = tile[1][::-1]
    tile_rotated[3] = tile[2]
    tile_rotated[0] = tile[3][::-1]
    return tile_rotated

def flip_hor(tile):
    '''
    Assigns the new order of edges as if the tile was flipped horisontally.
    '''
    tile_rotated = [[] for _ in range(4)]
    tile_rotated[1] = tile[1][::-1]
    tile_rotated[2] = tile[0]
    tile_rotated[3] = tile[3][::-1]
    tile_rotated[0] = tile[2]
    return tile_rotated

def flip_ver(tile):
    '''
    Assigns the new order of edges as if the tile was flipped vertically.
    '''
    tile_rotated = [[] for _ in range(4)]
    tile_rotated[1] = tile[3]
    tile_rotated[2] = tile[2][::-1]
    tile_rotated[3] = tile[1]
    tile_rotated[0] = tile[0][::-1]
    return tile_rotated

def make_transform(tile, trans_string):
    '''
    Transforms the tile according to trans_string.
    '''
    transform_dict = {'r': rotate_90, 'h': flip_hor, 'v': flip_ver}
    cur_tile = deepcopy(tile)
    for _ in trans_string:
        cur_tile = transform_dict[_](cur_tile)
    return cur_tile

def check_vertical(tile_up, tile_down):
    '''
    Checks if the bottom edge of tile_up fits the upper edge of tile_down.
    '''
    return tile_up[3] == tile_down[1]

def check_horisontal(tile_left, tile_right):
    '''
    Checks if the right edge of tile_left fits the left edge of tile_right.
    '''
    return tile_left[0] == tile_right[2]

def check_fit(cur_solution, new_tile, position, tiles_dict):
    '''
    Adds a new_tile to the existing cur_solution and checks if it fits after assigned
    transformations.
    cur_solution = {position: [tile number, transformations]}
    new_tile = [tile number, transformations]
    position = [x-direction, y-direction]
    '''
    tile = make_transform(tiles_dict[new_tile[0]], new_tile[1])
    result = True
    if position[0] > 0:
        tile_left = cur_solution[(position[0]-1, position[1])]
        tile_left = make_transform(tiles_dict[tile_left[0]], tile_left[1])
        result = check_horisontal(tile_left, tile)
    if result and position[1] > 0:
        tile_up = cur_solution[(position[0], position[1]-1)]
        tile_up = make_transform(tiles_dict[tile_up[0]], tile_up[1])
        result = check_vertical(tile_up, tile)
    return result

def next_position(pos, sol_size):
    '''
    Checks first coordinate of the position. If it is higher than the grid size,
    the first coordinate is set to zero and second coordinate is increased by one.
    '''
    new_pos = [pos[0] + 1, pos[1]]
    if new_pos[0] >= sol_size:
        new_pos[0] = 0
        new_pos[1] += 1
    return tuple(new_pos)

def find_solution(in_tiles):
    '''
    Adds tiles from in_tiles to the grid one-by-one trying all the transformations
    and checking if the new tile fits to the rest at a given position.
    The result is a dictionary of the form:
    {(column, row): (tile_id, string_with_list_of_transformations)}
    '''
    some_sol = None
    def add_tile(cur_solution, position, tiles_available):
        nonlocal some_sol
        if len(tiles_available) > 0:
            for tile_id in tiles_available:
                transformations = ['', 'r', 'rr', 'rrr', 'v', 'h', 'rh', 'hr']
                for transform in transformations:
                    cur_tile = (tile_id, transform)
                    if some_sol is None and check_fit(cur_solution, cur_tile, position, in_tiles):
                        tmp_solution = deepcopy(cur_solution)
                        tmp_solution[position] = cur_tile
                        tmp_position = next_position(position, int(len(in_tiles)**0.5))
                        add_tile(tmp_solution, tmp_position, tiles_available-{cur_tile[0]})
        else:
            some_sol = cur_solution
    add_tile({}, (0, 0), set(in_tiles.keys()))
    return some_sol

def make_dictionary_of_tile_edges(in_data):
    '''
    The result is the dictionary of the form: {tile_number: [string_for_edge_0,
                                                             string_for_edge_1,
                                                             string_for_edge_2,
                                                             string_for_edge_3]}
    '''
    tile_size = len(in_data[1])
    str_start = 5
    return {int(in_data[_][str_start:-1]): \
                            [''.join([i[-1] for i in in_data[_+1:_+tile_size+1]]),
                             in_data[_+1],
                             ''.join([j[0] for j in in_data[_+1:_+tile_size+1]]),
                             in_data[_+tile_size]]
            for _ in range(0, len(in_data), tile_size+2)}

assert rotate_90(['abcd', 'efgh', 'ijkl', 'mnop']) == ['ponm', 'abcd', 'hgfe', 'ijkl']
assert rotate_90(rotate_90(rotate_90(rotate_90(['...#.##..#', '...#.##..#',
                                                '#..##.#...', '#..##.#...'])))) \
                 == ['...#.##..#', '...#.##..#', '#..##.#...', '#..##.#...']
assert flip_hor(flip_hor(['abcd', 'efgh', 'ijkl', 'mnop'])) == ['abcd', 'efgh', 'ijkl', 'mnop']
assert flip_ver(flip_ver(['abcd', 'efgh', 'ijkl', 'mnop'])) == ['abcd', 'efgh', 'ijkl', 'mnop']

DICTIONARY = make_dictionary_of_tile_edges(get_data())
FIELD_DICT = find_solution(DICTIONARY)
FIELD_SIZE = int(len(DICTIONARY)**0.5)
print(FIELD_DICT[(0, 0)][0]*FIELD_DICT[(0, FIELD_SIZE-1)][0]*FIELD_DICT[(FIELD_SIZE-1, 0)][0]
      *FIELD_DICT[(FIELD_SIZE-1, FIELD_SIZE-1)][0])

# Saving the resulting dictionary, to be used in part 2:
#with open("result1.txt","w") as f:
#    print(field_dict, file=f)
#file1.close() #to change file access modes
