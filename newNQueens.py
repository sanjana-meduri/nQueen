import random
from matplotlib import pyplot as plt
import math
import sys
from time import time

global COUNT
COUNT = 0

def initial_state(n):
    return ([-1]*n, {i: set(range(n)) for i in range(n)})

def goal_test(state):
    return not (-1 in state[0])

def get_next_unassigned_var(state):
    min = 0
    for i in range(len(state[0])):
        if state[0][i] == -1:
            min = i
            break
    for key in state[1]:
        if state[0][key] == -1 and len(state[1][key]) < len(state[1][min]):
            min = key
    return min

def get_sorted_values(state, var):
    dict = state[1]
    li = list(state[1][var])
    li.sort()
    se = set(li)
    return se
    #return set(list(state[1][var]).sort())    #find better way to sort it

def assign(state, var, value):
    state[0][var] = value
    state[1][var] = {value} #you don't acutally have to do it
    for key in state[1]:
        if key != var:
            state[1][key].discard(value)
            state[1][key].discard(value + abs(key - var))
            state[1][key].discard(value - abs(key - var))

def csp(state):
    global COUNT
    queens, board = state
    #print(queens, board.items())
    if COUNT > 5*len(queens):
        (queens, board), COUNT = initial_state(len(queens)), 0
    if goal_test(state): return state
    COUNT += 1
    var = get_next_unassigned_var(state)
    vals = get_sorted_values(state, var)        #replace vals in line below
    for val in vals:
        new_state = (list(queens), {i: set(board[i]) for i in board})
        assign(new_state, var, val)
        result = csp(new_state)
        if result is not False:
            return result
    return False

def main():
    global COUNT
    initial = initial_state(int(input("length:\t")))
    tic = time()
    answer = csp(initial)
    toc = time()
    print(csp(initial)[0])
    print("nodes:", COUNT)
    print("time: %5.2f seconds" % (toc - tic))

def graph():
    global COUNT
    cap = 250
    times = []
    space = []
    for i in range(4, cap, 3):
        tic = time()
        csp(initial_state(i))
        toc = time()
        times.append(toc - tic)
        space.append(COUNT)
        COUNT = 0
    plt.plot(range(4, cap, 3), times)
    plt.ylabel("Time")
    plt.xlabel("Size")
    plt.title("Time Complexity")
    plt.show()


if __name__ == "__main__":
    graph()