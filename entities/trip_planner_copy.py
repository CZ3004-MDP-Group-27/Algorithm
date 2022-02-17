

from typing import List
from obstacle import Obstacle
from math import pi
from utils import Node
from heapq import heapify, heappush, heappop

# importing the constants 
from constants import OBS_DIM, CAR_DIM, TURNING_RAD, DELTA_ST, TR_ST,TR_SIDE



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

    def checkTurn(self, node:Node):

        pass


    def _expandNodeBFS(self,node: Node)-> List:

        cx, cy, ctheta = node.x, node.y, node.theta

        states = []

        if ctheta == 0:

            # forward 

            states.append(Node("STATE",cx+DELTA_ST, cy, ctheta))
            
            # reverse

            states.append(Node("STATE",cx-DELTA_ST, cy, ctheta))

            # dummy states 
            dummy_right = (Node("DUMMY", cx, cy-TR_SIDE, ctheta))
            dummy_st_fr = (Node("DUMMY", cx+TR_ST, cy, ctheta))
            dummy_left = (Node("DUMMY", cx, cy+TR_SIDE, ctheta))
            dummy_st_bk = (Node("DUMMY", cx-TR_ST, cy, ctheta))

            # forward turn
            if self._checkStateIsValid(dummy_st_fr):
                if self._checkStateIsValid(dummy_right):
                    states.append(Node("STATE",cx+TR_ST, cy-TR_SIDE, 270))
                if self._checkStateIsValid(dummy_left):
                    states.append(Node("STATE",cx+TR_ST, cy+TR_SIDE, 90))
            
            # backward turn
            if self._checkStateIsValid(dummy_st_bk):
                if self._checkStateIsValid(dummy_right):
                    states.append(Node("STATE",cx-TR_ST, cy-TR_SIDE, 90))
                if self._checkStateIsValid(dummy_left):
                    states.append(Node("STATE",cx-TR_ST, cy+TR_SIDE, 270))
        
        elif node.theta == 90:

            # forward 

            states.append(Node("STATE",cx, cy+DELTA_ST, ctheta))
            
            # reverse

            states.append(Node("STATE",cx, cy-DELTA_ST, ctheta))

            # dummy states 
            dummy_right = (Node("DUMMY", cx+TR_SIDE, cy, ctheta))
            dummy_st_fr = Node("DUMMY", cx, cy+TR_ST, ctheta)
            dummy_left = (Node("DUMMY", cx-TR_SIDE, cy, ctheta))
            dummy_st_bk = Node("DUMMY", cx, cy-TR_ST, ctheta)
            
            # forward turn
            if self._checkStateIsValid(dummy_st_fr):
                if self._checkStateIsValid(dummy_right):
                    states.append(Node("STATE",cx+TR_SIDE, cy+TR_ST, 0))
                if self._checkStateIsValid(dummy_left):
                    states.append(Node("STATE", cx-TR_SIDE, cy+TR_ST, 180))
            
            # backward turn
            if self._checkStateIsValid(dummy_st_bk):
                if self._checkStateIsValid(dummy_right):
                    states.append(Node("STATE",cx+TR_SIDE, cy-TR_ST, 180))
                if self._checkStateIsValid(dummy_left):
                    states.append(Node("STATE",cx-TR_SIDE, cy-TR_ST, 0))
        
        elif node.theta == 180:

            # forward 

            states.append(Node("STATE",cx-DELTA_ST, cy, ctheta))
            
            # reverse

            states.append(Node("STATE",cx+DELTA_ST, cy, ctheta))

            # dummy states
            dummy_right = Node("DUMMY", cx, cy+TR_SIDE, ctheta)
            dummy_st_fr = Node("DUMMY", cx-TR_ST, cy, ctheta)
            dummy_left = Node("DUMMY", cx, cy-TR_SIDE, ctheta)
            dummy_st_bk = Node("DUMMY", cx+TR_ST, cy, ctheta)

            # forward turn
            if self._checkStateIsValid(dummy_st_fr):
                if self._checkStateIsValid(dummy_right):
                    states.append(Node("STATE",cx-TR_ST, cy+TR_SIDE, 90))
                if self._checkStateIsValid(dummy_left):
                    states.append(Node("STATE",cx-TR_ST, cy-TR_SIDE, 270))
            
            # backward turn
            if self._checkStateIsValid(dummy_st_bk):
                if self._checkStateIsValid(dummy_right):
                    states.append(Node("STATE",cx+TR_ST, cy+TR_SIDE, 270))
                if self._checkStateIsValid(dummy_left):
                    states.append(Node("STATE",cx+TR_ST, cy-TR_SIDE, 90))
        
        elif node.theta == 270:

            # forward 

            states.append(Node("STATE",cx, cy-DELTA_ST, ctheta))
            
            # reverse

            states.append(Node("STATE",cx, cy+DELTA_ST, ctheta))

            # dummy states 
            dummy_right = Node("DUMMY", cx-TR_SIDE, cy, ctheta)
            dummy_st_fr = Node("DUMMY", cx, cy-TR_ST, ctheta)
            dummy_left = Node("DUMMY", cx+TR_SIDE, cy, ctheta)
            dummy_st_bk = Node("DUMMY", cx, cy+TR_ST, ctheta)

            # forward turn
            if self._checkStateIsValid(dummy_st_fr):
                if self._checkStateIsValid(dummy_right):
                    states.append(Node("STATE",cx-TR_SIDE, cy-TR_ST, 180))
                if self._checkStateIsValid(dummy_left):
                    states.append(Node("STATE",cx+TR_SIDE, cy-TR_ST, 0))
            
            if self._checkStateIsValid(dummy_st_bk):
                if self._checkStateIsValid(dummy_right):
                    states.append(Node("STATE",cx-TR_SIDE, cy+TR_ST, 0))
                if self._checkStateIsValid(dummy_left):
                    states.append(Node("STATE",cx+TR_SIDE, cy+TR_ST, 180))

        return_states = []

        for st in states:

            if self._checkStateIsValid(st):

                return_states.append(st)

        return return_states

    def generateInstructions(self, coordinates:  List):
        instructions = []
        delta = 0
        dummy_pt = f"200 200 -360" # for getting the final forward or reverse
        coordinates.append(dummy_pt)
        for i in range (len(coordinates)-1):
            currentx, currenty, currenttheta = list(map(int,coordinates[i].split(" ")))
            nextx, nexty, nexttheta = list(map(int,coordinates[i+1].split(" ")))
    
            if currenttheta == 0:
            
                if nexttheta == currenttheta:
                    
                    delta += (nextx - currentx)
                    
                    continue

                else:

                    if delta > 0:
                        instructions.append(f"FORWARD {delta}")
                    elif delta < 0:
                        instructions.append(f"BACKWARD {-delta}")
                    delta = 0

                    if nexttheta == 90:

                        if nextx > currentx:
                            instructions.append(f"FORWARD TURN LEFT")
                        if nextx < currentx:
                            instructions.append(f"BACKWARD TURN RIGHT")
                    
                    if nexttheta == 270:

                        if nextx > currentx:
                            instructions.append(f"FORWARD TURN RIGHT")
                        if nextx < currentx:
                            instructions.append(f"BACKWARD TURN LEFT")
            
            elif currenttheta == 90:
                if nexttheta == currenttheta:
                    
                    delta += (nexty - currenty)
                    continue

                else:

                    if delta > 0:
                        instructions.append(f"FORWARD {delta}")
                    elif delta < 0:
                        instructions.append(f"BACKWARD {-delta}")
                    delta = 0

                    if nexttheta == 0:

                        if nextx > currentx:
                            instructions.append(f"FORWARD TURN RIGHT")
                        if nextx < currentx:
                            instructions.append(f"BACKWARD TURN LEFT")
                    
                    if nexttheta == 180:

                        if nextx < currentx:
                            instructions.append(f"FORWARD TURN LEFT")
                        if nextx > currentx:
                            instructions.append(f"BACKWARD TURN RIGHT")
            
            elif currenttheta == 180:
                if nexttheta == currenttheta:
                    
                    delta += (currentx - nextx)
                    continue

                else:

                    if delta > 0:
                        instructions.append(f"FORWARD {delta}")
                    elif delta < 0:
                        instructions.append(f"BACKWARD {-delta}")
                    delta = 0

                    if nexttheta == 90:

                        if nextx < currentx:
                            instructions.append(f"FORWARD TURN RIGHT")
                        if nextx > currentx:
                            instructions.append(f"BACKWARD TURN LEFT")
                    
                    if nexttheta == 270:

                        if nextx < currentx:
                            instructions.append(f"FORWARD TURN LEFT")
                        if nextx > currentx:
                            instructions.append(f"BACKWARD TURN RIGHT")

            elif currenttheta == 270:
                if nexttheta == currenttheta:
                    
                    delta += (currenty - nexty)
                    continue

                else:

                    if delta > 0:
                        instructions.append(f"FORWARD {delta}")
                    elif delta < 0:
                        instructions.append(f"BACKWARD {-delta}")
                    delta = 0

                    if nexttheta == 180:

                        if nextx < currentx:
                            instructions.append(f"FORWARD TURN RIGHT")
                        if nextx > currentx:
                            instructions.append(f"BACKWARD TURN LEFT")
                    
                    if nexttheta == 0:

                        if nextx > currentx:
                            instructions.append(f"FORWARD TURN LEFT")
                        if nextx < currentx:
                            instructions.append(f"BACKWARD TURN RIGHT")

            
        return instructions
                    

                    

            

        # just trace back the code for _expand node

        pass

    def _computeManhattan(self,node1: Node, node2: Node):

        #theta_diff = abs(node1.theta - node2.theta)
        x_diff = abs (node1.x - node2.x)
        y_diff = abs (node1.y - node2.y)

        return x_diff + y_diff
    
    def _tracePath(self, stateDict:dict, goalNode: Node):
        gx, gy, gtheta = goalNode.x, goalNode.y, goalNode.theta

        path = []

        if f"{gx} {gy} {gtheta}" not in stateDict:
            return path
        
        else:
            current = f"{gx} {gy} {gtheta}" 

            while (True):

                _, node = stateDict[current]

                path.append(current)

                parent = node.parent

                if parent is None:

                    return path [::-1]
                current = f"{parent.x} {parent.y} {parent.theta}"

        



    def planTripAStar(self, startNode: Node, goalNode: Node):

        # Astar Algorithm with manhattan distance as heuristic

        # A map to represent closed list 

        # A minheap to represent the open list


        closed_list = {}
        open_list = [(0, startNode)]
        stateDetails = {}
        dist_sg = self._computeManhattan(startNode, goalNode)
        startNode.h = dist_sg
        stateDetails[f"{startNode.x} {startNode.y} {startNode.theta}"] = (f"{dist_sg} 0 {dist_sg}", startNode)
        heapify(open_list)

        while (len(open_list) != 0):
            f,current = heappop(open_list)
            adj = self._expandNodeBFS(current)
            current_hash = f"{current.x} {current.y} {current.theta}"
            _, gparent, __ = list(map(int,stateDetails[current_hash][0].split(" ")))

            for successor in adj:

                successor.parent = current
                gnew = gparent + self._computeManhattan(successor, current)
                hnew = self._computeManhattan(successor, goalNode)
                fnew = gnew + hnew 
                successor.h = hnew
                successor_hash = f"{successor.x} {successor.y} {successor.theta}"
                if successor == goalNode:
                    # return stateDetails
                    stateDetails[successor_hash] = (f"{fnew} {gnew} {hnew}", successor)
                    print ("Yay!!! We found a solution")
                    path = self._tracePath(stateDetails, goalNode)
                    return path
                elif closed_list.get(successor_hash) == False or closed_list.get(successor_hash) is None:

                    if successor_hash not in stateDetails:
                        heappush(open_list, (fnew, successor))
                        stateDetails[successor_hash] = (f"{fnew} {gnew} {hnew}", successor)
                        
                    else:
                        fold = int(stateDetails[successor_hash][0].split(" ")[0])

                        if fnew < fold:
                            heappush(open_list, (fnew, successor))
                            stateDetails[successor_hash] = (f"{fnew} {gnew} {hnew}", successor)
                elif closed_list.get(successor_hash) == True:
                    fold = int(stateDetails[successor_hash][0].split(" ")[0])

                    if fnew < fold:
                        closed_list[successor_hash] = False
                        heappush(open_list, (fnew, successor))
                        stateDetails[successor_hash] = (f"{fnew} {gnew} {hnew}", successor)

            closed_list [current_hash] = True
        
        # Algo failed which is impossible as Astar is complete 
        print ("Oops! No solution found")
        print(f"No of states searched: {len(closed_list)}")
        print(current.x, current.y, current.theta)
        return []




    def planTripBFS(self,startNode: Node , goalNode: Node):


        # breadth first search algorithm (Simple and Naive BackTracking)
        
        queue = [[startNode]]
        level = 0
        visited = {}

        while (len(queue) != 0):
            
            path = queue.pop(0)

            if len(path) > level:
                level += 1
                #print(f"Level: {level}")

            newNode = path[-1]

            if f"{newNode.x}, {newNode.y}, {newNode.theta}" in visited:
                continue

            if newNode == goalNode:
                #print(f"Trip from {startNode.key} to {goalNode.key}: {path}")

                return path
            
            adj = self._expandNodeBFS(newNode)

            #print(adj)

            for item in adj:

                newPath = path [:]
                # if item not in newPath:
                newPath.append(item)

                queue.append(newPath)
            
            visited[f"{newNode.x}, {newNode.y}, {newNode.theta}"] = True

        print(f"No of states searched: {len(visited)}")
        print(newNode.x, newNode.y, newNode.theta)
        return []
    
        



            

        


        





        