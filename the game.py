from pygame import *
from random import *
import pygame
import random
import pickle


height = 640
width = 800


fenetre = display.set_mode((width,height))
display.set_caption("Sweet Idyll")


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('songs\song5.wav')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

#les spritesheets
perso0 = image.load('3.png') 
perso1 = image.load('4.png')
perso2 = image.load('1.png')
perso3 = image.load('2.png')
perso = [perso0,perso1,perso2,perso3]

        
#les objets etc
donut = [image.load('Donut1.png'),image.load('golden donut.png')]
playbutton = [image.load('buttons\play button.png'),image.load('buttons\play button activated.png')]
son = [image.load('buttons\son on.png'),image.load('buttons\son off.png'),image.load('buttons\son on activated.png'),image.load('buttons\son off activated.png')]
back = image.load('nul.png')
clouds = [image.load('cloud.png'),image.load('cloud2.png'),image.load('cloud3.png')]
map = image.load('nul.png')
select = image.load('select.png')
pause_button = [image.load('buttons\pause button.png'),image.load('buttons\pause2.png')]


#vies
vies = [image.load('4 vies.png'),image.load('3 vies.png'),image.load('2 vies.png'),image.load('1 vie.png')]
vie = 0
xvie,yvie = width-300,6



#On associe les touches aux images
imageSprite = {K_UP:[perso[1]],
               K_LEFT:[perso[2]],
               K_DOWN:[perso[0]],
               K_RIGHT:[perso[3]],}
 
#paramètres de départ
jouer = True
engaged = False
unpressed = True
game_paused = False
pressed = True
clock = pygame.time.Clock()
direction = K_UP
vitesse = 5
goldendonut = 0
z = 0
index_img = 0

with open('mypicklefile', 'r') as f1:
    f1.read()


#clouds
xcloud1,ycloud1 = -220,150
xcloud2,ycloud2 = xcloud1 - width,90
xcloud3,ycloud3 = xcloud2 - 550,150

#title
title = 'sweet idyll'
undertitle = "designed with paint"
Font_title = pygame.font.Font('pixeled.ttf',60)
Font_undertitle = pygame.font.Font('pixeled.ttf',20)
title_blit = [Font_title.render(title,False,(255,255,0)),Font_title.render(title,False,(115,251,253)),Font_title.render(title,False,(237,28,36))]

size = pygame.Surface.get_size(title_blit[0])
title_l = size[0] + 10
title_h = size[1]

xt0 = (width - title_l)/2
xt1,xt2 = xt0 - 5,xt0 + 5
yt0 = yt1 = yt2 = height/6
print(xt0+100)
undertitle_blit = Font_undertitle.render(undertitle,False,(0,255,0))
xt,yt = xt0,yt0 + title_h - 30

#pause
size = pygame.Surface.get_size(pause_button[0])
pause_l = size[0]
pause_h = size[1]
xpause = width - pause_l - 30 
ypause = height - pause_h - 30
p =  0

#sons
size = pygame.Surface.get_size(son[0])
son_l = size[0]
son_h = size[1]
size = pygame.Surface.get_size(son[3])
son2_l = size[0]
son2_h = size[1]
xson,yson = xt0,height - son_h - 20
a = 0
    #intro
playlist = ['songs\song1.wav','songs\song2.wav','songs\song3.wav','songs\song5.wav','songs\song6.wav','songs\song8.wav','songs\song9.wav','songs\song10.wav','songs\song11.wav','songs\song12.wav',]

#score
score = 0
Font_score = pygame.font.Font('pixeled.ttf',30)
score_txt = ""
score_blit = Surface
xscore,yscore = width - 305,30

    #game paused
        #restart
Font_restart = pygame.font.Font('pixeled.ttf',30)
restart_txt = "RESTART"
restart_blit = [Font_restart.render(restart_txt,False,(255,255,0)),Font_restart.render(restart_txt,False,(115,251,253)),Font_restart.render(restart_txt,False,(237,28,36))]

size = pygame.Surface.get_size(restart_blit[0])
restart_l = size[0]
restart_h = size[1]
xrestart0 = (width - restart_l)/2
xrestart1,xrestart2 = xrestart0  - 5, xrestart0 + 5
yrestart = height/3
        #home
Font_home = pygame.font.Font('pixeled.ttf',30)
home_txt = "HOME"
home_blit = [Font_home.render(home_txt,False,(255,255,0)),Font_home.render(home_txt,False,(115,251,253)),Font_home.render(home_txt,False,(237,28,36))]

size = pygame.Surface.get_size(restart_blit[0])
home_l = size[0]
home_h = size[1]
xhome0 = xrestart0 + home_l/4
xhome1,xhome2 = xhome0  - 5, xhome0 + 5
yhome = yrestart + 100

#bouton
size = pygame.Surface.get_size(playbutton[0])
button_l = size[0]
button_h = size[1]
size = pygame.Surface.get_size(playbutton[1])
button2_l = size[0]
button2_h = size[1]
xPb0,yPb0 = (width/2) - button_l/2 ,height*(2/3) - 60 

xPb1,yPb1 = xPb0 - (button2_l - button_l)/2,yPb0 - (button2_h - button_h)/2
xPb,yPb = xPb0,yPb0
ib = 0

#donuts
size = pygame.Surface.get_size(donut[0])
donut_l = size[0]
donut_h = size[1]
XDonut1,XDonut2 = randint(5,width - donut_l - 5),randint(5,width - donut_l - 5)
YDonut1 =  YDonut2 = -height
c = 3
c2 = 2




#cloud
def cloud():
    global xcloud1,ycloud1,xcloud2,ycloud2,xcloud3,ycloud3,clouds

    #cloud 1
    if xcloud1 < width:
        xcloud1 += 1
    else:
        xcloud1 = -2*width

    #cloud 2
    if xcloud2 < width:
        xcloud2 += 1
    else:
        xcloud2 = -2*width

    #cloud 3
    if xcloud3 < width:
        xcloud3 += 1
    else:
        xcloud3 = -2*width

    

    fenetre.blit(clouds[0],(xcloud1,ycloud1))
    fenetre.blit(clouds[1],(xcloud2,ycloud2))
    fenetre.blit(clouds[2],(xcloud3,ycloud3))

#affichage de départ
def start_screen():
    global a,ib,xson,yson
    if ib == 1:
        xPb,yPb = xPb1,yPb1 
    else:
        xPb,yPb = xPb0,yPb0
    
    if a == 2 or a == 3:
        xson,yson = xt0 + 100 - (son2_l - son_l)/2,yPb0 + (button_h - son2_h)/2
    else:
        xson,yson = xt0 + 100,yPb0 + (button_h - son_h)/2

    fenetre.blit(map,(0,0))
    cloud()
    fenetre.blit(playbutton[ib],(xPb,yPb))
    fenetre.blit(son[a],(xson,yson))
    #titre
    fenetre.blit(title_blit[1],(xt1,yt1))
    fenetre.blit(title_blit[2],(xt2,yt2))
    fenetre.blit(title_blit[0],(xt0,yt0))
    fenetre.blit(undertitle_blit,(xt,yt))
    display.flip()
    
start_screen()

    
#premier plan
def premier_plan():
    global xson,yson,events,a,unpressed

    
    if events.type == pygame.MOUSEMOTION or events.type == pygame.FINGERMOTION:
        coordonnes = pygame.mouse.get_pos()  
        if (xson < coordonnes[0] < (xson + son_l)) and (yson < coordonnes[1] < (yson + son_h)):
            xson,yson = 40 - (son2_l - son_l)/2,40 - (son2_h - son_h)/2
            if a == 0:
                a = 2
            elif a == 1:
                a = 3
        else:
            xson,yson = 40,40
            if a == 2:
                a = 0
            elif a == 3:
                a = 1
    if events.type == pygame.MOUSEBUTTONDOWN:
        unpressed = True
    if events.type == pygame.MOUSEBUTTONUP or events.type == pygame.FINGERUP:
            coordonnes = pygame.mouse.get_pos()
            if unpressed:
                if (xson < coordonnes[0] < (xson + son_l)) and (yson < coordonnes[1] < (yson + son_h)):

                    if a == 0 or a == 2:
                        a = 3
                    else:
                        a = 2
                    
                    unpressed = False

    fenetre.blit(son[a],(xson,yson))
    fenetre.blit(score_blit[0],(xscore,yscore))
    fenetre.blit(score_blit[1],(xscore - 5,yscore))
    fenetre.blit(pause_button[p],(xpause,ypause))
    

def curseur_son():
    global events,a
    #curseur sur le son
    if events.type == pygame.MOUSEMOTION or events.type == pygame.FINGERMOTION:
        coordonnes = pygame.mouse.get_pos()  
        if (xson < coordonnes[0] < (xson + son_l)) and (yson < coordonnes[1] < (yson + son_h)):
            if a == 0:
                a = 2
            elif a == 1:
                a = 3
        else:
            if a == 2:
                a = 0
            elif a == 3:
                a = 1
                    
#player
size = pygame.Surface.get_size(perso[0])
player_l = size[0]
player_h = size[1]

y_lim = (height - player_h) - 20

xPlayer,yPlayer = (width/2) - player_l/2,y_lim
 
#les fonctions du jeu
    #fonction pour déplacer le perso
def deplacementPerso():
    global xPlayer,yPlayer,direction,index_img
    if k[K_LEFT]: 
        direction = K_LEFT
        if xPlayer <= -player_l:
            xPlayer = width
        else:
            xPlayer = xPlayer - vitesse
    elif k[K_RIGHT]:
        direction = K_RIGHT
        if xPlayer >= width:
            xPlayer = -player_l
        else:
            xPlayer = xPlayer + k[K_RIGHT]*vitesse
    elif k[K_DOWN]:
        direction = K_DOWN
        if yPlayer >= y_lim:
            yPlayer = yPlayer
        else:
            yPlayer = yPlayer + k[K_DOWN]*vitesse
    else:
        direction = K_UP

#fonction défilement
    #positions donut niveau 1 de difficulté
def falling_donuts():
    global YDonut1,YDonut2,XDonut1,XDonut2,c,c2
    

  

    #Donut 1
    if YDonut1 < height:
        YDonut1 += c
    else:
        YDonut1 = -donut_h
        XDonut1 = randint(5,width - donut_l - 5)
        c = randint(3,8)

    #Donut 2
    if YDonut2 < height:
        YDonut2 += c2
    else:
        YDonut2 = -donut_h
        XDonut2 = randint(5,width - donut_l - 5)
        c2 = randint(3,8)
        
        

    
    fenetre.blit(donut[0],(XDonut1,YDonut1))
    fenetre.blit(donut[0],(XDonut2,YDonut2))



    #collisions
def check_collisions():
    global c,c2,yPlayer,xPlayer,player_h,YDonut1,XDonut1,YDonut2,XDonut2,donut_h,score,score_blit,score_txt,game_over
    if goldendonut == 3:
        pts = 5
    else:
        pts = 1
    if ((yPlayer + 2 <= (YDonut1 + donut_h) <= (yPlayer + player_h)) or (yPlayer + 2 <= YDonut1 <= (yPlayer + player_h))) and (( XDonut1 <= (xPlayer + player_l) <= (XDonut1 + donut_l)) or (XDonut1 <= xPlayer <= (XDonut1 + donut_l))) :
        score += pts
        YDonut1 = -5*donut_h
        XDonut1 = randint(5,width - donut_l - 5)
        c = randint(3,8)

    elif YDonut1 > yPlayer:
        game_over = True

    if ((yPlayer + 2 <= (YDonut2 + donut_h) <= (yPlayer + player_h)) or (yPlayer + 2 <= YDonut2 <= (yPlayer + player_h))) and (( XDonut2 <= (xPlayer + player_l) <= (XDonut2 + donut_l)) or (XDonut2 <= xPlayer <= (XDonut2 + donut_l))) :
        score += pts
        YDonut2 = -5*donut_h
        XDonut2 = randint(5,width - donut_l - 5)
        c2 = randint(3,8)
    elif YDonut2 > yPlayer:
        game_over = True

    score_txt = "SCORE : "+ str(score)
    score_blit = [Font_score.render(score_txt,False,(115,251,253)),Font_score.render(score_txt,False,(255,255,255))]

#game screen
def game_screen():
    fenetre.blit(back,(0,0))
    fenetre.blit(imageSprite[direction][index_img],(xPlayer,yPlayer))

#game over screen
def pause():
    game_screen()
    premier_plan()
    global events,game_paused,engaged,p,score,XDonut1,XDonut2,YDonut1,YDonut2,xcloud1,xcloud2,c,c2,xPlayer,xson,yson
    if events.type == pygame.MOUSEMOTION or events.type == pygame.FINGERMOTION or events.type == pygame.MOUSEBUTTONDOWN or events.type == pygame.MOUSEBUTTONUP:
        coordonnes = pygame.mouse.get_pos()  
        if (xrestart0 < coordonnes[0] < (xrestart0 + restart_l)) and (yrestart < coordonnes[1] < (yrestart + restart_h)):
            xselect = xrestart0 - 60
            yselect = yrestart + 25
            fenetre.blit(select,(xselect,yselect))
        elif (xhome0 < coordonnes[0] < (xhome0 + home_l)) and (yhome < coordonnes[1] < (yhome + home_h)):
            xselect = xhome0 - 60
            yselect = yhome + 25
            fenetre.blit(select,(xselect,yselect))
           
        else:
            game_screen()
            premier_plan()


        if events.type == pygame.MOUSEBUTTONUP or events.type == pygame.FINGERUP: 
            coordonnes = pygame.mouse.get_pos()
            if (xhome0 < coordonnes[0] < (xhome0 + home_l)) and (yhome < coordonnes[1] < (yhome + home_h)):
                game_paused = False
                engaged = False
                p = 0
                score = 0
                XDonut1,XDonut2 = randint(5,width - donut_l - 5),randint(5,width - donut_l - 5)
                YDonut1 =  YDonut2 = -height
                c = 3
                c2 = 2
                xPlayer = (width/2) - player_l/2
                pygame.mixer.music.stop()
                pygame.mixer.music.load('songs\song8.wav')
                pygame.mixer.music.play(0,0,4000)

            elif (xrestart0 < coordonnes[0] < (xrestart0 + restart_l)) and (yrestart < coordonnes[1] < (yrestart + restart_h)):
                game_paused = False
                engaged = True
                p = 0
                score = 0
                XDonut1,XDonut2 = randint(5,width - donut_l - 5),randint(5,width - donut_l - 5)
                YDonut1 =  YDonut2 = -height
                c = 3
                c2 = 2
                xPlayer = (width/2) - player_l/2
                xson,yson = 40,40
                pygame.mixer.music.stop()
                pygame.mixer.music.load(random.choice(playlist))
                pygame.mixer.music.play(0,0,4000)
    #restart
    fenetre.blit(restart_blit[1],(xrestart1,yrestart))
    fenetre.blit(restart_blit[2],(xrestart2,yrestart))
    fenetre.blit(restart_blit[0],(xrestart0,yrestart))

    #home
    fenetre.blit(home_blit[1],(xhome1,yhome))
    fenetre.blit(home_blit[2],(xhome2,yhome))
    fenetre.blit(home_blit[0],(xhome0,yhome))
    
    display.flip()


#boucle jeu             
while jouer:
    for events in event.get():
        if events.type == QUIT:
            quit()

    #son
    
    if a == 1 or a == 3:
        pygame.mixer.music.set_volume(0)
    elif pygame.mixer.music.get_volume() == 0:
        pygame.mixer.music.set_volume(0.2)
    if pygame.mixer.music.get_busy() != True:
        pygame.mixer.init()
        pygame.mixer.music.load(random.choice(playlist))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)

    
    
    if engaged:
        k = key.get_pressed()
        game_screen()
        falling_donuts()
        check_collisions()
        deplacementPerso()
        premier_plan()
        #click sur pause
        if events.type == pygame.MOUSEBUTTONDOWN or events.type == pygame.FINGERDOWN:
            pressed = True

        if events.type == pygame.MOUSEBUTTONUP or events.type == pygame.FINGERUP:
            coordonnes = pygame.mouse.get_pos()
            if pressed:
                if (xpause < coordonnes[0] < (xpause + pause_l)) and (ypause < coordonnes[1] < (ypause + pause_h)):

                    if p == 0:
                        p = 1
                    else:
                        p = 0
                    game_paused = True
                    engaged = False
                    pressed = False


        display.flip()
    elif game_paused:
        pause()

        #click sur pause
        if events.type == pygame.MOUSEBUTTONDOWN or events.type == pygame.FINGERDOWN:
            pressed = True

        if events.type == pygame.MOUSEBUTTONUP or events.type == pygame.FINGERUP:
            coordonnes = pygame.mouse.get_pos()
            if pressed:
                if (xpause < coordonnes[0] < (xpause + pause_l)) and (ypause < coordonnes[1] < (ypause + pause_h)):

                    if p == 0:
                        p = 1
                    else:
                        p = 0
                    game_paused = False
                    engaged = True
                    pressed = False
        display.flip()
    else:
        start_screen()
        curseur_son()       
        display.flip()
        if events.type == pygame.MOUSEMOTION or events.type == pygame.FINGERMOTION:
            coordonnes = pygame.mouse.get_pos()
            if (xPb < coordonnes[0] < (xPb + button_l)) and (yPb < coordonnes[1] < (yPb + button_h)):
                ib = 1
            else:
                ib = 0

        #click sur le playbutton/son
        if events.type == pygame.MOUSEBUTTONDOWN or events.type == pygame.FINGERDOWN:
            unpressed = True
            coordonnes = pygame.mouse.get_pos()
            if (xPb < coordonnes[0] < (xPb + button_l)) and (yPb < coordonnes[1] < (yPb + button_h)):
                engaged = True
                xson,yson = 40,40

        if events.type == pygame.MOUSEBUTTONUP or events.type == pygame.FINGERUP:
            coordonnes = pygame.mouse.get_pos()
            if unpressed:
                if (xson < coordonnes[0] < (xson + son_l)) and (yson < coordonnes[1] < (yson + son_h)):

                    if a == 0 or a == 2:
                        a = 3
                    else:
                        a = 2
                    
                    unpressed = False
        
            

clock.tick(25)
