# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 07:42:08 2020

@author: Piotr.Idzik and Maria Paszkiewicz
Puzzle 24 from https://adventofcode.com/2020/day/24

--- Day 24: Lobby Layout ---

Part 1: Go through the renovation crew's list and determine which tiles they need
to flip. After all of the instructions have been followed, how many tiles are left
with the black side up?

Part 2: The tile floor in the lobby is meant to be a living art exhibit. Every day,
the tiles are all flipped according to the following rules:

- Any black tile with zero or more than 2 black tiles immediately adjacent to it
  is flipped to white.
- Any white tile with exactly 2 black tiles immediately adjacent to it is flipped
  to black.

Here, tiles immediately adjacent means the six tiles directly touching the tile
in question.

How many tiles will be black after 100 days?
"""
import math

def str_to_list(in_str):
    res_list = []

    def inner(in_str):
        if in_str:
            if in_str[0] in ['w', 'e']:
                res_list.append(in_str[0])
                inner(in_str[1:])
            else:
                assert in_str[0:2] in ['ne', 'nw', 'se', 'sw']
                res_list.append(in_str[0:2])
                inner(in_str[2:])
    inner(in_str)
    return res_list


def single_move(in_pos, in_dir):
    def get_shift(in_angle):
        rad_angle = math.radians(in_angle)
        return [math.cos(rad_angle), math.sin(rad_angle)]
    angle_dict = \
        {'e': 0, 'ne': 60, 'nw': 120, 'w': 180, 'sw': 240, 'se': 300}
    cur_shift = get_shift(angle_dict[in_dir])
    return [a+b for a, b in zip(in_pos, cur_shift)]


def list_to_pos(in_list):
    cur_pos = [0, 0]
    for _ in in_list:
        cur_pos = single_move(cur_pos, _)
    return cur_pos


def pos_to_key(in_pos):
    return tuple([round(2*in_pos[0]), round(2*in_pos[1]/(3**0.5))])


def key_to_pos(in_key):
    return [in_key[0]/2, in_key[1]*3**0.5/2]


def make_flips(in_str_list):
    tiles_dict = {}

    def proc_single_line(in_line_str):
        cur_key = pos_to_key(list_to_pos(str_to_list(in_line_str)))
        if cur_key in tiles_dict:
            if tiles_dict[cur_key] == 'B':
                del tiles_dict[cur_key]
            elif tiles_dict[cur_key] == 'W':
                tiles_dict[cur_key] = 'B'
            else:
                raise ValueError('wtf?!')
        else:
            tiles_dict[cur_key] = 'B'
    for _ in in_str_list:
        proc_single_line(_)
    return tiles_dict


def count_black(in_tiles_dict):
    return sum(1 for _ in in_tiles_dict if in_tiles_dict[_] == 'B')


def solve_1(in_str_list):
    '''
    Part 1
    '''
    return count_black(make_flips(in_str_list))


def get_data_m():
    with open('input_m.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')


def get_data_p():
    with open('input_p.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')


def get_dir_list():
    return ['e', 'ne', 'nw', 'w', 'sw', 'se']


def next_day(in_tiles_data):
    def get_color(in_dict, in_key):
        if in_key in in_dict:
            res = in_dict[in_key]
        else:
            res = 'W'
        return res

    def get_sur(in_key):
        dir_list = get_dir_list()
        in_pos = key_to_pos(in_key)
        res_list = [pos_to_key(single_move(in_pos, _)) for _ in dir_list]
        return res_list

    def count_black_sur(in_key):
        return sum(1 for _ in get_sur(in_key)
                   if get_color(in_tiles_data, _) == 'B')
    active_pos_set = set()
    for _ in in_tiles_data:
        active_pos_set.update(get_sur(_))
        active_pos_set.add(_)
    res_dict = {}
    for _ in active_pos_set:
        black_num = count_black_sur(_)
        if get_color(in_tiles_data, _) == 'B':
            if not (black_num == 0 or black_num > 2):
                res_dict[_] = 'B'
        elif black_num == 2:
            res_dict[_] = 'B'
    return res_dict


def simulate(in_str_list, max_day_num):
    '''
    Part 2
    '''
    tiles_data = make_flips(in_str_list)
    for _ in range(max_day_num):
        tiles_data = next_day(tiles_data)
    return count_black(tiles_data)


assert str_to_list('seswneswswsenwwnwse') == \
    ['se', 'sw', 'ne', 'sw', 'sw', 'se', 'nw', 'w', 'nw', 'se']

TEST_STR = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

assert solve_1(TEST_STR.split('\n')) == 10
assert solve_1(get_data_m()) == 341
assert solve_1(get_data_p()) == 322

assert simulate(TEST_STR.split('\n'), 1) == 15
assert simulate(TEST_STR.split('\n'), 2) == 12
assert simulate(TEST_STR.split('\n'), 10) == 37
assert simulate(TEST_STR.split('\n'), 20) == 132
assert simulate(TEST_STR.split('\n'), 100) == 2208

assert simulate(get_data_p(), 100) == 3831
assert simulate(get_data_m(), 100) == 3700

print(solve_1(get_data_m()))
print(simulate(get_data_m(), 100))
