
from utils import Node
from obstacle import Obstacle
from graph import Graph
from trip_planner import TripPlanner

def main(input_str = "ROB:20,20;OBS1:105,105,90;OBS2:155,65,90;OBS3:65,65,270;OBS4:195,105,180;OBS5:130,160,180"):

    # input_str = input()

    carNode, obstacles = preprocess(input_str= input_str)

    graph = Graph(carNode)
    graph.constructGraph(obstacles)

    best_path = graph.bruteforce()
    greedy_path = graph.nearestNeighbour()
    best_path_str, greedy_path_str = "", ""

    for item in best_path:
        best_path_str += f"->{item.key}"
    
    for item in greedy_path:
        greedy_path_str += f"->{item.key}"

    

    print(f"Best path:{best_path_str}")
    print(f"Greedy Path: {greedy_path_str}")

    algo = TripPlanner(best_path, obstacles)
    commands = []
    for item in best_path:

        item.x = round(item.x)
        item.y = round(item.y)
        print((item.x, item.y))

    for i in range (len(best_path)-1):

        print(((best_path[i].x,best_path[i].y), (best_path[i+1].x,best_path[i+1].y)))
        trip = algo.planTripAStar(best_path[i], best_path[i+1])

        instr = algo.generateInstructions(trip)
        commands += instr
        commands.append("CAPTURE 20")

    return commands 


def preprocess(input_str):

    objects = input_str.split(";")

    obstacles = []

    for item in objects:

        key, pos = item.split(":")

        if key == "ROB":

            posX, posY = list(map(int,pos.split(",")))
            carNode = Node(key, posX, posY, theta= 90)
        else:

            posX, posY, pos_image = list(map(int,pos.split(",")))
            print(posX,posY,pos_image)
            
            obstacles.append(Obstacle(key, posX, posY, pos_image))
    return carNode, obstacles 




    






if __name__ == "__main__":

    print(main('ROB:15,15;OBS1:170,30,90;OBS2:130,70,0;OBS3:135,155,90;OBS4:15,95,270;OBS5:60,140,180'))