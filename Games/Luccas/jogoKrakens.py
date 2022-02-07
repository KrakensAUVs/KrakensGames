import pygame, random
from pygame.locals import *
from pygame import mixer

#variaveis globais
# definindo movimentos.
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

MY_KEY_UP = UP
MY_KEY_DOWN = DOWN
MY_KEY_LEFT = LEFT
MY_KEY_RIGHT = RIGHT

aux = 0

# funções


def dentroGrid():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def colisao(p1, p2):
    return (p1[0] == p2[0]) and (p1[1] == p2[1])


#definindo cores
WHITE = (255,255,255)
BLACK = (0,0,0,)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo Krakens')

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill(WHITE)
score = 0

maca_cor = RED
maca_pos = dentroGrid()
maca = pygame.Surface((10,10))
maca.fill(maca_cor)

my_direction = LEFT
nModo = 0

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)

game_over = False
my_clock = 10
while not game_over:
    clock.tick(my_clock)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#verifica movimentos
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = MY_KEY_UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = MY_KEY_DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = MY_KEY_LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = MY_KEY_RIGHT

    if colisao(snake[0], maca_pos):
        snake.append((0,0))
        if aux == 2:
            nModo = 0
            aux = 0
            my_clock = 10
            snake_skin.fill(WHITE)
        if nModo == 0:
            MY_KEY_UP = UP
            MY_KEY_DOWN = DOWN
            MY_KEY_LEFT = LEFT
            MY_KEY_RIGHT = RIGHT
            snake_skin.fill(WHITE)
        if nModo == 1:
            mixer.Sound('Passandomal.wav').play()
            aux = aux + 1
            MY_KEY_UP = DOWN
            MY_KEY_DOWN = UP
            MY_KEY_LEFT = RIGHT
            MY_KEY_RIGHT = LEFT
            snake_skin.fill(YELLOW)
        if nModo == 2:
            mixer.Sound('Tapirra.wav').play()
            aux = aux + 1
            my_clock = 30
            snake_skin.fill(BLUE)
        score = score + 1
        if (score % 5) == 0:
            nModo = random.randint(1,2)
            maca.fill(GREEN)
        else:
            maca.fill(RED)
        maca_pos = dentroGrid()

    # verifica se a cobra esta dentro dos limites
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        mixer.Sound('Bigodei.wav').play()
        break

    # verifica se a cobra colidio com ela
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            mixer.Sound('Bigodei.wav').play()
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # movimenta a cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    screen.fill(BLACK)
    screen.blit(maca, maca_pos)

# linhas horizontais
    for x in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
 # linhas verticais
    for y in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
