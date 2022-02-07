import random
import os

# define score: aircraft carrier = 5, ship = 3, submarine = 1, water = 0, bomb = -5
# Global variables that help count game stop conditions
score = 5
cnt_emb = 0


#print the game instructions
def instructions():
    print('''Your objective is to hit all the ships without losing all your points with bombs 
    
    • The map has a total of 70 squares (board: 10x7), containing boats, water and bombs
    • When you shoot a bomb, you will lose 5 points, and you will see -5 on the map
    • If you hit the Kraken, the game ends
    • When hitting the water you lose 1 point, on the map it appears as 0
    • Vessels are marked with your score, which will be visible on the map when you hit them:
        • aircraft carrier: 5
        • ships: 3
        • submarines: 1
    • Across the ocean (board) there are 24 vessels   
    
    The game ends when the player completely sinks the squad or loses all points\n''')


def print_score():

    print(f'\nScore:{score}\n')


# receive and verify the shot, then update the maps
def get_shot(map1, map2):
    shot = [-1, -1]
    global score
    global cnt_emb

    shot[0] = int(input('~~~*Enter the coordinates of the shot*~~~\nrow:'))
    shot[1] = int(input('Column:'))

    # map starts at zero
    shot[0] = shot[0] - 1
    shot[1] = shot[1] - 1

    # while the shot is not valid
    while (shot[0] < 0 or shot[0] > 9) or (shot[1] > 6 or shot[1] < 0) or map2[shot[0]][shot[1]] == -1:
        print('\nUnavailable coordinate, try again')
        shot[0] = int(input('~~~*Enter the coordinates of the shot*~~~\nrow:'))
        shot[1] = int(input('Column:'))

        shot[0] = shot[0] - 1
        shot[1] = shot[1] - 1

    # check target

    # Update map 1 so the user can see what he's hit, update the score and print a message
    if map2[shot[0]][shot[1]] == 0:
        map1[shot[0]][shot[1]] = '0'
        print_map(map1)
        score = score - 1
        print('Just water. You lost 1 point')

    elif map2[shot[0]][shot[1]] == '\U0001F419':
        map1[shot[0]][shot[1]] = '\U0001F419'
        print_map(map1)
        print('Oh no, the Kraken\U0001F419')
        print('GAME OVER')
        score = -1

    elif map2[shot[0]][shot[1]] == -5:
        map1[shot[0]][shot[1]] = '\U0001F4A3'
        print_map(map1)
        if score >= 5:
            score = score - 5
            print('\U0001F4A3 A bomb! You lost 5 points')
        else:
            score = -1
            print('oh no, looks like you lost all the points.')

    elif map2[shot[0]][shot[1]] == 1:
        map1[shot[0]][shot[1]] = '1'
        print_map(map1)

        cnt_emb = cnt_emb - 1
        score = score + 1
        print('Hit a submarine, got a point!')

    elif map2[shot[0]][shot[1]] == 3:
        map1[shot[0]][shot[1]] = '3'
        print_map(map1)

        cnt_emb = cnt_emb - 1
        score = score + 3
        print('Hit a ship, got three points!')

    elif map2[shot[0]][shot[1]] == 5:
        map1[shot[0]][shot[1]] = '5'
        print_map(map1)

        cnt_emb = cnt_emb - 1
        score = score + 5
        print('WOW, an aircraft carrier, plus 5 points!!')

    map2[shot[0]][shot[1]] = -1  # To handle possible coordinate repetitions

    print_score()  # Update de score for the user


# Randomize the distribution of boats, bombs and Kraken
def randomize_map(map):
    c_ac = 0
    c_ship = 0
    c_sub = 0
    c_bomb = 0

    line = 10
    column = 7

    # Fills the hidden map with 0 (water)
    for i in range(line):
        row = []
        for j in range(column):
            row.append(0)
        map.append(row)

    # Distribute 6 aircraft carriers
    while c_ac < 6:
        line = random.randint(0, 9)
        column = random.randint(0, 6)

        map[line][column] = 5
        c_ac += 1

    # From here, there will be check if the random location is free ( = 0)
    # Distribute 8 ships
    while c_ship < 8:
        line = random.randint(0, 9)
        column = random.randint(0, 6)

        while map[line][column] != 0:
            line = random.randint(0, 9)
            column = random.randint(0, 6)

        map[line][column] = 3
        c_ship += 1

    #  Distribute 10 submarines
    while c_sub < 10:
        line = random.randint(0, 9)
        column = random.randint(0, 6)
        while map[line][column] != 0:
            line = random.randint(0, 9)
            column = random.randint(0, 6)

        map[line][column] = 1
        c_sub += 1

    #  Distribute 10 bombs
    while c_bomb < 10:
        line = random.randint(0, 9)
        column = random.randint(0, 6)

        while map[line][column] != 0:
            line = random.randint(0, 9)
            column = random.randint(0, 6)

        map[line][column] = -5
        c_bomb += 1

    #  randomizes the location of the kraken
    line = random.randint(0, 9)
    column = random.randint(0, 6)

    while map[line][column] != 0:
        line = random.randint(0, 9)
        column = random.randint(0, 6)

    map[line][column] = '\U0001F419'

    global cnt_emb

    #update the vessel counter
    cnt_emb = c_ac + c_sub + c_ship


# creates the map that the user will view
def create_map():

    map = []

    for i in range(0, 10):
        line = []
        for j in range(0, 7):
            line.append('~')
        map.append(line)

    return map


# Print the map with its numbered columns and rows
def print_map(map):
    line_num = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']
    column_name = ['1', '2', '3', '4', '5', '6', '7']

    print('  ', column_name)

    for i in range(0, 10):
        print(line_num[i], map[i])
    print('\n')


# Show the menu options
def menu():
    print('~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~')
    print('''   [ 1 ] Start
   [ 2 ] Instructions
   [ 3 ] Quit''')
    print('~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~')


# Keeps the main loop, where the game takes place
def main():

    # show the menu while a valid option is not entered
    menu()
    op = int(input('Choose an option: '))
    while op != 1 and op != 2 and op != 3:
        print('\nInvalid option. Try again.')
        op = int(input('Option: '))

    while op == 1 or op == 2 or op == 3:
        if op == 1:
            # map1 initialization and map2 randomize
            map1 = create_map()  # Map that will contain the boats and the Kraken
            map2 = []  # Map that will be printed for the player

            global score
            global cnt_emb

            randomize_map(map2)

            os.system('clear')

            print_map(map1)

            # As long as the player has score and ships, the game will continue.
            while score >= 0 and cnt_emb > 0:
                get_shot(map1, map2)

                # If the player find all ships, win
                if cnt_emb == 0:
                    print('WOW, you won! All enemy ships were hit!!!')

                # If the player lose all points, game over
                elif score < 0:
                    print('~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~GAME OVER~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~')

            return 0

        # show the instruction and return at menu
        elif op == 2:
            instructions()

            menu()
            op = int(input('Choose an option: '))
            while op != 1 and op != 2 and op != 3:
                print('\nInvalid option. Try again.')
                op = int(input('Option: '))

        elif op == 3:
            print('\U0001F419 Thanks for playing \U0001F419')


main()
