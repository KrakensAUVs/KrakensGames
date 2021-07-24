from random import choice 

with open('palavras.txt') as arquivo:
  linhas = arquivo.read()
  listaPalavras = linhas.split('\n')

palavra = choice(listaPalavras).upper()

forca = """
____
    |
    |
    -
"""

vazio = """
    

"""

cabeca = """
    O
"""

tronco = """
    O
    |
"""

bracoe = """
    O
   /|
"""

bracod = """
    O
   /|\\
"""

pernae = """
    O
   /|\\
   /
"""

pernad = """
    O
   /|\\
   / \\
"""

morreu = """
    X
   /|\\
   / \\
"""

boneco = [vazio, cabeca, tronco, bracoe, bracod, pernae, pernad, morreu]

acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''

while acertos != len(palavra) and erros != 6:
  mensagem = ''
  print(forca+boneco[erros])
  for letra in palavra:
    if letra in letras_acertadas:
      mensagem += f'{letra} '
    else:
      mensagem += '_ '
  print(mensagem)

  print('As letras que você acertou são: ' + letras_acertadas)
  print('As letras que você errou são: ' + letras_erradas)

  letra = input('Digite uma letra: ').upper()
  
  if letra in palavra:
    if letra not in letras_acertadas:
      letras_acertadas += letra
      print('Você acertou a letra!')
      acertos += palavra.count(letra)
    else:
      print('Você já digitou essa letra. Ao todo, você já tentou as seguintes letras: ' + letras_acertadas+letras_erradas)
  else:
    print('Você errou a letra...')
    letras_erradas += letra
    erros += 1

if acertos == len(palavra):
  print('Parabéns! Você conseguiu acertar a palavra')
else:
  print('Infelizmente, você se enforcou...')
  print(forca+boneco[7])
