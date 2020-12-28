# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 07:40:56 2020

@author: Piotr.Idzik and Maria Paszkiewicz
Puzzle 25 from https://adventofcode.com/2020/day/25

The handshake used by the card and the door involves an operation that transforms
a subject number. To transform a subject number, start with the value 1. Then,
a number of times called the loop size, perform the following steps:

Set the value to itself multiplied by the subject number.
Set the value to the remainder after dividing the value by 20201227.
The card always uses a specific, secret loop size when it transforms a subject
number. The door always uses a different, secret loop size.

The cryptographic handshake works like this:
- The card transforms the subject number of 7 according to the card's secret loop
  size. The result is called the card's public key.
- The door transforms the subject number of 7 according to the door's secret loop
  size. The result is called the door's public key.
- The card and door use the wireless RFID signal to transmit the two public keys
  (your puzzle input) to the other device. Now, the card has the door's public key,
  and the door has the card's public key. Because you can eavesdrop on the signal,
  you have both public keys, but neither device's loop size.
- The card transforms the subject number of the door's public key according to
  the card's loop size. The result is the encryption key.
- The door transforms the subject number of the card's public key according to
  the door's loop size. The result is the same encryption key as the card calculated.

At this point, you can use either device's loop size with the other device's public
key to calculate the encryption key. Transforming the subject number of 17807724
(the door's public key) with a loop size of 8 (the card's loop size) produces the
encryption key, 14897079. (Transforming the subject number of 5764801 (the card's
public key) with a loop size of 11 (the door's loop size) produces the same
encryption key: 14897079.)

What encryption key is the handshake trying to establish?
"""

def find_loop_num(in_value):
    cur_value = 1
    cur_loop_num = 0
    while cur_value != in_value:
        cur_value *= 7
        cur_value %= 20201227
        cur_loop_num += 1
    return cur_loop_num

def produce_key(in_loop_num, in_subject_num):
    cur_value = 1
    for _ in range(in_loop_num):
        cur_value *= in_subject_num
        cur_value %= 20201227
    return cur_value

def solve_1(key_a, key_b):
    loop_a = find_loop_num(key_a)
    loop_b = find_loop_num(key_b)
    res_a = produce_key(loop_a, key_b)
    res_b = produce_key(loop_b, key_a)
    assert res_a == res_b
    return res_a

def get_data_p():
    return 10943862, 12721030

def get_data_m():
    return 5099500, 7648211

assert find_loop_num(5764801) == 8
assert find_loop_num(17807724) == 11

assert produce_key(find_loop_num(5764801), 17807724) == 14897079
assert produce_key(find_loop_num(17807724), 5764801) == 14897079

assert solve_1(*get_data_m()) == 11288669
assert solve_1(*get_data_p()) == 5025281

print(solve_1(*get_data_m()))
