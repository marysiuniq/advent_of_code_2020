# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 06:28:28 2020

@author: Marysia
Puzzle 22 part 2 from https://adventofcode.com/2020/day/22
--- Day 22: Crab Combat ---

Recursive Combat rules:
- Before either player deals a card, if there was a previous round in this game
  that had exactly the same cards in the same order in the same players' decks,
  the game instantly ends in a win for player 1. Previous rounds from other games
  are not considered. (This prevents infinite games of Recursive Combat, which
  everyone agrees is a bad idea.)
- Otherwise, this round's cards must be in a new configuration; the players begin
  the round by each drawing the top card of their deck as normal.
- If both players have at least as many cards remaining in their deck as the value
  of the card they just drew, the winner of the round is determined by playing
  a new game of Recursive Combat (see below).
- Otherwise, at least one player must not have enough cards left in their deck
  to recurse; the winner of the round is the player with the higher-value card.

What is the winning player's score?
"""

from copy import copy

def get_data():
    with open('input.txt', 'r') as in_file:
        data_str = in_file.read()
    return data_str.split('\n')

def play_game(p1, p2):
    p1_prev = []
    p2_prev = []
    while bool(p1) and bool(p2):
        p1_prev += [copy(p1)]
        p2_prev += [copy(p2)]
        card1 = p1.pop(0)
        card2 = p2.pop(0)
        if len(p1) >= card1 and len(p2) >= card2:
            p1_copy, p2_copy = play_game(p1[:card1], p2[:card2])
            if bool(p1_copy) and not bool(p2_copy):
                p1 += [card1, card2]
            elif not bool(p1_copy) and bool(p2_copy):
                p2 += [card2, card1]
        elif card1 > card2:
            p1 += [card1, card2]
        else:
            p2 += [card2, card1]
        if p1 in p1_prev or p2 in p2_prev:
            return p1, []
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
