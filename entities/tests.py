
from typing import List
from obstacle import Obstacle
from math import pi
from utils import Node
from heapq import heapify, heappush, heappop
from trip_planner import TripPlanner
# # testing 
# ## TEST 1
# startNode = Node("START", 80, 60, 90)
# goalNode = Node("GOAL", 50, 85, 180)

# obs = [ Obstacle("2", 80, 85, 0)]
# path = []

# algo = TripPlanner(path, obs)
# print(algo._checkStateIsValid(startNode))
# print(algo._checkStateIsValid(goalNode))

# trip = algo.planTripBFS(startNode, goalNode)
# if len(trip) == 0:
#     print ("Oops! No solution found")
# for st in trip:
#     print(f"ROB Moves to ({st.x}, {st.y}, {st.theta})")


# ## TEST 2 

# startNode = Node("START", 80, 60, 90)
# goalNode = Node("GOAL", 50, 85, 180)

# obs = [ Obstacle("2", 80, 85, 0)]
# path = []

# algo = TripPlanner(path, obs)
# print(algo._checkStateIsValid(startNode))
# print(algo._checkStateIsValid(goalNode))

# trip =  algo.planTripAStar(startNode, goalNode)


# for st in trip:
#         print(f"ROB Moves to ({st})")

## TEST 3 (More obstacles)

startNode = Node("START", 15, 15, 90)
goalNode = Node("GOAL", 190, 160, 180)

obs = [ Obstacle("1", 150, 60, 0),Obstacle("2", 100, 100, 90), Obstacle("3", 60, 60, 270), Obstacle("3", 180, 150, 270) ]
path = []

algo = TripPlanner(path, obs)
print(algo._checkStateIsValid(startNode))
print(algo._checkStateIsValid(goalNode))
trip = algo.planTripBFS(startNode, goalNode)
if len(trip) == 0:
    print ("Oops! No solution found")
trip =  algo.planTripAStar(startNode, goalNode)


for st in trip:
        print(f"ROB Moves to ({st})")
