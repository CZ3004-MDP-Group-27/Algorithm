import pygame

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

#Car
car_img = pygame.image.load('GUI_Images/Car.png')
car_x = 17.5
car_y = 577.5
car_x_change = 0
car_y_change = 0

#for turning(not yet implemented)
car_orientation = 0
rotate_angle = 0


def car(x,y):
    screen.blit(car_img,(x, y))

def move_up(car_y, pos):
    if car_y > pos:
        return car_y - 0.1
    if car_y == pos:
        return car_y
    

 

#Game loop
clock = pygame.time.Clock()
running = True
while running:

    screen.fill((255,255,255))
    screen.blit(background, (0, 0))
    
    new_pos = 560
    
    
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        
       
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                print("left")
                print(car_x)
                car_x_change -= 17.5
               
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                print("right")
                car_x_change += 17.5
            if event.key == pygame.K_UP or event.key == pygame.K_w: 
                print("up")
                car_y_change -= 17.5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                print("down")
                car_y_change += 17.5
        

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a\
            or event.key == pygame.K_RIGHT or event.key == pygame.K_d\
            or event.key == pygame.K_UP or event.key == pygame.K_w\
            or event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                print("key released")
                car_x_change = 0
                car_y_change = 0

    #check new coordinates
    if car_x_change != 0:
        print("new corner coordinates: {}, {}".format(car_x+car_x_change, car_y))
        car_center_x = car_x + car_x_change + 52.5
        car_center_y = car_y + 52.5
        print("new center coordinates: {}, {}".format(car_center_x, car_center_y))

    if car_y_change !=0:
        print("new corner coordinates: {}, {}".format(car_x, car_y+car_y_change))
        car_center_x = car_x + 52.5
        car_center_y = car_y + car_y_change + 52.5
        print("new center coordinates: {}, {}".format(car_center_x, car_center_y))


    #moving one unit in selected direction
    if (car_x + car_x_change)>=0 and (car_x + car_x_change)<=595:
        car_x += car_x_change
        car_x_change = 0 
    
    if (car_x + car_x_change)<0 or (car_x + car_x_change)>595:
        car_x_change = 0 
        print("collision with boundary")
    
    if (car_y + car_y_change)>=0 and(car_y + car_y_change)<=595:
        car_y += car_y_change
        car_y_change = 0

    if (car_y + car_y_change)<0 or (car_y + car_y_change)>595:
        car_y_change = 0 
        print("collision with boundary")

    
    clock.tick(120)

    car(car_x, car_y)
    pygame.display.update()