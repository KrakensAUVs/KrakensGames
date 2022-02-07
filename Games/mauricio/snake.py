# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting

import curses, sys
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

VALID_OPTIONS = [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]
WIDTH = 80
HEIGHT = 20
FOODS = ['@', '$', '%', '&']


def init_game():
    curses.initscr()
    win = curses.newwin(HEIGHT, WIDTH, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    snake = [[1,10], [1,9], [1,8]]                                    
    food = [int(HEIGHT/2), int(WIDTH/2)]          
    
    win.addch(food[0], food[1], get_fruit()) 

    score = 0
    key = KEY_RIGHT

    return win, snake, food, score, key

def get_fruit():
    return FOODS[randint(0, len(FOODS) - 1)]

def player_input(win, key, prevKey):
    prevKey = key                                              
    event = win.getch()
    key = key if event == -1 else event 
    if key == ord(' '):                                        
        key = -1                                                   
        while key != ord(' '):
            key = win.getch()
        key = prevKey
    alive = False if key == 27 else True
    if key not in VALID_OPTIONS:   
        key = prevKey
    return key, prevKey, alive

def update_snake(snake, key, diff):
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])    
    snake, alive = check_bounds(snake, diff)
    if alive:
        alive = False if snake[0] in snake[1:] else True
    return snake, alive

def check_bounds(snake, diff):
    if snake[0][0] == 0: snake[0][0] = HEIGHT - 2
    if snake[0][1] == 0: snake[0][1] = WIDTH - 2
    if snake[0][0] == HEIGHT - 1: snake[0][0] = 1
    if snake[0][1] == WIDTH - 1: snake[0][1] = 1
    return snake, True

def update_screen(snake, food, score, win):
    if snake[0] == food:                                           
        food = []
        score += 1
        while food == []:
            food = [randint(1, HEIGHT - 1), randint(1, WIDTH - 1)]         
            if food in snake: food = []  
        win.addch(food[0], food[1], get_fruit())
    else:    
        last = snake.pop()                                         
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')
    return food, score

def main():
    diff = sys.argv[1] if len(sys.argv) > 1 else 0
    win, snake, food, score, key = init_game()
    prevKey = None
    alive = True
    while alive:
        win.border(0)
        win.addstr(0, int(WIDTH/2), f" Score : {score} ")                                 
        win.timeout(int(200 - (len(snake)/20)%100))
        key, prevKey, alive = player_input(win, key,prevKey)
        if alive:
            snake, alive = update_snake(snake, key, diff)
            food, score = update_screen(snake, food, score, win)
    
    curses.endwin()
    print(f"Score - {score}")

main()