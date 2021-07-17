# simulação de plantação de melancia
'''
i (erva daninha) = capinar -> 20% de semente


'''

import curses

LIN = 25
COL = 50

curses.initscr()

curses.beep()
curses.beep()

window = curses.newwin(LIN, COL, 0, 0)
window.keypad(1)
window.border('X', 'X', 'X', 'X')

def irrigar(agua):
    if(agua > 0):
        lin = input('IRRIGAR[linha]: ')
        col = input('IRRIGAR[coluna]: ')
        
        if((matriz[lin][col] == ' ') and (lin < 25) and (col < 50)):        # :(
            matriz[lin][col] = '~'
            agua--
        else:
            print ('\nATENCAO: Posicao invalida ou ja ocupada!\n')
    else:
        print('\nATENCAO: Sem saldo de agua!\n')
    

