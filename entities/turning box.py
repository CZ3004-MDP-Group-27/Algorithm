from trip_planner import *
from constants import width, height, WIDTH, HEIGHT

class turning_box():
    pos = [0,0]
    x_boundary = [0,0]
    y_boundary = [0,0]
    def __init__(self, pos_of_car, orientation,  direction_of_turn):
        super().__init__()
        if orientation == 'N':
            if direction_of_turn == 'left':
                self.pos[0] = pos_of_car[0] + width - (WIDTH/2)
                self.pos[1] = pos_of_car[1] + height - (HEIGHT/2)
            elif direction_of_turn == 'right':
                self.pos[0] = pos_of_car[0] - width - (WIDTH/2)
                self.pos[1] = pos_of_car[1] + height - (HEIGHT/2)
            self.x_boundary[0] = self.pos[0] - (WIDTH/2)
            self.x_boundary[1] = self.pos[0] + (WIDTH/2)
            self.y_boundary[0] = self.pos[1] - (HEIGHT/2)
            self.y_boundary[1] = self.pos[1] + (HEIGHT/2)
        elif orientation == 'S':
            if direction_of_turn == 'left':
                self.pos[0] = pos_of_car[0] - width + (WIDTH/2)
                self.pos[1] = pos_of_car[1] - height + (HEIGHT/2)
            elif direction_of_turn == 'right':
                self.pos[0] = pos_of_car[0] + width - (WIDTH/2)
                self.pos[1] = pos_of_car[1] - height + (HEIGHT/2)
            self.x_boundary[0] = self.pos[0] - (WIDTH/2)
            self.x_boundary[1] = self.pos[0] + (WIDTH/2)
            self.y_boundary[0] = self.pos[1] - (HEIGHT/2)
            self.y_boundary[1] = self.pos[1] + (HEIGHT/2)
        elif orientation == 'E':
            if direction_of_turn == 'left':
                self.pos[0] = pos_of_car[0] - height + (HEIGHT/2)
                self.pos[1] = pos_of_car[1] + width - (WIDTH/2)
            elif direction_of_turn == 'right':
                self.pos[0] = pos_of_car[0] - height + (HEIGHT/2)
                self.pos[1] = pos_of_car[1] - width + (WIDTH/2)
            self.x_boundary[0] = self.pos[0] - (HEIGHT/2)
            self.x_boundary[1] = self.pos[0] + (HEIGHT/2)
            self.y_boundary[0] = self.pos[1] - (WIDTH/2)
            self.y_boundary[1] = self.pos[1] + (WIDTH/2)
        elif orientation == 'W':
            if direction_of_turn == 'left':
                self.pos[0] = pos_of_car[0] + height - (HEIGHT/2)
                self.pos[1] = pos_of_car[1] - width + (WIDTH/2)
            elif direction_of_turn == 'right':
                self.pos[0] = pos_of_car[0] + height - (HEIGHT/2)
                self.pos[1] = pos_of_car[1] + width - (WIDTH/2)
            self.x_boundary[0] = self.pos[0] - (HEIGHT/2)
            self.x_boundary[1] = self.pos[0] + (HEIGHT/2)
            self.y_boundary[0] = self.pos[1] - (WIDTH/2)
            self.y_boundary[1] = self.pos[1] + (WIDTH/2)

        self.pos = [self.pos[0], self.pos[1]]


out_of_bounds = False
box =  turning_box((300,300), 'E', 'right')
print("(x, y): ",box.pos)
print("x boundary: ",box.x_boundary)
print("y boundary: ",box.y_boundary)

obstacle_list = [[595.0, 595.0, 90], [455.0, 455.0, 0], [472.5, 157.5, 90], [52.5, 367.5, 270], [210.0, 210.0, 180]]

for boundary in box.x_boundary:
    if boundary < 0  or boundary > 700:
        print("x coordinate of turning box out of bounds")
        out_of_bounds = True

for boundary in box.y_boundary:
    if boundary < 0  or boundary > 700:
        print("y coordinate of turning box out of bounds")
        out_of_bounds = True


for obstacle in obstacle_list:
    if (obstacle[0]-17.5 > box.x_boundary[0] and obstacle[0]+17.5 < box.x_boundary[1]) or (obstacle[1]-17.5 > box.y_boundary[0] and obstacle[1]+17.5 < box.y_boundary[1]):
        print("obstacle({}, {}) is within the turning box".format(obstacle[0], obstacle[1]))

