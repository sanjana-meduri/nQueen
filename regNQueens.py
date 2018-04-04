import collections
import matplotlib.pyplot as plt
from time import time
from random import *
global NODECOUNTER
NODECOUNTER = 0

LENGTH = -1

def create_empty_board(k):
    tup = tuple()
    for i in range(0, int(k)):
        tup = tup + (k,)
    return tup


def get_unassigned_var(state):
    return state.index(LENGTH)

def get_values_for_var(var, state):
    vals = set()
    for i in range(0, LENGTH):
        if i not in state:
            temp = True
            for j in range(0, var):
                if abs(state[j] - i) == abs(j - var):
                    temp = False
            if temp:
                vals.add(i)
    return vals

def MRV_get_unassigned_var(state):
    lens = list()
    for i in range(0, LENGTH):
        lens.append((len(state[i]), random(), i))
    lens.sort()
    for i in range(0, LENGTH):
        if lens[i][0] == 0:
            return None
        if lens[i][0] != 1:
            return lens[i][2]

def get_all_unassigned(state):
    empty = set()
    for i in range(0, LENGTH):
        if state[i] == LENGTH:
            empty.add(i)
    return empty

def MRV_goal_test(state):
    for i in range(0, LENGTH):
        if len(state[i]) != 1:
            return False
    return True

def CSP(state):
    if LENGTH not in state:
        return state
    var = get_unassigned_var(state)
    if var is not None:
        for val in get_values_for_var(var, state):
            w = list(state)
            w[var] = val
            w = tuple(w)
            result = CSP(w)
            if result is not False:
                return result
    return False


def MRV_CSP_old(state):
    if MRV_goal_test(state):
        return state
    var = get_MRV(state)
    if var is not None:
        for val in state[var]:
            w = state
            w = list(state)
            w[var] = set(val)
            for i in range(0, len(w)):
                w[i] = set(get_values_for_var(i, w))
                #adjust
            w = tuple(w)
            result = MRV_CSP(w)
            if result is not False:
                return result
    return False

def get_MRV(state):
    var = get_unassigned_var(state)
    potentialVars = get_all_unassigned(state)
    for i in potentialVars:
        vals = get_values_for_var(var, state)
        if len(vals) > len(get_values_for_var(i, state)):
            var = i
    return var

def MRV_CSP(state):
    global NODECOUNTER
    if LENGTH not in state:
        return state
    var = get_MRV(state)
    if var is not None:
        for val in get_values_for_var(var, state):
            w = state
            w = list(state)
            w[var] = val
            w = tuple(w)
            result = CSP(w)
            NODECOUNTER = NODECOUNTER + 1
            if result is not False:
                return result
    return False

def main():
    global LENGTH
    LENGTH = int(input("Length?\t"))
    board = create_empty_board(LENGTH)
    tic = time()
    board = MRV_CSP(board)
    toc = time()
    print(board)
    print("time: %5.2f seconds" % (toc - tic))

def graph():
    global NODECOUNTER
    global LENGTH
    LENGTH = int(input("Length?\t"))
    xvals = []
    yvals = []
    for i in range(4, LENGTH):
        xvals.append(i)
        queens = create_empty_board(i)
        MRV_CSP(queens)
        yvals.append(NODECOUNTER)
        NODECOUNTER = 0
    plt.plot(xvals, yvals)
    plt.ylabel("space")
    plt.show()

if __name__ == "__main__":
    graph()