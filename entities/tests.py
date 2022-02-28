
from typing import List
from obstacle import Obstacle
from math import pi
from utils import Node
from heapq import heapify, heappush, heappop
from trip_planner import TripPlanner
# # testing 
# ## TEST 1
startNode = Node("START", 80, 60, 90)
goalNode = Node("GOAL", 80, 85, 90)

obs = [ Obstacle("2", 140, 85, 0)]
path = []

algo = TripPlanner(path, obs)
i = algo._moveForward(startNode)
print(i.x, i.y,i.theta)
print(algo.collision_detector.checkStateIsValid(startNode))
print(algo.collision_detector.checkStateIsValid(goalNode))

trip = algo.planTripBFS(startNode, goalNode)
if len(trip) == 0:
    print ("Oops! No solution found")
for st in trip:
    print(f"ROB Moves to ({st.x}, {st.y}, {st.theta})")


# ## TEST 2 

startNode = Node("START", 80, 60, 90)
goalNode = Node("GOAL", 50, 85, 180)

obs = [ Obstacle("2", 80, 85, 0)]
path = []

algo = TripPlanner(path, obs)
# print(algo._checkStateIsValid(startNode))
# print(algo._checkStateIsValid(goalNode))

trip =  algo.planTripAStar(startNode, goalNode)


for st in trip:
        print(f"ROB Moves to ({st})")

# ## TEST 3 (More obstacles)

# startNode = Node("START", 155, 105, 270)
# goalNode = Node("GOAL", 155, 105, 0)

# obs = [ Obstacle("1", 155, 65, 0),Obstacle("2", 105, 105, 90), Obstacle("3", 65, 65, 270), Obstacle("4", 195, 105, 180) ]
# path = []

# algo = TripPlanner(path, obs)
# # print(algo._checkStateIsValid(startNode))
# # print(algo._checkStateIsValid(goalNode))
# trip = algo.planTripBFS(startNode, goalNode)
# if len(trip) == 0:
#     print ("Oops! No solution found")
# trip =  algo.planTripAStar(startNode, goalNode)

# for st in trip:
#     print(f"ROB Moves to ({st})")
# instructions = algo.generateInstructions(trip)
# print(instructions)

