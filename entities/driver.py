from doctest import ELLIPSIS_MARKER
from utils import Node
from obstacle import Obstacle
from graph import Graph

def main():

    # input_str = input()

    input_str = "ROB:15,15;OBS1:100,100,90;OBS2:150,60,0;OBS3:60,60,270;OBS4:200,100,180"

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
    



def preprocess(input_str):

    objects = input_str.split(";")

    obstacles = []

    for item in objects:

        key, pos = item.split(":")

        if key == "ROB":

            posX, posY = list(map(int,pos.split(",")))
            carNode = Node(key, posX, posY)
        else:

            posX, posY, pos_image = list(map(int,pos.split(",")))
            print(posX,posY,pos_image)
            
            obstacles.append(Obstacle(key, posX, posY, pos_image))
    return carNode, obstacles 




    






if __name__ == "__main__":

    main()