


import os, sys, pygame

from pygame.rect import Rect

pygame.init()
screen_width=1000
screen_height= 600
player_width=10
player_height=20
player_x=screen_width/2-player_width/2
player_y= screen_height-player_height-10
player_speed=2
player_jumpdecay=0.3
player_jumpstrength=14
player_jumpPower=0
gravity_multiplier=5
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("python testi")
drawables=[]


def make_platform (pos_x,pos_y,platform_width,platform_height):
    drawables.append(pygame.Rect(pos_x,pos_y,platform_width,platform_height))

clock= pygame.time.Clock()
i=0

make_platform(0,500,400,20)
def check_col(rect1,rect2):
    return pygame.Rect(rect1).colliderect(pygame.Rect(rect2))
def check_colAndRep(checkAgainst) :
     t=0
     while (t<len(drawables)) :
        if(check_col(drawables[t],checkAgainst)):
            return drawables[t]
        t+=1
        
   

while True:
    playerRect=pygame.Rect(player_x,player_y,player_width,player_height)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    dir1=pygame.Vector2(0,0)
    collider=check_colAndRep(playerRect)
    if collider is not None :
        vec1=pygame.Vector2(player_x,player_y)
        cord=collider.centerx,collider.y
        vec2=pygame.Vector2(cord)
        dirvec=vec1-vec2
        dirvecnorm=pygame.Vector2.normalize(dirvec)
        print(dirvecnorm)
        print(abs(dirvecnorm.x),abs(dirvecnorm.y))
            
    keys=pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]and player_x>0 :
        if collider is None or abs(dirvecnorm.x)<0.999 :
            player_x-=player_speed
    if keys[pygame.K_RIGHT]and player_x <screen_width- player_width:
        if collider is None or abs(dirvecnorm.x)<0.999 :
            player_x+= player_speed
    if keys[pygame.K_UP] and player_y>0 and player_jumpPower<=0:
    
            player_jumpPower=player_jumpstrength
    
    if  player_jumpPower>0  :
        if collider is not None:
            if dirvecnorm.y<0 :
                player_y-=player_jumpPower
        else :
            player_y-=player_jumpPower
    elif (check_col(drawables[0],playerRect)) :
        print("col")
       # player_y-=player_height/3
  
    if player_y<screen_height-player_height :
            if collider is not None :
                if dirvecnorm.y>0 :
                    player_y+=gravity_multiplier
            else :
                player_y+=gravity_multiplier 

    player_jumpPower-= player_jumpdecay
    screen.fill((163,154,164))
   
   
    
    while (len( drawables)>i) :
    
        pygame.draw.rect(screen,(100,30,30),drawables[i])
        i+=1

    i=0
   
    pygame.draw.rect(screen,(0,128,255),playerRect)
    pygame.display.flip()
    clock.tick(90)

