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
car_img = pygame.image.load('GUI_Images/car3.png')
car_x = 17.5
car_y = 577.5
car_center_x = car_x + 52.5
car_center_y = car_y + 52.5
car_x_change = 0
car_y_change = 0

#for turning(not yet implemented)
car_orientation = 0
rotate_angle = 0

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

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
    

    
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
       
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                print("left")
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

            if event.key == pygame.K_e:
                car_img = rot_center(car_img, -45)
            
            if event.key == pygame.K_q:
                car_img = rot_center(car_img, 45)


        

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a\
            or event.key == pygame.K_RIGHT or event.key == pygame.K_d\
            or event.key == pygame.K_UP or event.key == pygame.K_w\
            or event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                print("key released")
                car_x_change = 0
                car_y_change = 0

    #moving one unit
    if car_x_change != 0:
        if (car_x + car_x_change)>=0 and (car_x + car_x_change)<=595:
            car_x += car_x_change
            car_x_change = 0 
        else:
            car_x_change = 0 
            print("collision with boundary")
        
        car_center_x = car_x + 52.5
        car_center_y = car_y + 52.5

        print("corner coordinates: {}, {}".format(car_x, car_y))
        print("center coordinates: {}, {}".format(car_center_x, car_center_y))

    if car_y_change != 0:
        if (car_y + car_y_change)>=0 and (car_y + car_y_change)<=595:
            car_y += car_y_change
            car_y_change = 0 
        else:
            car_y_change = 0 
            print("collision with boundary")
        
        car_center_x = car_x + 52.5
        car_center_y = car_y + 52.5

        print("corner coordinates: {}, {}".format(car_x, car_y))
        print("center coordinates: {}, {}".format(car_center_x, car_center_y))


    
    

    
    clock.tick(30)

    car(car_x, car_y)
    pygame.display.update()
