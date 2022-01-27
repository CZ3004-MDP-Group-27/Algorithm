


class Node:

    def __init__(self,key,x, y):
        self.key = key
        self.x = x
        self.y = y


class Edge:

    def __init__(self, src:Node, dest:Node, weight: float):

        self.src = src
        self.dest = dest
        self.weight = weight 





