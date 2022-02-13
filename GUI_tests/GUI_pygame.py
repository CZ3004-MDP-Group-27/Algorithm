import pygame
from pygame.math import Vector2
import math


#intialize game
pygame.init()

#initialize screen
screen = pygame.display.set_mode((1000, 700))
background = pygame.image.load("GUI_Images/Arena.png")
background = pygame.transform.scale(background,(700,700))

#Title
pygame.display.set_caption("GUI")
"""
set icon below
"""
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)

class Movable_Object(pygame.sprite.Sprite):
    def __init__ (self, pos, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.offset = Vector2(0, 0)
        self.pos = Vector2(pos) 
        self.angle = 0


    def move_forward(self, distance, angle):
        if angle == 0:
            self.pos[1] -= distance
        if angle == 45:
            self.pos[0] -= distance * (1/math.sqrt(2))
            self.pos[1] -= distance * (1/math.sqrt(2))
        if angle == 90:
            self.pos[0] -= distance
        if angle == 135:
            self.pos[0] -= distance * (1/math.sqrt(2))
            self.pos[1] += distance * (1/math.sqrt(2))
        if angle == 180:
            self.pos[1] += distance
        if angle == 225:
            self.pos[0] += distance * (1/math.sqrt(2))
            self.pos[1] += distance * (1/math.sqrt(2))
        if angle == 270:
            self.pos[0] += distance
        if angle == 315:
            self.pos[0] += distance * (1/math.sqrt(2))
            self.pos[1] -= distance * (1/math.sqrt(2))
    
    def move_backward(self, distance, angle):
        if angle == 0:
            self.pos[1] += distance
        if angle == 45:
            self.pos[0] += distance * (1/math.sqrt(2))
            self.pos[1] += distance * (1/math.sqrt(2))
        if angle == 90:
            self.pos[0] += distance
        if angle == 135:
            self.pos[0] += distance * (1/math.sqrt(2))
            self.pos[1] -= distance * (1/math.sqrt(2))
        if angle == 180:
            self.pos[1] -= distance
        if angle == 225:
            self.pos[0] -= distance * (1/math.sqrt(2))
            self.pos[1] -= distance * (1/math.sqrt(2))
        if angle == 270:
            self.pos[0] -= distance
        if angle == 315:
            self.pos[0] -= distance * (1/math.sqrt(2))
            self.pos[1] += distance * (1/math.sqrt(2))


    def update(self):
        self.angle = self.angle%360
        self.rotate(self.angle)


    def draw(self, surf):
        surf.blit(self.image, self.center)


    def rotate(self, angle):
        """Rotate the image of the sprite around a pivot point."""
        # Rotate the image.
        self.image = pygame.transform.rotozoom(self.orig_image, angle, 1)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(self.angle)
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.pos+offset_rotated)
        
        
        

obstacle_up = pygame.image.load("GUI_Images/o up.png")
obstacle_down = pygame.image.load("GUI_Images/o down.png")
obstacle_left = pygame.image.load("GUI_Images/o left.png")
obstacle_right = pygame.image.load("GUI_Images/o right.png")

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, orientation):
        super().__init__()
        if orientation == 0:
            self.image = obstacle_up
        elif orientation == 1:
            self.image = obstacle_left
        elif orientation == 2:
            self.image = obstacle_down
        elif orientation == 3:
            self.image = obstacle_right

        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.offset = Vector2(0, 0)
        self.pos = Vector2(pos) 
        self.angle = 0

    def update(self):
        self.angle = self.angle%360
        self.rotate(self.angle)


    def draw(self, surf):
        surf.blit(self.image, self.center)


    def rotate(self, angle):
        """Rotate the image of the sprite around a pivot point."""
        # Rotate the image.
        self.image = pygame.transform.rotozoom(self.orig_image, angle, 1)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(self.angle)
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.pos+offset_rotated)
    

car = Movable_Object([70, 630], "GUI_Images/car with no box.png")
Movable_Object_Group = pygame.sprite.Group()
Movable_Object_Group.add(car)

bounding_box = Movable_Object([70, 630], "GUI_Images/bounding box.png")
Movable_Object_Group.add(bounding_box)


Obstacle_Group = pygame.sprite.Group()
obstacle_list = [[595.0, 595.0, 1], [455.0, 455.0, 3], [472.5, 157.5, 1], [52.5, 367.5, 2], [210.0, 210.0, 2]]

def insert_obstacle(x, y, orientation):
    obstacle = Obstacle([x,y], orientation)
    Obstacle_Group.add(obstacle)

#Game loop
clock = pygame.time.Clock()
running = True
while running:
    for x in range(0,5):
        insert_obstacle(obstacle_list[x][0],obstacle_list[x][1], obstacle_list[x][2])

    screen.fill((255,255,255))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 


        if event.type == pygame.KEYDOWN:
              
            if event.key == pygame.K_UP or event.key == ord('w'):
                car.move_forward(10, car.angle)
                bounding_box.move_forward(10, car.angle)

            if event.key == pygame.K_DOWN or event.key == ord('s'):

                car.move_backward(10, car.angle)
                bounding_box.move_backward(10, car.angle)

                
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                car.angle += 45
                
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                car.angle -= 45

            print(car.pos)
            print(car.angle)

    Movable_Object_Group.update()
    Movable_Object_Group.draw(screen)
    Obstacle_Group.update()
    Obstacle_Group.draw(screen)
    clock.tick(30)
    
    pygame.display.flip()
