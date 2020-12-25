# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 08:07:46 2020

@author: Marysia (thanks to help of Piotr Idzik)
Puzzle 19 part 1 from https://adventofcode.com/2020/day/19
--- Day 19: Monster Messages ---

They sent you a list of the rules valid messages should obey and a list of received
messages they've collected so far (your puzzle input).

Your goal is to determine the number of messages that completely match rule 0.
"""

def get_data():
    with open('input.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')

def check_message(in_mes, in_rules):
    '''
    Checks message.
    '''
    def check_single_list(in_string, key_list):
        '''
        check if all from list is valid [ 1, 2, 3] (key list is a list of integers)
        '''
        cur_string = in_string
        cur_result = 'pass'
        for cur_key in key_list:
            cur_string, cur_result = check_single_rule(cur_string, cur_key)
            if cur_result == 'fail':
                return cur_string, cur_result
        return cur_string, cur_result
    def check_single_rule(in_string, rule_key):
        '''
        check single rule (the rule_key)
        '''
        cur_string = in_string
        if isinstance(in_rules[rule_key], str):
            if len(in_string) > 0 and in_string[0] == in_rules[rule_key]:
                return in_string[1:], 'pass'
            return '', 'fail'
        for lst in in_rules[rule_key]:
            cur_string, cur_result = check_single_list(in_string, lst)
            if cur_result == 'pass':
                return cur_string, cur_result
        return '', 'fail'
    result = check_single_rule(in_mes, 0)
    return result[0] == '' and result[1] == 'pass'

INPUT = get_data()

RULES = [_+ ' ' for _ in INPUT[0:INPUT.index('')]]
rules_dict = {int(_[:_.index(':')]) : _[_.index(':')+2:].split(' ') \
              for _ in INPUT[0:INPUT.index('')]}

for key, value in rules_dict.items():
    if '|' in value:
        val1 = value[:value.index('|')]
        val2 = value[value.index('|')+1:]
        rules_dict[key] = [[int(_) for _ in val1], [int(_) for _ in val2]]
    elif value[0].isdigit():
        rules_dict[key] = [[int(_) for _ in value]]
    else:
        rules_dict[key] = value[0].strip('"')

start_entry_ind = INPUT.index('')

SUM = 0
for entry in INPUT[start_entry_ind+1:]:
    if check_message(entry, rules_dict):
        SUM += 1

print(SUM)
