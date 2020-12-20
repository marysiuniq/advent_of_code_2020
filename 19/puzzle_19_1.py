# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 06:00:49 2020

@author: Marysia
"""

def get_data():
    with open('test.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')

def check_rules(the_rules, number, possibilities, index):
    def is_number(in_str):
        res = True
        try:
            int(in_str)
        except ValueError:
            res = False
        return res
    def add_letter(letters, letter):
        return letters + letter
    def add_possibilities(possis, ind):
        possis += [possis[ind]]
        return possis
    #rule_zero = [_ for _ in the_rules if _.startswith(number)]
    #rule_zero = rule_zero[0].split(' ')
    rule_zero = the_rules.split(' ')
    if rule_zero[1] == '"a"':
        possibilities[index] = add_letter(possibilities[index], 'a')
    elif rule_zero[1] == '"b"':
        possibilities[index] = add_letter(possibilities[index], 'b')
    elif '|' in rule_zero:
        add_possibilities(possibilities, index)
        splitter = rule_zero.index('|') - 1
        for i, entry in enumerate(rule_zero[1:]):
            if i < splitter:
                if is_number(entry):
                    possibilities, index = check_rules(the_rules, entry + ':', possibilities, index)
                else:
                    print("Not a number. Wrong rule.")
                    break
            elif i > splitter:
                possibilities, index =  check_rules(the_rules, entry + ':', possibilities, index)
        index += 1
    else:
        for j, jentry in enumerate(rule_zero[1:]):
            if is_number(jentry):
                possibilities, index = check_rules(the_rules, jentry + ':', possibilities, index)
            else:
                print("Not a number. Wrong rule.")
                break

    return possibilities, index
        
#    
#    
#def check_message(input_data):
#    
#    check_rules(input_data)
#

#
#RES1 = sum(check_message(_) for _ in get_data())
#print(RES1)

INPUT = get_data()
#RULE_ZERO = INPUT[:][0].index('0')

#RULES = check_rules(INPUT[0:INPUT.index('')], '0:', [''], 0)
#RULES = [check_rules(line, '0:', [''], line[0:line.index(' ')]) for line in INPUT[0:INPUT.index('')]]

def  find_containing(character, input_arg):
    #letter_a = [_ for _ in INPUT[0:INPUT.index('')] if '"a"' in _][0].split(':')[0]
    return [_ for _ in input_arg if character in _][0].split(':')[0]

def replace_this(letter_a, with_letter, in_rules):
    for i,line in enumerate(in_rules):
        if ' '+letter_a+' ' in line.split(':')[1]:
            line = line.replace(letter_a,with_letter)
        in_rules[i] = line
    return in_rules
#letter_a = [_ for _ in INPUT[0:INPUT.index('')] if '"a"' in _][0].split(':')[0]
#letter_b = [_ for _ in INPUT[0:INPUT.index('')] if '"b"' in _][0].split(':')[0]
RULES = [_+ ' ' for _ in INPUT[0:INPUT.index('')]]
letter_a = find_containing('"a"', RULES)
letter_b = find_containing('"b"', RULES)

for i,line in enumerate(RULES):
    RULES = replace_this(letter_a, 'a', RULES)
    RULES = replace_this(letter_b, 'b', RULES)

finished_set = set('a b |')
done = [letter_a, letter_b]
for i,line in enumerate(RULES):
    number = line.split(':')[0]
    code = line.split(':')[1]
    if  set(code).difference(finished_set) == set() and number not in done:
        RULES = replace_this(number, code, RULES)
        done += [number]
    #elif set(code).difference(finished_set) != set():
        
        
#for _ in INPUT 
