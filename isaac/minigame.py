import pygame
from random import random, randrange
import time

window = pygame.display.set_mode((600, 600))    # resolução 600x600

# cores: RGB 
branco = (255, 255, 255)
preto = (0, 0, 0)
cinza = (50, 50, 50)
cinza_claro = (150, 150, 150)
vermelho = (255, 0, 0)
vermelho_escuro = (170, 0, 0)
verde = (0, 255, 0)
verde_escuro = (0, 170, 0)
azul = (0, 0, 255)
azul_escuro = (0, 0, 170)
amarelo = (255, 255, 0)
amarelo_escuro = (170, 170, 0)

# função para inicializar o tabuleiro
def inicializa(window):
    window.fill(branco)
    pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(window, preto, (100, 295, 400, 5))
    pygame.draw.rect(window, preto, (295, 100, 5, 400))
    pygame.draw.circle(window, branco, (300, 300), 300, 100)
    pygame.draw.circle(window, preto, (300, 300), 200, 8)
    pygame.draw.circle(window, preto, (300, 300), 90)
    pygame.draw.circle(window, cinza, (300, 300), 60)
    pygame.display.update()

def botao_verde(window):
    window.fill(branco)
    pygame.draw.rect(window, verde, (100, 100, 200, 200))
    pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(window, preto, (100, 295, 400, 5))
    pygame.draw.rect(window, preto, (295, 100, 5, 400))
    pygame.draw.circle(window, branco, (300, 300), 300, 100)
    pygame.draw.circle(window, preto, (300, 300), 200, 8)
    pygame.draw.circle(window, preto, (300, 300), 90)
    pygame.draw.circle(window, cinza, (300, 300), 60)
    pygame.display.update()

def botao_vermelho(window):
    window.fill(branco)
    pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(window, vermelho, (300, 100, 200, 200))
    pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(window, preto, (100, 295, 400, 5))
    pygame.draw.rect(window, preto, (295, 100, 5, 400))
    pygame.draw.circle(window, branco, (300, 300), 300, 100)
    pygame.draw.circle(window, preto, (300, 300), 200, 8)
    pygame.draw.circle(window, preto, (300, 300), 90)
    pygame.draw.circle(window, cinza, (300, 300), 60)
    pygame.display.update()

def botao_amarelo(window):
    window.fill(branco)
    pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(window, amarelo, (100, 300, 200, 200))
    pygame.draw.rect(window, preto, (100, 295, 400, 5))
    pygame.draw.rect(window, preto, (295, 100, 5, 400))
    pygame.draw.circle(window, branco, (300, 300), 300, 100)
    pygame.draw.circle(window, preto, (300, 300), 200, 8)
    pygame.draw.circle(window, preto, (300, 300), 90)
    pygame.draw.circle(window, cinza, (300, 300), 60)
    pygame.display.update()

def botao_azul(window):
    window.fill(branco)
    pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(window, azul, (300, 300, 200, 200))
    pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(window, preto, (100, 295, 400, 5))
    pygame.draw.rect(window, preto, (295, 100, 5, 400))
    pygame.draw.circle(window, branco, (300, 300), 300, 100)
    pygame.draw.circle(window, preto, (300, 300), 200, 8)
    pygame.draw.circle(window, preto, (300, 300), 90)
    pygame.draw.circle(window, cinza, (300, 300), 60)
    pygame.display.update()            

def botao_inicio(window):
    window.fill(branco)
    pygame.draw.rect(window, verde_escuro, (100, 100, 200, 200))
    pygame.draw.rect(window, vermelho_escuro, (300, 100, 200, 200))
    pygame.draw.rect(window, azul_escuro, (300, 300, 200, 200))
    pygame.draw.rect(window, amarelo_escuro, (100, 300, 200, 200))
    pygame.draw.rect(window, preto, (100, 295, 400, 5))
    pygame.draw.rect(window, preto, (295, 100, 5, 400))
    pygame.draw.circle(window, branco, (300, 300), 300, 100)
    pygame.draw.circle(window, preto, (300, 300), 200, 8)
    pygame.draw.circle(window, preto, (300, 300), 90)
    pygame.draw.circle(window, cinza_claro, (300, 300), 60)
    pygame.display.update()


# fonte
pygame.font.init()
fonte = pygame.font.SysFont("arial", 30)

# variáveis 
click_on_off = 0
gameSeq = []
colorRepeat = 0
response = []       # 0 = verde; 1 = vermelho; 2 = amarelo; 3 = azul

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # mouse
    mouse = pygame.mouse.get_pos()

    # click do mouse
    click = pygame.mouse.get_pressed()

    # repetição das cores
    if colorRepeat == 1:
        inicializa(window)
        time.sleep(1)
        for i in range(len(gameSeq)):
            if gameSeq[i] == 0:
                botao_verde(window)
            if gameSeq[i] == 1:
                botao_vermelho(window)
            if gameSeq[i] == 2:
                botao_amarelo(window)
            if gameSeq[i] == 3:
                botao_azul(window)
            time.sleep(1)
            inicializa(window)
            time.sleep(0.5)
        colorRepeat = 0

    # lógica
    if response == gameSeq and gameSeq != []:
        colorRepeat = 1
        gameSeq.append(randrange(4))
        response = []
    
    if len(response) > 0 and len(gameSeq) > 0 and response[len(response) -1] != gameSeq[len(response) - 1] and gameSeq != []:
        pygame.quit()

    # posições do mouse -> brilhar quando passar em cima dos botões
    if (mouse[0] - 300)**2 + (mouse[1] - 300)**2 <= 40000 and (mouse[0] - 300)**2 + (mouse[1] - 300)**2 >= 8100 and 100 <= mouse[0] <= 300 and 100 <= mouse[1] <= 300:
        botao_verde(window)
        if click[0] == 0 and click_on_off == 1:
            response.append(0)
    elif (mouse[0] - 300)**2 + (mouse[1] - 300)**2 <= 40000 and (mouse[0] - 300)**2 + (mouse[1] - 300)**2 >= 8100 and 300 <= mouse[0] <= 500 and 100 <= mouse[1] <= 300:
        botao_vermelho(window)
        if click[0] == 0 and click_on_off == 1:
            response.append(1)
    elif (mouse[0] - 300)**2 + (mouse[1] - 300)**2 <= 40000 and (mouse[0] - 300)**2 + (mouse[1] - 300)**2 >= 8100 and 100 <= mouse[0] <= 300 and 300 <= mouse[1] <= 500:
        botao_amarelo(window)
        if click[0] == 0 and click_on_off == 1:
            response.append(2)
    elif (mouse[0] - 300)**2 + (mouse[1] - 300)**2 <= 40000 and (mouse[0] - 300)**2 + (mouse[1] - 300)**2 >= 8100 and 300 <= mouse[0] <= 500 and 300 <= mouse[1] <= 500:
        botao_azul(window)
        if click[0] == 0 and click_on_off == 1:
            response.append(3)
    elif (mouse[0] - 300)**2 + (mouse[1] - 300)**2 <= 3600:
        botao_inicio(window)
        if click[0] == 0 and click_on_off == 1:
                colorRepeat = 1
                gameSeq.append(randrange(4))
                response = []
    else:
        inicializa(window)

    click_on_off = click[0]

    pygame.display.update()