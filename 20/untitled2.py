# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 15:32:36 2020

@author: Marysia
"""

def find_matching_edges_straight(in_dictionary):
    pairs = []
    for key, value in sorted(in_dictionary.items()):
        for key1, value1 in sorted(in_dictionary.items()):
            if key1 > key:
                for edge in value:
                    if key != key1 and edge in value1:
                        pairs += [key, value.index(edge), key1, value1.index(edge)]
        #del in_dictionary[key]
    return pairs

def find_matching_edges_reversed(in_dictionary, dict_rev):
    pairs = []
    for key, value in sorted(in_dictionary.items()):
        for key1, value1 in sorted(dict_rev.items()):
            if key1 > key:
                for edge in value:
                    if key != key1 and edge in value1:
                        pairs += [key, value.index(edge), key1, value1.index(edge)]
        #del in_dictionary[key]
    return pairs

INPUT = get_data()

TILE_SIZE = len(INPUT[1])
str_start = 5
#dictionary = {int(INPUT[_][str_start:-1]):
#                            {1:''.join([i[-1] for i in INPUT[_+1:_+TILE_SIZE+1]]), 
#                             2:INPUT[_+1], 
#                             3:''.join([j[0] for j in INPUT[_+1:_+TILE_SIZE+1]]), 
#                             4:INPUT[_+TILE_SIZE]} 
#              for _ in range(0,len(INPUT),TILE_SIZE+2)}
dictionary = {int(INPUT[_][str_start:-1]):
                            [''.join([i[-1] for i in INPUT[_+1:_+TILE_SIZE+1]]), 
                             INPUT[_+1], 
                             ''.join([j[0] for j in INPUT[_+1:_+TILE_SIZE+1]]), 
                             INPUT[_+TILE_SIZE]] 
              for _ in range(0,len(INPUT),TILE_SIZE+2)}
dictionary_reversed = {int(INPUT[_][str_start:-1]):
                            [''.join([i[-1] for i in INPUT[_+1:_+TILE_SIZE+1]])[::-1], 
                             INPUT[_+1][::-1], 
                             ''.join([j[0] for j in INPUT[_+1:_+TILE_SIZE+1]])[::-1], 
                             INPUT[_+TILE_SIZE][::-1]] 
              for _ in range(0,len(INPUT),TILE_SIZE+2)}
#dictionary = {int(INPUT[_][str_start:-1]):np.array(INPUT[_+1:_+TILE_SIZE+1]) for _ in range(0,len(INPUT),TILE_SIZE+2)}
pairs_straight = find_matching_edges_straight(dictionary)
pairs_mixed = find_matching_edges_reversed(dictionary, dictionary_reversed)