# Pygame Tutorial Episode 4 | Animating Our Character

import pygame
import sys

pygame.init()

root = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Pygame Tutorial")


images_left = [pygame.image.load("assets/Run__001L.png"),
                   pygame.image.load("assets/Run__002L.png"),
                   pygame.image.load("assets/Run__003L.png"),
                   pygame.image.load("assets/Run__004L.png"),
                   pygame.image.load("assets/Run__005L.png"),
                   pygame.image.load("assets/Run__006L.png"),
                   pygame.image.load("assets/Run__007L.png"),
                   pygame.image.load("assets/Run__008L.png"),
                   pygame.image.load("assets/Run__009L.png")]

images_right = [pygame.image.load("assets/Run__001.png"),
                    pygame.image.load("assets/Run__002.png"),
                    pygame.image.load("assets/Run__003.png"),
                    pygame.image.load("assets/Run__004.png"),
                    pygame.image.load("assets/Run__005.png"),
                    pygame.image.load("assets/Run__006.png"),
                    pygame.image.load("assets/Run__007.png"),
                    pygame.image.load("assets/Run__008.png"),
                    pygame.image.load("assets/Run__009.png")]



run = True

pos_x = 30
pos_y = 400
width = 80
height = 100
velocity = 10
is_jump = False
jump_velocity = 15
walkCount = 0
facing_right = False
facing_left = False

clock = pygame.time.Clock()

bg_image = pygame.image.load("assets/bg.jpg")


def load_screen():
    global root, walkCount

    root.blit(bg_image, dest=(0,0))

    if walkCount > 8:
        walkCount = 0


    if facing_right:
        image = images_right[walkCount]
    elif facing_left:
        image = images_left[walkCount]
    else:
        image = pygame.image.load("assets/Idle__001.png")



    root.blit(image,dest=(pos_x,pos_y))
    pygame.display.update()




while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                is_jump = True
        

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and pos_x <= root.get_width() - width:
        pos_x += velocity
        walkCount += 1
        facing_right = True
        facing_left = False
 
    if keys[pygame.K_LEFT] and pos_x >=0 :
        pos_x -= velocity
        walkCount +=1
        facing_left = True
        facing_right = False


    if keys[pygame.K_DOWN] and pos_y + height <= root.get_height():
        facing_left= False
        facing_right = False
        walkCount = 0




    if is_jump:
        pos_y -= jump_velocity
        pygame.time.delay(8)
        jump_velocity -= 1
        if jump_velocity < -15:
            is_jump = False
            jump_velocity = 15


    load_screen()

    
