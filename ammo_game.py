import pygame
import time
import math
pygame.init()


clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Ammo Khandeh")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
#
background_img = pygame.image.load('background.png')
#bullet
bullet_state = 0
bullet_img = []
bullet_img.append(pygame.image.load('bullet.png'))
bullet_img.append(pygame.image.load('fire.png'))
bullet_img.append(pygame.image.load('light.png'))
bullet_img.append(pygame.image.load('knife.png'))
bullet_img.append(pygame.image.load('bullet.png'))
bullet_type = 10
bullet_y=-100
bullet_y_constant = -100
bullet_x=0
bullet_y_movment = 2
#
save_pos = 100
num_player = 4
#character 
playerimg = []
playerimg.append(pygame.image.load('player1.png'))
playerimg.append(pygame.image.load('player2.png'))
playerimg.append(pygame.image.load('player3.png'))
playerimg.append(pygame.image.load('player4.png'))

#player abbilty

player_abbilityimg = []
player_abbilityimg.append(pygame.image.load('player1_abbility.png'))
player_abbilityimg.append(pygame.image.load('player2_abbility.png'))
player_abbilityimg.append(pygame.image.load('player3_abbility.png'))
player_abbilityimg.append(pygame.image.load('player4_abbility.png'))

explosionimg=pygame.image.load('explosion.png')

player_x = []
player_y = []
player_live = []
player_abbility = []
player_live = []



for i in range(8):
    player_abbility.append(0)
for i in range(num_player):
    player_live.append(2)


#player1
player_x.append(20)
player_y.append(300)
#player2
player_x.append(200)
player_y.append(300)
#player3
player_x.append(820)
player_y.append(300)
#player4
player_x.append(1000)
player_y.append(300)

player_rect =[]
for i in range(num_player):
    player_rect.append(pygame.Rect(player_x[i],player_y[i],170,260))


#time
source_time= time.time()
total_person_time = 60
time_passed=0

player_button = []
for i in range(num_player):
    player_button.append(pygame.Rect(player_x[i]+4,227,68,52))
    player_button.append(pygame.Rect(player_x[i]+76,227,68,52))

time_image=0

def name_show():
    name_font = pygame.font.Font("Vazir-Bold.ttf",30)
    leftplayer_name_rend=name_font.render("ﺎﺿﺮﯿﻠﻋ ",True,(0,0,0))
    screen.blit(leftplayer_name_rend,(20,16))
    leftplayer_name_rend=name_font.render("ﺎﯾﺩﺮﺑ ",True,(0,0,0))
    screen.blit(leftplayer_name_rend,(1115,16))
def time_show(t):
    time_font = pygame.font.Font("Vazir-Bold.ttf",40)
    time = time_font.render(" : ﻥﺎﻣﺯ  ",True,(0,0,0))
    time_sec = time_font.render(str(t),True,(0,0,0))
    screen.blit(time,(580,3))
    screen.blit(time_sec,(500,6))
def player(x,y,i):
    #charachter
    screen.blit(playerimg[i],(x,y))
    #abbility
    screen.blit(player_abbilityimg[i],(x,y-100))

def shot(x,y,i):
    screen.blit(bullet_img[i],(x,y))

def damage_effect(pos):
    screen.blit(explosionimg,(player_x[save_pos],player_y[save_pos]))
        
running = True
while running:
    screen.blit(background_img,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for i in range(8):
                state_local1=0
                for k in range(8):
                    if player_abbility[k] == 1 or player_abbility[k] == 2 or player_abbility[k] == 3 or player_abbility[i]==4 or bullet_y > 250:
                        state_local1 +=1
                        print(player_abbility[k])
                if player_button[i].collidepoint(x,y) :
                    if state_local1 == 0:
                        print(state_local1)
                        player_abbility[i] = 1
            for i in range(8):
                if player_abbility[i] == 1:
                    if i < 4:
                        j=2
                    elif i > 3 :
                        j=0
                    if player_rect[j].collidepoint(x,y) and player_live[j] > 0 :
                        player_abbility[i] = 2
                        save_pos= j
                        if i == 0 or i==2 or i== 4 or i == 6 :
                            bullet_type = 0
                        if i == 1 :
                            bullet_type = 1
                        if i == 3 :
                            bullet_type = 2
                        if i == 5 :
                            bullet_type = 3           
                        if i == 7 :
                            bullet_type = 4        
                    j += 1
                    if player_rect[j].collidepoint(x,y) and player_live[j] > 0 :
                        save_pos = j
                        player_abbility[i] = 2
                        if i == 0 or i==2 or i== 4 or i == 6 :
                            bullet_type = 0
                        if i == 1 :
                            bullet_type = 1
                        if i == 3 :
                            bullet_type = 2
                        if i == 5 :
                            bullet_type = 3           
                        if i == 7 :
                            bullet_type = 4
                        
    
    now_time=time.time()
    time_passed=math.trunc(total_person_time-(now_time-source_time))
    time_show(time_passed)
    name_show()
    for i in range(num_player):    
        player(player_x[i],player_y[i],i)
    for i in range(8):
        if player_abbility[i] == 2:
            bullet_y = -100
            bullet_y_movment = 2
            player_abbility[i] = 3
            if save_pos == 0:
                bullet_x = 70 + player_x[0]
            if save_pos == 1:
                bullet_x = 70 + player_x[1]
            if save_pos == 2:
                bullet_x = 70 + player_x[2]
            if save_pos == 3:
                bullet_x = 70 +player_x[3]
    for i in range(8):
        if player_abbility[i] == 3:
            bullet_y += bullet_y_movment 
            shot(bullet_x,bullet_y,bullet_type)
            if bullet_y > 250 :
                player_abbility[i] = 4 
                player_live[save_pos] -= 1
                bullet_x=0
                bullet_y=2000
                bullet_y_movment = 0        
        if player_abbility[i] == 4:
            if time_image < 220:
                time_image +=1
                damage_effect(save_pos)
            else:
                bullet_y = bullet_y_constant
                time_image = 0
                player_abbility[i]=5
    pygame.display.update()
    clock.tick(60)