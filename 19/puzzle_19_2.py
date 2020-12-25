# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:40:02 2020

@author: Marysia (thanks to help of Piotr Idzik)
Puzzle 19 part 2 from https://adventofcode.com/2020/day/19

As you look over the list of messages, you realize your matching rules aren't
 quite right. To fix them, completely replace rules 8: 42 and 11: 42 31 with the following:

8: 42 | 42 8
11: 42 31 | 42 11 31

After updating rules 8 and 11, how many messages completely match rule 0?
"""

def get_data():
    with open('input.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')

def check_message(in_mes, in_rules):
    '''
    check message
    '''
    def proc_str_list(in_str_list, in_rule_key):
        '''
        calls check_single_rule for elements from list of strings in_str_list
        '''
        res_list = []
        for cur_str in in_str_list:
            cur_res = check_single_rule(cur_str, in_rule_key)
            for _ in cur_res:
                if _[1] == 'pass':
                    res_list += [_]
        return res_list
    def check_single_list(in_string, key_list):
        '''
        check if all from list is valid [ 1, 2, 3] (key list is a list of integers)
        '''
        cur_string_list = [in_string]
        for cur_key in key_list:
            kutas = proc_str_list(cur_string_list, cur_key)
            cur_string_list = [_[0] for _ in kutas if _[1] == 'pass']
        kutas = [_ for _ in kutas if _[1] == 'pass']
        return kutas
    def check_single_rule(in_string, rule_key):
        '''
        check single rule (the rule_key)
        '''
        cur_rule = in_rules[rule_key]
        if isinstance(cur_rule, str):
            if len(in_string) > 0 and in_string[0] == cur_rule:
                return [[in_string[1:], 'pass']]
            return [['', 'fail']]
        result_list = []
        for lst in cur_rule:
            kutas = check_single_list(in_string, lst)
            result_list += kutas
        return result_list
    result = check_single_rule(in_mes, 0)
    return ['', 'pass'] in result

INPUT = get_data()

RULES = [_+ ' ' for _ in INPUT[0:INPUT.index('')]]
rules_dict = {int(_[:_.index(':')]) : _[_.index(':')+2:].split(' ') \
              for _ in INPUT[0:INPUT.index('')]}
rules_dict[8] = ['42', '|', '42', '8']
rules_dict[11] = ['42', '31', '|', '42', '11', '31']

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
