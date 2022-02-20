
import pygame
import time
from widgets import Movable_Object, Obstacle, Button
from commands import parse
from main import main
import time, math
TIME_LIMIT = 360

#intialize game
pygame.init()

#initialize screen
screen = pygame.display.set_mode((1000, 700))
background = pygame.image.load("GUI_Images/Arena.png")
background = pygame.transform.scale(background,(700,700))

TURNING_RAD = 25
SCALE = 3.5

#Title
pygame.display.set_caption("GUI")
"""
set icon below
"""

    

car = Movable_Object([350, 630], "GUI_Images/car with no box.png")
Movable_Object_Group = pygame.sprite.Group()
Movable_Object_Group.add(car)

bounding_box = Movable_Object([350, 630], "GUI_Images/bounding box.png")
Movable_Object_Group.add(bounding_box)

sim_button = Button(
    "Simulate",
    (800, 300),
    font=25,
    bg="green"
)

rst_button = Button(
    "Reset",
    (815, 400),
    font=25,
    bg="red"
)


class Simulator():

    def __init__():
        pass

#Game loop
clock = pygame.time.Clock()
running = True
commands = ["FORWARD 5", "ROTATE 45", "FORWARD 35.35", "ROTATE -45", "REVERSE 5"]

Obstacle_Group = pygame.sprite.Group()
#obstacle_list = [[595.0, 595.0, 90], [455.0, 455.0, 0], [472.5, 157.5, 90], [52.5, 367.5, 270], [210.0, 210.0, 180]]
#obstacle_list = [[542.5,472.5,90], [227.5,472.5, 270],[682.5, 332.5, 180], [455, 140,180]]
obstacle_list = [[350, 437.5, 0], [350, 437.5, 90], [350, 437.5, 180], [350, 437.5, 270]]
android_string = "ROB:100,15"
for i in range(len(obstacle_list)):
    x, y , theta = obstacle_list[i]
    x = x//SCALE
    y = (700 - y)//SCALE
    android_string += f";OBS{i+1}:{int(x)},{int(y)},{int(theta)}"

print(android_string)

def generate_commands():
    instr = main(android_string)
    print(instr)
    commands = parse(instr)
    print(commands)
    return commands

commands = generate_commands()




def insert_obstacle(x, y, orientation):
    obstacle = Obstacle([x,y], orientation)
    Obstacle_Group.add(obstacle)


simulate = False
START_TIME = None

while running:
    if START_TIME  is not None:
        
        time_delta = current - START_TIME
        print(time_delta)
        if round(time_delta) > TIME_LIMIT:
            simulate = False
    
    for x in range(len(obstacle_list)):
        insert_obstacle(obstacle_list[x][0],obstacle_list[x][1], obstacle_list[x][2])
    screen.fill((255,255,255))
    screen.blit(background, (0, 0))

    Movable_Object_Group.update()
    Movable_Object_Group.draw(screen)
    Obstacle_Group.update()
    Obstacle_Group.draw(screen)
    sim_button.show(screen)
    rst_button.show(screen)
   

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False 
        
        if event.type == pygame.KEYDOWN:
              
            if event.key == pygame.K_UP or event.key == ord('w'):
                car.move_forward(5, car.angle)
                bounding_box.move_forward(5, car.angle)

            if event.key == pygame.K_DOWN or event.key == ord('s'):

                car.move_backward(5, car.angle)
                bounding_box.move_backward(5, car.angle)

                
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                car.angle += 45
                
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                car.angle -= 45

        
        simulate, tm = sim_button.click(event, simulate)

        if tm is not None:
            START_TIME = tm
        
        rst_button.click(event,simulate,rst=True, robot = car, bounding_box= bounding_box)
    
    if simulate:

    
        if len(commands) == 0:
            instr = None
            simulate = False
            sim_button.display_text("Simulate", bg = "green")
            commands = generate_commands()
        else:
            instr, num = commands.pop(0).split(" ")
            num = float(num)
        
        current = time.time()
    
        if instr == "FORWARD":
            car.move_forward(num, car.angle)
            bounding_box.move_forward(num, car.angle)
            pygame.display.update()
            time.sleep(1)

        elif instr == "ROTATE":
            car.angle -= int(num)
            pygame.display.update()
            time.sleep(1)

        elif instr == "REVERSE":
            car.move_backward(num, car.angle)
            bounding_box.move_backward(num, car.angle)
            pygame.display.update()
            time.sleep(1)
        elif instr == "CAPTURE":
            myfont = pygame.font.SysFont('Comic Sans MS', 25)
            textsurface = myfont.render('Capturing Image', False, (0, 0, 0))
            screen.blit(textsurface,(0,0))
            pygame.display.update()
            time.sleep(3)

    pygame.display.update()





 