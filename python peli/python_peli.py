
import os, sys, pygame
pygame.init()
screen_width=1000
screen_height= 600
player_width=10
player_height=20
player_x=screen_width//2-player_width//2
player_y= screen_height-player_height-10
player_speed=2
player_jumpdecay=0.2
player_jumpstrength=6
player_jumpPower=0
gravity_multiplier=4
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("python testi")

clock= pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]and player_x>0:
        player_x-=player_speed
    if keys[pygame.K_RIGHT]and player_x <screen_width- player_width:
        player_x+= player_speed
    if keys[pygame.K_UP] and player_y>0 and player_jumpPower<=0:
        player_jumpPower=player_jumpstrength

    if player_jumpPower>0 :
         player_y-=player_jumpPower
    else: 
        if player_y<screen_height-player_height:
            player_y+=gravity_multiplier

    player_jumpPower-= player_jumpdecay
       

    screen.fill((163,154,164))
    pygame.draw.rect(screen,(0,128,255),(player_x,player_y,player_width,player_height))
    pygame.display.flip()
    clock.tick(90)

