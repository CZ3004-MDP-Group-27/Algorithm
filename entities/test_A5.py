
from obstacle import Obstacle
from utils import Node
from trip_planner_copy import TripPlanner

def calcPath(y_dist):


    startNode = Node("START", 100, 15, 90)

    obs_lst = [Obstacle("1", 100, y_dist, 270), Obstacle("2", 100, y_dist, 0), Obstacle("3", 100, y_dist, 90), Obstacle("4", 100, y_dist, 180)]
    path = []

    algo = TripPlanner(path, obs_lst)

    nodeList = []

    for obs in obs_lst:

        posX, posY, theta = obs.generate_waypoint()
        nodeList.append(Node(obs.key, posX, posY, theta=theta))
        print(f"Waypoint of {obs.key}: {posX}, {posY}, {theta}")

    nodeList = [startNode] + nodeList

    for item in nodeList:

        item.x = round(item.x)
        item.y = round(item.y)
        print((item.x, item.y))

    commands = []
    for i in range (len(nodeList)-1):

        print(((nodeList[i].x,nodeList[i].y), (nodeList[i+1].x,nodeList[i+1].y)))

        trip = algo.planTripAStar(nodeList[i], nodeList[i+1])

        instr = algo.generateInstructions(trip)
        
        trp = ";".join(instr)
        print(trp)
        commands.append(trp)

    return "-".join(commands)


print(calcPath(60))
        

