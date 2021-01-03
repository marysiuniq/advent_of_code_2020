# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 08:18:10 2020

@author: prendradjaja
"""

order = [int(x) for x in '463528179']

LOW = min(order)
HIGH = max(order)

nodes = {}

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def pick_up(self):
        next3 = [self.next, self.next.next, self.next.next.next]
        ints = [x.val for x in next3]
        next_val = self.val - 1
        if next_val < LOW:
            next_val = HIGH
        while next_val in ints:
            next_val -= 1
            if next_val < LOW:
                next_val = HIGH
        self.next = next3[-1].next
        next3[-1].next = nodes[next_val].next
        nodes[next_val].next = next3[0]
        return self.next

root = None
prev = None
for x in order:
    nodes[x] = Node(x)
    if prev is None:
        root = nodes[x]
    else:
        prev.next = nodes[x]
    prev = nodes[x]
prev.next = root

curr = root
for i in range(100):
    curr = curr.pick_up()

res = ''
curr = nodes[1].next
while curr != nodes[1]:
    res += str(curr.val)
    curr = curr.next
print(res)

order2 = list(range(1, 1000001))
order2[:len(order)] = order

LOW = min(order2)
HIGH = max(order2)

nodes = {}

root = None
prev = None
for x in order2:
    nodes[x] = Node(x)
    if prev is None:
        root = nodes[x]
    else:
        prev.next = nodes[x]
    prev = nodes[x]
prev.next = root

curr = root
for i in range(10000000):
    curr = curr.pick_up()

print(nodes[1].next.val * nodes[1].next.next.val)