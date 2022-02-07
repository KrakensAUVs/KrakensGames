def create_map():

    map = []

    for i in range(0, 10):
        line = []
        for j in range(0, 7):
            line.append('~')
        map.append(line)

    return map

#pesquisar melhor forma de preencher e imprimir o mapa
def print_map(map):
    line_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    column_name = ['1', '2', '3', '4', '5', '6', '7']

    print(' ', column_name)
    for i in range(0, 10):
        print(line_name[i], map[i])
    print('\n')


def menu():
    print('~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~')
    print('''   [ 1 ] Start
   [ 2 ] Instructions
   [ 3 ] Quite''')
    print('~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~')


def main():
    map1 = create_map()  #Map that will contain the boats and the Kraken
    map2 = create_map()  #Map that will be printed for the player
    print_map(map1)
    menu()
    op = int(input('Choose an option: '))
    while op != 1 and op != 2 and op != 3:
        print('\nInvalid option. Try again.')
        op = int(input('Option: '))

    if op == 1:
        #Chamar funções do jogo
        print('Jogar')

    elif op == 2:
        # Chamar a função das instruções
        print('Instruçoes')

    elif op == 3:
        print('\U0001F419 Thanks for playing \U0001F419')


main()
