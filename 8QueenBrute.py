import collections
class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.children = []
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

#1 = queen placed
#0 = possible place
#-1 = invalid square

LENGTH = 8

def placeQueen(board, index):
    global LENGTH
    l = list(board)
    l[index] = "1"
    n = index
    while inBounds(n2ij(n)[0] - 1) and inBounds(n2ij(n)[1] + 1) and n - 7 >= 0:
        l[n - 7] = "2"
        n = n - 7
    n = index
    while inBounds(n2ij(n)[0] - 1) and inBounds(n2ij(n)[1] - 1) and n - 9 >= 0:
        l[n - 9] = "2"
        n = n - 9
    n = index
    while inBounds(n2ij(n)[0] + 1) and inBounds(n2ij(n)[1] + 1) and n + 9 < LENGTH ** 2:
        l[n + 9] = "2"
        n = n + 9
    n = index
    while inBounds(n2ij(n)[0] + 1) and inBounds(n2ij(n)[1] - 1) and n + 7 < LENGTH ** 2:
        l[n + 7] = "2"
        n = n + 7
    n = index
    while n - 8 >= 0:
        l[n - 8] = "2"
        n = n - 8
    n = index
    while n + 8 < LENGTH ** 2:
        l[n + 8] = "2"
        n = n + 8
    #do rows if you have time, but not necessary
    return "".join(l)

def n2ij(n):
    global LENGTH
    return (int(n/LENGTH), n % LENGTH)

def inBounds(i):
    global LENGTH
    return i >= 0 and i <= LENGTH

def dfs(start_node):
    global LENGTH
    fringe = collections.deque()
    fringe.appendleft(start_node)
    visited = set()
    while len(fringe) != 0:
        v = fringe.popleft()
        if v.state.count("1") == LENGTH:         #checks if there are 8 ones in the state
            return v
        for i in range(LENGTH * v.depth, LENGTH * v.depth + LENGTH):
            print(i, len(v.state))
            k = v.state[i]
            if k == "0":
                v.children.append(Node(placeQueen(v.state, i), v))
        for c in v.children:
            fringe.appendleft(c)
            visited.add(c.state)
    return None

def main():
    global LENGTH
    board = ""
    for i in range(0, LENGTH * LENGTH):
        board += "0"
    node = dfs(Node(board, None))
    print(node.state)

if __name__ == "__main__":
    main()