


class Node:

    def __init__(self,key,x, y, theta, parent = None, h = None):
        self.key = key
        self.x = x
        self.y = y
        self.theta = theta
        self.parent = parent
        self.h = h 

    def __eq__(self, other):
        
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y and self.theta == other.theta
        return False
    
    def __lt__(self, other):
         return self.h < other.h


class Edge:

    def __init__(self, src:Node, dest:Node, weight: float):

        self.src = src
        self.dest = dest
        self.weight = weight 


# class AStar_Node (Node):

#     def __init__(self, key, x, y, theta, f = 0, g = 0, h=0):
#         super().__init__(key, x, y, theta)
#         self.f = f
#         self.g = g
#         self.h = h
#         self.parent = None
    
#     def setParent(self, parent):

#         self.parent = parent
    
#     def setf(self, f):
#         self.f = f
    
#     def setg (self, g):
#         self.g = g
    
#     def seth(self, h):

#         self.h = h
    
#     def __eq__(self, other):

#         if isinstance(other, AStar_Node):
#             return self.x == other.x and self.y == other.y and self.theta == other.theta
#         return False

#     # add cmp function

#     def __lt__(self, other):
#         return self.f < other.f






