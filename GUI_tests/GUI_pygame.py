from turtle import forward
import pygame
from pygame.math import Vector2
import math

#intialize game
pygame.init()

#initialize screen
screen = pygame.display.set_mode((1000, 700))
background = pygame.image.load("GUI_Images/Arena.png")
background = pygame.transform.scale(background,(700,700))

ani = 4
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


    

car = Movable_Object([70, 630], "GUI_Images/car with no box.png")
Movable_Object_Group = pygame.sprite.Group()
Movable_Object_Group.add(car)

bounding_box = Movable_Object([70, 630], "GUI_Images/bounding box.png")
Movable_Object_Group.add(bounding_box)

"""
def check_collision(dist, direction_of_motion, angle, x,y):
    if direction_of_motion =='forward':
        if angle == 0:
            if y - dist <= 0:
                return True
        if angle == 45:
            if x - dist <= 0 or y - dist <= 0:
                return True
        if angle == 90:
            if x - dist <= 0:
                return True
        if angle == 135:
            if x - dist <= 0 or y + dist >= 700:
                return True
        if angle == 180:
            if y + dist >= 180:
                return True
        if angle == 225:
            if x + dist >= 700 or y + dist >= 700:
                return True
        if angle == 270:
            if x + dist >= 700:
                return True
        if angle == 315:
            if x + dist >= 700 or y -dist <= 0:
                return True

    return False
"""

#Game loop
clock = pygame.time.Clock()
running = True
while running:

    screen.fill((255,255,255))
    screen.blit(background, (0, 0))
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
    

        if event.type == pygame.KEYDOWN:
              
            if event.key == pygame.K_UP or event.key == ord('w'):
               # if not check_collision(10, 'foward', car.angle, bounding_box.pos[0]-52.5, bounding_box[1]-52.5):
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
    clock.tick(30)
    
    pygame.display.flip()
