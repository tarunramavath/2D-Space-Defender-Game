import pygame
import sys
from button import Button
import math
from pygame import mixer
import random
pygame.init()
mixer.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Defender")
color=['#ff0800','#eeff00','#ffa600']
BG = pygame.image.load("images/bg.png")
def get_font1(size):
    return pygame.font.Font("Ahutapersonaluse.ttf", size)
def get_font2(size):
    return pygame.font.Font("NovaSquareSlim-Book.ttf", size)
def get_font(size): 
    return pygame.font.Font("GCRANK.TTF", size)
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        enemy=['images/alien1.png','images/alien2.png','images/alien3.png','images/alien4.png','images/alien10.png','images/alien6.png','images/alien7.png','images/alien8.png','images/alien9.png']
        mixer.music.load('sounds/background.wav')
        mixer.music.play(-1)
        screen=pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Space Defender')
        icon=pygame.image.load('images/icon.png')
        pygame.display.set_icon(icon)
        background=pygame.image.load('images/bg.png')
        spaceshipimg=pygame.image.load('images/arcade.png')
        alienimg=[]
        alienX=[]
        alienY=[]
        alienspeedX=[]
        alienspeedY=[]
        no_of_aliens=5
        for i in range(no_of_aliens):
            alienimg.append(pygame.image.load(random.choice(enemy)))
            alienX.append(random.randint(30,500))
            alienY.append(random.randint(30,150))
            alienspeedX.append(-1)
            alienspeedY.append(40)
        score=0
        bulletimg=pygame.image.load('images/bullet.png')
        check=False
        bulletX=386
        bulletY=490

        spaceshipX=370
        spaceshipY=480
        changeX=0
        running=True
        font=pygame.font.SysFont('Arial',32,'bold')
        def score_text():
            img=font.render(f'Score:{score}',True,'white')
            screen.blit(img,(10,10))
        font_gameover=pygame.font.SysFont('Arial',64,'bold')
        def gameover():
                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                img_gameover = font_gameover.render('GAME OVER', True,"white" )
                screen.blit(img_gameover, (200, 200))          
                PLAY_BACK = Button(image=None, pos=(380, 330), 
                                    text_input="REPLAY", font=get_font(50), base_color="Green", hovering_color="Green")
                PLAY_BACK.changeColor(PLAY_MOUSE_POS)
                PLAY_BACK.update(SCREEN)
                QUIT_BUTTON = Button(image=None, pos=(380, 410), 
                                    text_input="QUIT", font=get_font(50), base_color="Red", hovering_color="Red")
                QUIT_BUTTON.changeColor(PLAY_MOUSE_POS)
                QUIT_BUTTON.update(SCREEN)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                            play()
                        if QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
        pygame.display.update()
        while running:
            screen.blit(background,(0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        changeX=-5
                    if event.key==pygame.K_RIGHT:
                        changeX=5
                    if event.key==pygame.K_SPACE:
                        if check is False:
                            bulletSound=mixer.Sound('sounds/laser.wav')
                            bulletSound.play()
                            check=True
                            bulletX=spaceshipX+16
                    if event.type==pygame.KEYUP:
                        changeX=0
            spaceshipX+=changeX  
            if spaceshipX<=0:
                spaceshipX=0
            elif spaceshipX>=736:
                spaceshipX=736
            for i in range(no_of_aliens):
                if alienY[i] > 420:
                    for j in range(no_of_aliens):
                        alienY[j] = 2000
                        gameover()        
                alienX[i]+=alienspeedX[i]
                if alienX[i]<=0:
                    alienspeedX[i]=1
                    alienY[i]+=alienspeedY[i]
                if alienX[i]>=736:
                    alienspeedX[i]=-1
                    alienY[i]+=alienspeedY[i]
                distance = math.sqrt(math.pow(bulletX - alienX[i], 2) + math.pow(bulletY - alienY[i], 2))
                if distance < 27:
                    explosion= mixer.Sound('sounds/explosion.wav')
                    explosion.play()
                    bulletY = 480
                    check = False
                    alienX[i] = random.randint(0, 736)
                    alienY[i] = random.randint(30, 150)
                    score += 1
                screen.blit(alienimg[i], (alienX[i], alienY[i]))
            if bulletY<=0:
                bulletY=490
                check=False
            if check:
                screen.blit(bulletimg, (bulletX, bulletY))
                bulletY-=5
            screen.blit(spaceshipimg, (spaceshipX, spaceshipY))
            score_text()
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay.checkForInput(PLAY_MOUSE_POS):
                    play()
        pygame.display.update()
        exit()
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        GAME_NAME = get_font1(100).render("SPACE DEFENDER", True,"White")
        GAME_RECT = GAME_NAME.get_rect(center=(400,150))
        PLAY_BUTTON = Button(image=None, pos=(380, 275), 
                            text_input="PLAY", font=get_font(50), base_color="Green", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(380, 400), 
                            text_input="QUIT", font=get_font(50), base_color="Red", hovering_color="Red")
        SCREEN.blit(GAME_NAME, GAME_RECT)
        for button in [PLAY_BUTTON,QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()
