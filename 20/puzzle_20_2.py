# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 18:07:50 2020

@author: Marysia (thanks to help of Piotr Idzik)
Puzzle 20 part 2 from https://adventofcode.com/2020/day/20

How many # are not part of a sea monster?
"""

from copy import deepcopy

def get_data():
    '''
    Loads the data from input.txt.
    '''
    with open('input.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str

def split(word):
    '''
    Splits string into list of chars.
    '''
    return [char for char in word]


def get_result():
    '''
    Gets copied result FIELD_DICT from part 1.
    '''
    return {(0, 0): (3779, ''), (1, 0): (2521, 'h'), (2, 0): (2239, 'rr'),
            (3, 0): (1093, 'h'), (4, 0): (3547, 'rh'), (5, 0): (1777, 'rh'),
            (6, 0): (2441, ''), (7, 0): (3191, ''), (8, 0): (2857, 'hr'),
            (9, 0): (1889, 'rh'), (10, 0): (1289, 'rrr'), (11, 0): (3329, 'rr'),
            (0, 1): (3541, ''), (1, 1): (3833, 'h'), (2, 1): (1489, 'rh'),
            (3, 1): (2179, ''), (4, 1): (1583, 'rh'), (5, 1): (2207, 'rh'),
            (6, 1): (2143, 'r'), (7, 1): (3793, 'r'), (8, 1): (1867, 'rh'),
            (9, 1): (2927, 'hr'), (10, 1): (3001, 'rrr'), (11, 1): (3853, 'h'),
            (0, 2): (2551, 'rh'), (1, 2): (3701, 'rh'), (2, 2): (2141, 'rrr'),
            (3, 2): (3331, 'hr'), (4, 2): (1423, 'hr'), (5, 2): (3359, 'hr'),
            (6, 2): (1031, ''), (7, 2): (3313, ''), (8, 2): (2633, 'r'),
            (9, 2): (1231, 'rr'), (10, 2): (1171, 'rrr'), (11, 2): (2503, 'r'),
            (0, 3): (1297, 'hr'), (1, 3): (2161, 'rh'), (2, 3): (2593, 'rrr'),
            (3, 3): (2137, 'rr'), (4, 3): (1249, ''), (5, 3): (1163, 'h'),
            (6, 3): (3083, 'rrr'), (7, 3): (3413, 'r'), (8, 3): (3923, 'rh'),
            (9, 3): (3607, 'rr'), (10, 3): (3319, 'hr'), (11, 3): (2351, 'hr'),
            (0, 4): (2843, 'rh'), (1, 4): (3461, 'h'), (2, 4): (1621, 'rr'),
            (3, 4): (2837, 'hr'), (4, 4): (2459, 'rh'), (5, 4): (3727, 'rrr'),
            (6, 4): (3433, 'rrr'), (7, 4): (2131, 'h'), (8, 4): (1433, 'r'),
            (9, 4): (3929, 'hr'), (10, 4): (1493, 'rrr'), (11, 4): (1453, 'rr'),
            (0, 5): (1657, 'rrr'), (1, 5): (1097, 'rh'), (2, 5): (3613, 'h'),
            (3, 5): (2689, 'h'), (4, 5): (1361, 'h'), (5, 5): (1223, 'rh'),
            (6, 5): (2081, 'rh'), (7, 5): (1069, ''), (8, 5): (2063, 'hr'),
            (9, 5): (1283, 'rr'), (10, 5): (1753, 'hr'), (11, 5): (1931, 'r'),
            (0, 6): (3041, 'rr'), (1, 6): (1709, 'rr'), (2, 6): (1307, 'rh'),
            (3, 6): (2389, 'rr'), (4, 6): (1697, 'rr'), (5, 6): (1571, 'rrr'),
            (6, 6): (1567, 'hr'), (7, 6): (2731, ''), (8, 6): (3407, 'rh'),
            (9, 6): (3449, 'r'), (10, 6): (3253, 'h'), (11, 6): (2039, 'hr'),
            (0, 7): (3371, 'r'), (1, 7): (2539, 'rr'), (2, 7): (3049, 'rh'),
            (3, 7): (1277, 'r'), (4, 7): (2053, 'hr'), (5, 7): (2713, 'h'),
            (6, 7): (3463, 'hr'), (7, 7): (3121, 'h'), (8, 7): (3557, 'r'),
            (9, 7): (3947, 'rrr'), (10, 7): (2693, 'rrr'), (11, 7): (1667, 'h'),
            (0, 8): (3631, 'h'), (1, 8): (1987, 'hr'), (2, 8): (1117, 'rh'),
            (3, 8): (2953, 'rr'), (4, 8): (3559, 'rr'), (5, 8): (1811, ''),
            (6, 8): (3593, 'hr'), (7, 8): (1259, 'hr'), (8, 8): (1523, ''),
            (9, 8): (2579, ''), (10, 8): (2089, ''), (11, 8): (1747, 'r'),
            (0, 9): (2221, ''), (1, 9): (3109, ''), (2, 9): (2963, 'h'),
            (3, 9): (1103, 'rh'), (4, 9): (3347, 'hr'), (5, 9): (1907, ''),
            (6, 9): (2909, 'hr'), (7, 9): (1439, 'h'), (8, 9): (1009, ''),
            (9, 9): (2153, 'r'), (10, 9): (3169, 'rr'), (11, 9): (2591, 'rh'),
            (0, 10): (1783, 'r'), (1, 10): (3467, 'rr'), (2, 10): (1327, ''),
            (3, 10): (3943, ''), (4, 10): (3203, 'r'), (5, 10): (3491, 'rh'),
            (6, 10): (3529, ''), (7, 10): (2861, 'hr'), (8, 10): (1559, ''),
            (9, 10): (2287, 'h'), (10, 10): (3673, 'hr'), (11, 10): (1187, 'rrr'),
            (0, 11): (3061, 'rrr'), (1, 11): (2897, 'hr'), (2, 11): (1217, 'hr'),
            (3, 11): (1979, 'hr'), (4, 11): (2003, ''), (5, 11): (3067, 'h'),
            (6, 11): (1237, 'rrr'), (7, 11): (3389, 'r'), (8, 11): (2647, 'h'),
            (9, 11): (1597, 'rrr'), (10, 11): (3761, 'hr'), (11, 11): (2789, 'rh')}

def get_result_test():
    '''
    Gets copied result FIELD_DICT from part 1 for test data.
    '''
    return {(0, 0): (3079, 'r'),
            (1, 0): (2473, 'h'),
            (2, 0): (1171, 'hr'),
            (0, 1): (2311, 'rh'),
            (1, 1): (1427, 'rh'),
            (2, 1): (1489, 'rh'),
            (0, 2): (1951, 'rh'),
            (1, 2): (2729, 'rh'),
            (2, 2): (2971, 'rh')}

def rotate_p(in_data):
    '''
    Rotates the tile clockwise.
    '''
    out_data = [[0 for _ in in_data] for _ in in_data[0]]
    for res_row_num, _ in enumerate(out_data):
        for res_col_num in range(len(out_data[res_row_num])):
            out_data[res_row_num][res_col_num] = \
                in_data[-res_col_num-1][res_row_num]
    return out_data

def rotate(in_data):
    '''
    Rotates the tile counter-clockwise having provided the function for clockwise rotation.
    '''
    return rotate_p(rotate_p(rotate_p(in_data)))

def flip_hor(in_data):
    '''
    Flips the tile horisontaly.
    '''
    result = deepcopy(in_data)
    for i, _ in enumerate(result):
        result[i].reverse()
    return result

#def flip_ver(in_data):
#    result = deepcopy(in_data)
#    result = rotate(result)
#    result = flip_hor(result)
#    return rotate_p(result)

def flip_ver(in_data):
    '''
    Flips the tile vertically.
    '''
    result = []
    for entry in in_data:
        result = [entry] + result
    return result

def make_transform(tile, trans_string):
    '''
    Transforms the tile according to trans_string.
    '''
    transform_dict = {'r': rotate, 'h': flip_hor, 'v': flip_ver}
    cur_tile = deepcopy(tile)
    for _ in trans_string:
        cur_tile = transform_dict[_](cur_tile)
    return cur_tile

def remove_edges(in_tile):
    '''
    Removes edges from in_tile.
    '''
    return [_[1:-1] for _ in in_tile[1:-1]]

def merge_image(in_data):
    '''
    Builds the whole image from tiles in in_data.
    '''
    result = []
    sol_size = int(len(in_data)**0.5)
    for big_row_num in range(sol_size):
        for small_row_num in range(len(in_data[(0, 0)])):
            cur_row = []
            for big_col_num in range(sol_size):
                cur_row += in_data[(big_col_num, big_row_num)][small_row_num]
            result += [cur_row]
    return result

def find_monster(in_image, monster):
    '''
    Checks if the monster pattern is in the image. If so, replaces # with O.
    '''
    size_hor = len(monster[0])
    size_ver = len(monster)
    image_with_monsters = deepcopy(in_image)
    def replace_hash(in_col, in_row, image):
        image_copy = deepcopy(image)
        for in_c in range(in_col, in_col+size_hor):
            for in_r in range(in_row, in_row+size_ver):
                if monster[in_r-in_row][in_c-in_col] == '#':
                    image_copy[in_r][in_c] = 'O'
        return image_copy
    def monster_in_window(in_window, in_monster):
        for in_c in range(len(monster[0])):
            for in_r in range(len(monster)):
                if in_monster[in_r][in_c] == '#':
                    if in_window[in_r][in_c] != in_monster[in_r][in_c]:
                        return False
        return True
    for col in range(0, len(in_image[0])-size_hor+1):
        for row in range(0, len(in_image)-size_ver+1):
            window = [_[col:col+size_hor] for _ in in_image[row:row+size_ver]]
            if monster_in_window(window, monster):
                image_with_monsters = replace_hash(col, row, image_with_monsters)
    return image_with_monsters

def image_to_str(in_image):
    '''
    Converts image from list of lists to string lines.
    '''
    return '\n'.join([''.join(_) for _ in in_image])

def hash_calc(in_image):
    '''
    Computes the number of # in in_image.
    '''
    return image_to_str(in_image).count('#')

MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
MONSTER = [list(_) for _ in MONSTER.split('\n')]

# Create the dictionary with whole tiles {tile_id: [['']]}
DICTIONARY = {}
for cur_piece in get_data().split('\n\n'):
    cur_lines = cur_piece.split('\n')
    cur_key = int(cur_lines[0][5:-1])
    cur_lines = cur_lines[1:]
    DICTIONARY[cur_key] = [list(_) for _ in cur_lines]

# Dictionary with positions and transformations of tiles
# {(column, row): (tile_id, transformations_string)}
FIGURE = get_result()
DICTIONARY_ROTATED_AND_CROPPED = {}

# Create the dictionary with whole tiles {tile_id: [['']]}, which are already
# transformed and with removed edges
for value in FIGURE.values():
    DICTIONARY_ROTATED_AND_CROPPED[value[0]] = \
    (make_transform(remove_edges(DICTIONARY[value[0]]), value[1]))

# Final dictionary of the form {(column, row): [['']]} in which the tiles are
# already transformed and with removed edges.
DICTIONARY_FINAL = {}
for key, value in FIGURE.items():
    DICTIONARY_FINAL[key] = DICTIONARY_ROTATED_AND_CROPPED[value[0]]

# Merged image.
IMAGE = merge_image(DICTIONARY_FINAL)
print(image_to_str(IMAGE))

# Merged image with monsters marked.
IMAGE_WITH_MONSTERS = find_monster(IMAGE, MONSTER)

TRANSFORMATIONS = ['', 'r', 'rr', 'rrr', 'v', 'h', 'rh', 'hr', 'rv', 'hrr', 'hrrr']
# The smallest number is the answer to puzzle 20 part 2.
for _ in TRANSFORMATIONS:
    print(hash_calc(find_monster(make_transform(IMAGE, _), MONSTER)))
