# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 05:52:57 2020

@author: Piotr.Idzik and Maria Paszkiewicz
Puzzle 21 part 1 from https://adventofcode.com/2020/day/21

--- Day 21: Allergen Assessment ---
Each allergen is found in exactly one ingredient. Each ingredient contains zero
or one allergen. Allergens aren't always marked; when they're listed (as in
(contains nuts, shellfish) after an ingredients list), the ingredient that contains
each listed allergen will be somewhere in the corresponding ingredients list.
However, even if an allergen isn't listed, the ingredient that contains that
allergen could still be present: maybe they forgot to label it, or maybe it was
labeled in a language you don't know.

Part 1: Determine which ingredients cannot possibly contain any of the allergens
in your list. How many times do any of those ingredients appear?

Part 2: Arrange the ingredients alphabetically by their allergen and separate
them by commas to produce your canonical dangerous ingredient list. (There should
not be any spaces in your canonical dangerous ingredient list.) In the above example,
this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous ingredient
list?

"""

def str_to_data(in_str):
    def proc_line(in_line_str):
        foods_str, allergens_str = in_line_str.split(' (contains ')
        foods = foods_str.split(' ')
        assert allergens_str[-1] == ')'
        allergens_str = allergens_str[:-1]
        allergens = allergens_str.split(', ')
        return foods, allergens
    return [proc_line(_) for _ in in_str.split('\n')]

def get_data():
    with open('input_m.txt', 'r') as in_file:
        data_str = in_file.read()
    return str_to_data(data_str)

def get_test_data():
    cur_str = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
    return str_to_data(cur_str)

def get_allergen_to_intersection(in_data):
    allergen_set = set()
    for _ in in_data:
        allergen_set.update(_[1])
    allergen_to_line = {}
    for (line_num, line_data) in enumerate(in_data):
        for cur_al in line_data[1]:
            if cur_al in allergen_to_line:
                allergen_to_line[cur_al].append(line_num)
            else:
                allergen_to_line[cur_al] = [line_num]
    allergen_to_intersection = {}
    for cur_al in allergen_to_line:
        set_list = []
        for cur_line in allergen_to_line[cur_al]:
            set_list.append(set(in_data[cur_line][0]))
        allergen_to_intersection[cur_al] = set.intersection(*set_list)
    for _ in allergen_to_intersection:
        allergen_to_intersection[_] = list(allergen_to_intersection[_])
    make_remove(allergen_to_intersection)
    return allergen_to_intersection

def make_remove(allergen_to_intersection):
    proc_keys = set()
    while any(len(_) > 1 for _ in allergen_to_intersection.values()):
        cur_keys = set(allergen_to_intersection.keys())-proc_keys
        cur_keys = list(cur_keys)
        cur_keys = sorted(cur_keys, key=lambda x: len(allergen_to_intersection[x]))
        assert len(cur_keys) > 0
        cur_key = list(cur_keys)[0]
        assert len(allergen_to_intersection[cur_key]) == 1
        cur_word = allergen_to_intersection[cur_key][0]
        for _ in allergen_to_intersection:
            if _ != cur_key:
                if cur_word in allergen_to_intersection[_]:
                    allergen_to_intersection[_].remove(cur_word)
        proc_keys.add(cur_key)

def proc_data(in_data):
    allergen_to_intersection = get_allergen_to_intersection(in_data)
    word_set = set()
    for cur_line in in_data:
        cur_word_set = set(cur_line[0])
        word_set.update(cur_word_set)
    for _ in allergen_to_intersection:
        for cur_val in allergen_to_intersection[_]:
            word_set.remove(cur_val)
    res_val = 0
    for cur_line in in_data:
        cur_words = cur_line[0]
        for _ in word_set:
            if _ in cur_words:
                res_val += 1
    return res_val, word_set

def proc_data_2(in_data):
    allergen_to_intersection = get_allergen_to_intersection(in_data)
    word_set = set()
    for cur_line in in_data:
        cur_word_set = set(cur_line[0])
        word_set.update(cur_word_set)
    for _ in allergen_to_intersection:
        for cur_val in allergen_to_intersection[_]:
            if cur_val in word_set:
                word_set.remove(cur_val)
    dan_set = set()
    for cur_line in in_data:
        cur_word_set = set(cur_line[0])
        dan_set.update(cur_word_set)
    tmp_dict = {}
    for _ in allergen_to_intersection:
        for tmp_key in allergen_to_intersection[_]:
            if tmp_key not in tmp_dict:
                tmp_dict[tmp_key] = _
            else:
                tmp_dict[tmp_key] = min([_, tmp_dict[tmp_key]])

    return ','.join(sorted(list(dan_set-word_set), key=lambda x, dict_data=tmp_dict: dict_data[x]))


TEST_RES, TEST_SAFE_ING = proc_data(get_test_data())
assert TEST_RES == 5
assert {'kfcds', 'nhms', 'sbzzf', 'trh'} == TEST_SAFE_ING
RES_1, SAFE_ING = proc_data(get_data())
print(RES_1)
#assert RES_1 == 2262 # for P
assert RES_1 == 1958 # for M
assert proc_data_2(get_test_data()) == 'mxmxvkd,sqjhc,fvjkl'
RES_2 = proc_data_2(get_data())
print(RES_2)
#assert RES_2 == 'cxsvdm,glf,rsbxb,xbnmzr,txdmlzd,vlblq,mtnh,mptbpz' # for P
assert RES_2 == 'xxscc,mjmqst,gzxnc,vvqj,trnnvn,gbcjqbm,dllbjr,nckqzsg' # for M
