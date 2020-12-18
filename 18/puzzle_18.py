# -*- coding: utf-8 -*-0
"""
Created on Fri Dec 18 05:47:36 2020

@author: Piotr.Idzik and Maria Paszkiewicz
Puzzle 18 from https://adventofcode.com/2020/day/18

Part 1:
Rather than evaluating multiplication before addition, the operators have the
same precedence, and are evaluated left-to-right regardless of the order in which
they appear.

Part 2:
Now, addition and multiplication have different precedence levels, but they're not
the ones you're familiar with. Instead, addition is evaluated before multiplication.

Before you can help with the homework, you need to understand it yourself.
Evaluate the expression on each line of the homework; what is the sum of the
resulting values?
"""

def get_data():
    with open('input.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')

def get_val(in_str):
    def is_number(in_str):
        res = True
        try:
            int(in_str)
        except ValueError:
            res = False
        return res
    piece_list = in_str.split(' ')
    res_val = 0
    op_dict = {'+': lambda a, b: a+b, '*': lambda a, b: a*b}
    cur_val = None
    cur_op = None
    res_val = None
    piece_num = 0
    while piece_num < len(piece_list):
        cur_piece = piece_list[piece_num]
        if is_number(cur_piece):
            cur_val = int(cur_piece)
            piece_num += 1
        elif cur_piece in op_dict:
            cur_op = op_dict[cur_piece]
            piece_num += 1
        elif cur_piece[0] == '(':
            tmp_piece_num = piece_num
            tmp_count = 0
            while tmp_piece_num < len(piece_list):
                tmp_count += piece_list[tmp_piece_num].count('(')
                tmp_count -= piece_list[tmp_piece_num].count(')')
                if ')' in piece_list[tmp_piece_num]:
                    if tmp_count == 0:
                        break
                tmp_piece_num += 1
            assert tmp_piece_num < len(piece_list)
            tmp_str = ' '.join(piece_list[piece_num:tmp_piece_num+1])
            cur_val = get_val(tmp_str[1:-1])
            piece_num = tmp_piece_num+1
        if cur_val and cur_op:
            res_val = cur_op(res_val, cur_val)
            cur_op = None
            cur_val = None
        elif cur_val and not res_val and not cur_op:
            res_val = cur_val
            cur_val = None
    return res_val

def get_val_2(in_str):
    piece_list = in_str.split(' ')
    for cur_piece_num in range(1, len(piece_list)-1):
        if '+' in piece_list[cur_piece_num]:
            piece_list[cur_piece_num-1] = '(' + piece_list[cur_piece_num-1]
            piece_list[cur_piece_num+1] = piece_list[cur_piece_num+1] + ')'
    tmp_str = ' '.join(piece_list)
    return eval(tmp_str)

assert get_val('5 + 6') == 11
assert get_val('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert get_val('2 * 3 + (4 * 5)') == 26
assert get_val('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632
assert get_val_2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

# Part 1
RES1 = sum(get_val(_) for _ in get_data())
print(RES1)

# Part 2
RES2 = sum(get_val_2(_) for _ in get_data())
print(RES2)
