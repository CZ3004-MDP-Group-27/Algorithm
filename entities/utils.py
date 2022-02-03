


class Node:

    def __init__(self,key,x, y, theta):
        self.key = key
        self.x = x
        self.y = y
        self.theta = theta

    def __eq__(self, other):
        
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y and self.theta == other.theta
        return False


class Edge:

    def __init__(self, src:Node, dest:Node, weight: float):

        self.src = src
        self.dest = dest
        self.weight = weight 





