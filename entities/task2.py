
from utils import Node
from obstacle import Obstacle
from graph import Graph
from trip_planner import TripPlanner
import math
from copy import deepcopy

OBS_LENGTH = 60
OBS_WIDTH = 10
CAR_CX = 100
CAR_CY = 15
FOCUS = 10


def generateCheckpoints(obsx, obsy):

    obs_cx = CAR_CX +obsx
    obs_cy = CAR_CY + obsy + 15 + OBS_WIDTH//2

    checkpoint_left_x = obs_cx - (OBS_LENGTH//2 + FOCUS + 15)
    checkpoint_left_y = obs_cy

    checkpoint_right_x = obs_cx + (OBS_LENGTH//2 + FOCUS + 15)
    checkpoint_right_y = obs_cy

    checkpoint_up_x = obs_cx
    checkpoint_up_y = obs_cy + (OBS_WIDTH//2 + FOCUS + 15)

    checkpoint_down_x = CAR_CX
    checkpoint_down_y = CAR_CY + obsy - (30+15)

    checkpoints = [Node("STATE", checkpoint_down_x, checkpoint_down_y, 90), Node("STATE", checkpoint_left_x, checkpoint_left_y, 90),
    Node("STATE", checkpoint_up_x, checkpoint_up_y, 0), Node("STATE", checkpoint_right_x, checkpoint_right_y, 180), Node("STATE", checkpoint_down_x, checkpoint_down_y, 90)]

    return checkpoints

def generateObstacles(obsx, obsy):
    obs_cx = CAR_CX +obsx
    obs_cy = CAR_CY + obsy + 15 + OBS_WIDTH//2

    lower_limit = obs_cx - 20
    upper_limit = obs_cx + 20

    obstacles = []
    for cx in range(lower_limit, upper_limit+1, 10):

        obstacles.append(Obstacle("OBS", cx, obs_cy, 0))

    return obstacles




def main(obsx, obsy):

    start_node = Node("ROB", CAR_CX, CAR_CY, 90)

    checkpoints = generateCheckpoints(obsx, obsy)

    checkpoints.append(start_node)

    current = start_node
    obstacle_lst = generateObstacles(obsx, obsy)
    algo = TripPlanner(checkpoints, obstacle_lst)
    stm_commands = []

    for next in range (0,len(checkpoints)):

        dest = deepcopy(checkpoints[next])
        
        print("First Try:")
        print(((current.x,current.y), (dest.x,dest.y)))
        trip = algo.planTripAStar(current, dest)
        if len(trip) == 0:
            return ""
        
        stm_instr = algo.generateInstructions(trip, device = "stm")
        stm_commands.append(';'.join(stm_instr))
        current=dest
    stm_commands = "-".join(stm_commands)
    return stm_commands

if __name__ == "__main__":

    print(main(0, 80))

    

