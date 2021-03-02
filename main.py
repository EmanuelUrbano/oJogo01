import pygame,sys, keyword

import pygame.mixer

from PySimpleGUI import PySimpleGUI as sg

pygame.init()

altura = 600
largura = 1230
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((largura,altura), 0, 32)

font = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 70)
font3 = pygame.font.Font("Gameplay.ttf", 150)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)


def collisaEsquerdaParedeVertical(de, ate, px, pos_x, pos_y):
    for i in range(de,ate):
        if pos_x == px and pos_y == i:
            pos_x += 10
    return pos_x

def collisaDireitaVertical(de, ate, px, pos_x, pos_y):
    for i in range(de,ate):
        if pos_x == px and pos_y == i:
            pos_x -= 10
    return pos_x

def collisaCimaHorizontal(de, ate, py, pos_x, pos_y):
    for i in range(de,ate):
        if pos_x == i and pos_y == py:
            pos_y += 10
    return pos_y
def collisaBaixoHorizontal(de, ate, py, pos_x, pos_y):
    for i in range(de,ate):
        if pos_x == i and pos_y == py:
            pos_y -= 10
    return pos_y

def main_menu():
    seta_px = 190
    seta_py = 300


    while True:

        color_text1 = 225,225,225
        color_text2 = 225,225,225

        if seta_px == 190 and seta_py == 420:
            color_text2 = 106,20,245

        if seta_px == 190 and seta_py == 300:
            color_text1 = 106,20,245

        screen.fill((5,0,205))

        clique = pygame.mixer.Sound("clique_2.wav")
        seta = pygame.image.load("seta-removebg-preview.png")
        draw_text("Start", font2, (color_text1), screen, 265, 300)
        draw_text("Options", font2, (color_text2), screen, 265, 420)
        draw_text("O Jogo", font3, (225,225,225), screen, 70,50)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_e:
                    if seta_px == 190 and seta_py == 300:
                        clique.play()
                        game()
                    if seta_px == 190 and seta_py == 420:
                        clique.play()
                        options()

                if event.key == pygame.K_DOWN:
                    seta_py = 420


                if event.key == pygame.K_UP:
                    seta_py = 300





        draw_text("Start", font2, (color_text1), screen, 265, 300)
        draw_text("Options", font2, (color_text2), screen, 265, 420)
        screen.blit(seta,(seta_px, seta_py))
        pygame.display.update()
        mainClock.tick(60)


def GUI():
    o = True
    while o:


        screen.fill((5,0,205))
        draw_text("VIDA:", font2, (225,225,225),screen, 44,56)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    o = False 


        pygame.display.update()
        mainClock.tick(60)






def game():
    vel = 10
    anim = 0
    home = pygame.image.load("images\home.png")
    IdleDonw = pygame.image.load("images\spritesTestes\imagem_1.png")
    IdleLeft = pygame.image.load("images\spritesTestes\imagem_4.png")
    IdleUp = pygame.image.load("images\spritesTestes\imagem_7.png")
    IdleRigth = pygame.image.load("images\spritesTestes\imagem_10.png")
    animImgDonw = ["images\spritesTestes\imagem_1.png", "images\spritesTestes\imagem_2.png", "images\spritesTestes\imagem_1.png","images\spritesTestes\imagem_3.png"]
    animImgLeft = ["images\spritesTestes\imagem_4.png", "images\spritesTestes\imagem_5.png","images\spritesTestes\imagem_4.png","images\spritesTestes\imagem_6.png"]
    animImgUP = ["images\spritesTestes\imagem_7.png", "images\spritesTestes\imagem_8.png","images\spritesTestes\imagem_7.png","images\spritesTestes\imagem_9.png"]
    animImgRight = ["images\spritesTestes\imagem_10.png", "images\spritesTestes\imagem_11.png","images\spritesTestes\imagem_10.png","images\spritesTestes\imagem_12.png"]
    pos_x = 340
    pos_y = 130

    vida = 30
    vidaS = "Vida: "


    dire = [animImgDonw,animImgLeft,animImgRight,animImgUP]
    çao = 0


    character = pygame.image.load("images\spritesTestes\imagem_1.png")

    screen.blit(home, (0,0))
    screen.blit(character,(pos_x, pos_y))

    running = True
    while running:
        screen.fill((0,0,0))
        keys = pygame.key.get_pressed()
        character = pygame.image.load(dire[çao][0]) 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 

                if event.key == pygame.K_m:
                    GUI()






        if keys[pygame.K_LEFT]:
            pos_x -= vel
            anim += 1
            çao = 1
            if anim == 4:
                anim = 0 
            character = pygame.image.load(animImgLeft[anim])

        if keys[pygame.K_RIGHT]:
            pos_x += vel
            anim += 1
            çao = 2
            if anim == 4:
                anim = 0 
            character = pygame.image.load(animImgRight[anim])

        if keys[pygame.K_UP]:
            pos_y -= vel
            anim += 1
            çao = 3
            if anim == 4:
                anim = 0 

            character = pygame.image.load(animImgUP[anim])

        if keys[pygame.K_DOWN]:
            pos_y += vel
            anim += 1
            çao = 0
            if anim == 4:
                anim = 0 
            character = pygame.image.load(animImgDonw[anim]) 




        if pos_x >= 640:
            pos_x -= 10
        if pos_y >= 420:
            pos_y -= 10
        if pos_x <= 30:
            pos_x += 10
        if pos_y <= 70:
            pos_y += 10


        pos_y = collisaCimaHorizontal(40, 310,330, pos_x, pos_y)
        pos_x = collisaEsquerdaParedeVertical(340,360, 250,pos_x,pos_y)
        pos_y = collisaCimaHorizontal(200, 250,360,pos_x,pos_y)
        pos_x = collisaEsquerdaParedeVertical(340, 380, 210,pos_x,pos_y)
        pos_y = collisaCimaHorizontal(160,210, 380,pos_x,pos_y)
        pos_x = collisaDireitaVertical(340,390, 150, pos_x,pos_y)
        pos_y = collisaCimaHorizontal(40, 80, 380, pos_x,pos_y)
        pos_x = collisaEsquerdaParedeVertical(240,330, 310,pos_x,pos_y)
        pos_x = collisaEsquerdaParedeVertical(340,360, 110,pos_x,pos_y)

        screen.blit(home, (0,0))
        draw_text(vidaS+"{}".format(vida), font2, (225,225,225),screen, 30, 30)
        screen.blit(character,(pos_x, pos_y))
        pygame.display.update()
        mainClock.tick(10)
        print(pos_y, pos_x)

        pygame.display.update()

def carto():
    terrp = pygame.image.load("quart-fer.png")
    terrp = pygame.transform.scale(terrp, (900, 720))
    vel = 10
    anim = 0
    IdleDonw = pygame.image.load("images\spritesTestes\imagem_1.png")
    IdleLeft = pygame.image.load("images\spritesTestes\imagem_4.png")
    IdleUp = pygame.image.load("images\spritesTestes\imagem_7.png")
    IdleRigth = pygame.image.load("images\spritesTestes\imagem_10.png")
    animImgDonw = ["images\spritesTestes\imagem_1.png", "images\spritesTestes\imagem_2.png", "images\spritesTestes\imagem_1.png","images\spritesTestes\imagem_3.png"]
    animImgLeft = ["images\spritesTestes\imagem_4.png", "images\spritesTestes\imagem_5.png","images\spritesTestes\imagem_4.png","images\spritesTestes\imagem_6.png"]
    animImgUP = ["images\spritesTestes\imagem_7.png", "images\spritesTestes\imagem_8.png","images\spritesTestes\imagem_7.png","images\spritesTestes\imagem_9.png"]
    animImgRight = ["images\spritesTestes\imagem_10.png", "images\spritesTestes\imagem_11.png","images\spritesTestes\imagem_10.png","images\spritesTestes\imagem_12.png"]
    pos_x = 450 + 20
    pos_y = 500 - 50

    dire = [animImgDonw,animImgLeft,animImgRight,animImgUP]
    çao = 0


    voltar = range(410, 470)
    cara = pygame.image.load("cara_1.png")
    cara = pygame.transform.scale(cara,(60, 70))
    character = pygame.image.load("images\spritesTestes\imagem_4.png")
    screen.blit(terrp, (0,0))
    screen.blit(character,(pos_x, pos_y))

    running = True
    while running:
        screen.fill((0,0,0))
        keys = pygame.key.get_pressed()
        character = pygame.image.load(dire[çao][0]) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if keys[pygame.K_LEFT]:
            pos_x -= vel
            anim += 1
            çao = 1
            if anim == 4:
                anim = 0 
            character = pygame.image.load(animImgLeft[anim])

        if keys[pygame.K_RIGHT]:
            pos_x += vel
            anim += 1
            çao = 2
            if anim == 4:
                anim = 0 
            character = pygame.image.load(animImgRight[anim])

        if keys[pygame.K_UP]:
            pos_y -= vel
            anim += 1
            çao = 3
            if anim == 4:
                anim = 0 
            character = pygame.image.load(animImgUP[anim])

        if keys[pygame.K_DOWN]:
            pos_y += vel
            anim += 1
            çao = 0
            if anim == 4:
                anim = 0 
            character = pygame.image.load(animImgDonw[anim]) 

        for tel in voltar:
            if pos_y == tel and pos_x == 510:
                running = False
                game()


        if pos_x >= 520:
            pos_x -= 10
        if pos_y <= 120:
            pos_y += 10
        if pos_x <= 180:
            pos_x += 10
        if pos_y >= 520:
            pos_y -= 10

        screen.blit(terrp, (0,0))
        screen.blit(cara,(290,230))
        screen.blit(character,(pos_x, pos_y))
        pygame.display.update()
        mainClock.tick(10)
        print(pos_y, pos_x)
        pygame.display.update()

def options():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text("options", font, (255,255,255), screen, 40, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 
        pygame.display.update()
        mainClock.tick(60)
def battle():
    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 
        pygame.display.update()
        mainClock.tick(10)

main_menu() 
