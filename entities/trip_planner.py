

from typing import List
from obstacle import Obstacle
from utils import Node



from constants import OBS_DIM, CAR_DIM, TURNING_RAD, DELTA_ST


# Add instuctions after moving to the co-ordinate 
# make a seperate function for that 


class TripPlanner:

    def __init__(self, path_sequence, obstacles):

        self.path_sequence = path_sequence
        self.obstacles = obstacles
    

    def _checkCollision(self, state:Node, obstacle :Obstacle):

        # bottom right and top left co-ordinates

        l1 = (state.x - CAR_DIM//2, state.y + CAR_DIM//2)
        l2 = (obstacle.pos_x - OBS_DIM//2, obstacle.pos_y + OBS_DIM//2)

        r1 = (state.x + CAR_DIM//2, state.y - CAR_DIM//2)
        r2 = (obstacle.pos_x + OBS_DIM//2, obstacle.pos_y - OBS_DIM//2)

        if (l1[0] > r2[0] or l2[0] > r1[0]):

            return False

        if (r1[1] > l2[1] or r2[1] > l1[1]):

            return False
        
        return True




    def _checkStateIsValid(self,node: Node):

        # check robot is not outside the arena

        cx, cy, ctheta = node.x, node.y, node.theta

        if CAR_DIM//2<=cx<=200 - CAR_DIM//2 and CAR_DIM//2<=cy<=200-CAR_DIM//2 and ctheta % 90 == 0:

            for obs in self.obstacles:

                if self._checkCollision(node, obs):
                    return False
                
            return True
        
        return False


    def _expandNode(self,node: Node)-> List:

        cx, cy, ctheta = node.x, node.y, node.theta

        states = []

        if node.theta == 0:

            # forward 

            states.append(Node("STATE",cx+DELTA_ST, cy, ctheta))
            
            # reverse

            states.append(Node("STATE",cx+DELTA_ST, cy, ctheta))

            # turn right 

            states.append(Node("STATE",cx+TURNING_RAD, cy-TURNING_RAD, 270))

            # turn left

            states.append(Node("STATE",cx+TURNING_RAD, cy+TURNING_RAD, 90))
        
        elif node.theta == 90:

            # forward 

            states.append(Node("STATE",cx, cy+DELTA_ST, ctheta))
            
            # reverse

            states.append(Node("STATE",cx, cy+DELTA_ST, ctheta))

            # turn right 

            states.append(Node("STATE",cx+TURNING_RAD, cy+TURNING_RAD, 0))

            # turn left

            states.append(Node("STATE", cx-TURNING_RAD, cy+TURNING_RAD, 180))
        
        elif node.theta == 180:

            # forward 

            states.append(Node("STATE",cx-DELTA_ST, cy, ctheta))
            
            # reverse

            states.append(Node("STATE",cx+DELTA_ST, cy, ctheta))

            # turn right 

            states.append(Node("STATE",cx-TURNING_RAD, cy+TURNING_RAD, 90))

            # turn left

            states.append(Node("STATE",cx-TURNING_RAD, cy-TURNING_RAD, 270))
        
        elif node.theta == 270:

            # forward 

            states.append(Node("STATE",cx, cy-DELTA_ST, ctheta))
            
            # reverse

            states.append(Node("STATE",cx, cy+DELTA_ST, ctheta))

            # turn right 

            states.append(Node("STATE",cx-TURNING_RAD, cy-TURNING_RAD, 180))

            # turn left

            states.append(Node("STATE",cx+TURNING_RAD, cy-TURNING_RAD, 0))

        return_states = []

        for st in states:

            if self._checkStateIsValid(st):

                return_states.append(st)

        return return_states

    def _generateInstructions(self):

        # just trace back the code for _expand node

        pass


    def planTripBFS(self,startNode: Node , goalNode: Node):


        # breadth first search algorithm (Simple and Naive BackTracking)
        
        queue = [[startNode]]
        level = 0
        visited = {}

        while (len(queue) != 0):
            
            path = queue.pop(0)

            if len(path) > level:
                level += 1
                print(f"Level: {level}")

            newNode = path[-1]

            if f"{newNode.x}, {newNode.y}, {newNode.theta}" in visited:
                continue

            if newNode == goalNode:
                #print(f"Trip from {startNode.key} to {goalNode.key}: {path}")

                return path
            
            adj = self._expandNode(newNode)

            for item in adj:

                newPath = path [:]
                # if item not in newPath:
                newPath.append(item)

                queue.append(newPath)
            
            visited[f"{newNode.x}, {newNode.y}, {newNode.theta}"] = True
    
            


# testing 
## TEST 1
startNode = Node("START", 60, 60, 90)
goalNode = Node("GOAL", 150, 60, 180)

obs = [ Obstacle("2", 100, 60, 0), Obstacle("1", 180, 70, 180)]
path = []

algo = TripPlanner(path, obs)

trip = algo.planTripBFS(startNode, goalNode)

for st in trip:

    print(f"ROB Moves to ({st.x}, {st.y}, {st.theta})")






            

        


        





        