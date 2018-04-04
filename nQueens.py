import collections
from time import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, state, parent, length):
        self.state = state
        self.parent = parent
        self.children = []
        self.remvals = set()
        for i in range(0, length):
            self.remvals.add(i)
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

LENGTH = 0
 #values would be the row number


def dfs(start):
    count = 0
    fringe = collections.deque()
    fringe.appendleft(start)
    visited = set()
    while len(fringe) > 0:
        v = fringe.popleft()
        if not LENGTH in v:
            return (v, count)
        op = v.index(LENGTH)            #put MRV heuristic here
        for i in range(0, int(LENGTH)):
            if i not in v:
                temp = True
                for j in range(0, op):
                    if abs(v[j] - i) == abs(j - op):
                        temp = False
                if temp and op != 0:
                    w = v
                    w = list(w)
                    w[op] = i
                    w = tuple(w)
                    fringe.appendleft(w)
                    visited.add(w)
                    count += 1
                if temp and op == 0:
                    w = v
                    w = list(w)
                    w[op] = i
                    w = tuple(w)
                    fringe.appendleft(w)
                    visited.add(w)
                    count += 1
    return (-1, -1)

def graph():
    global LENGTH
    LENGTH = int(input("Length?\t"))
    xvals = []
    yvals = []
    for i in range(4, LENGTH):
        xvals.append(i)
        queens = create_empty(i)
        yvals.append(CSP(queens)[1])
    print(len(xvals), len(yvals))
    plt.plot(xvals, yvals)
    plt.ylabel("some numbers")
    plt.show()

def CSP(state):
    if LENGTH not in state:
        return state
    var = get_unassigned_var(state)
    if var is not None:
        for val in get_values_for_var(var, state):
            w = state
            w = list(state)
            w[var] = val
            w = tuple(w)
            result = CSP(w)
            if result is not False:
                return result
    return False

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

def main():
    global LENGTH
    LENGTH = input("Length?\t")
    queens = create_empty(LENGTH)
    #print(dfs(queens)[1])
    print(CSP(create_empty(5))[1])
    #graph(tup)

def create_empty(size):
    tup = tuple()
    for i in range(0, int(size)):
        tup = tup + (LENGTH,)
    return tup

if __name__ == "__main__":
    graph()
