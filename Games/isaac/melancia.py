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

