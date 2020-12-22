# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 05:41:38 2020

@author: Marysia
Puzzle 22 part 1 from https://adventofcode.com/2020/day/22
--- Day 22: Crab Combat ---

Before the game starts, split the cards so each player has their own deck (your
puzzle input). Then, the game consists of a series of rounds: both players draw
their top card, and the player with the higher-valued card wins the round. The
winner keeps both cards, placing them on the bottom of their own deck so that
the winner's card is above the other card. If this causes a player to have all
of the cards, they win, and the game ends.

Once the game ends, you can calculate the winning player's score. The bottom card
in their deck is worth the value of the card multiplied by 1, the
second-from-the-bottom card is worth the value of the card multiplied by 2, and so on.

Play the small crab in a game of Combat using the two decks you just dealt.
What is the winning player's score?
"""

def get_data():
    with open('input.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')

def play_game(p1, p2):
    while bool(p1) and bool(p2):
        card1 = p1.pop(0)
        card2 = p2.pop(0)
        if card1 > card2:
            p1 += [card1, card2]
        else:
            p2 += [card2, card1]
    return p1, p2

def determine_score(p1, p2):
    if p1 > p2:
        score = 0
        for i, card in enumerate(p1):
            score += card * (len(p1)-i)
    else:
        score = 0
        for i, card in enumerate(p2):
            score += card * (len(p2)-i)
    return score

INPUT = get_data()
PLAYER1, PLAYER2 = play_game([int(_) for _ in INPUT[1:INPUT.index('')]],
                             [int(_) for _ in INPUT[INPUT.index('')+2:]])
print(determine_score(PLAYER1, PLAYER2))
