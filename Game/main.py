import random

opciones = ('Piedra', 'Papel', 'Tijeras')
rounds = 1
cpu_wins = 0
user_wins = 0

while True:

  print('*' * 20)
  print('ROUND', rounds)
  print('*' * 20)

  print('Puntos - Tú:', user_wins)
  print('Puntos - CPU:', cpu_wins)

  user_option = input('Vamos a jugar al piedra, papel, tijeras, elige uno! ')

  rounds += 1

  user_option = user_option.capitalize()
  if not user_option in opciones:
    print(
      'Lo siento, parece que esa no es una opcion valida. Volvamos a intentarlo!'
    )
    continue

  cpu_option = random.choice(opciones)
  if user_option.capitalize == cpu_option:
    print('Esto es un empate, sigamos jugando!')
  elif user_option == 'Piedra':
    if cpu_option == 'Tijeras':
      print('CPU eligio Tijeras!')
      print('Piedra le gana a Tijeras!')
      print('You Won!')
      user_wins += 1
    else:
      print('CPU eligio Papel!')
      print('Papel le gana a la Piedra!')
      print('You Lose!')
      cpu_wins += 1
  elif user_option == 'Papel':
    if cpu_option == 'Tijeras':
      print('CPU eligio Tijeras!')
      print('Tijeras le gana a Papel!')
      print('You Lose!')
      cpu_wins += 1
    else:
      print('CPU eligio Piedra!')
      print('Papel le gana a la Piedra!')
      print('You Won!')
      user_wins += 1
  elif user_option == 'Tijeras':
    if cpu_option == 'Papel':
      print('CPU eligio Papel!')
      print('Tijeras le gana a Papel!')
      print('You Won!')
      user_wins += 1
    else:
      print('CPU eligio Piedra!')
      print('Piedra le gana a Tijeras!')
      print('You Lose!')
      cpu_wins += 1

  if cpu_wins == 2:
    print('CPU ha ganado!')
    print('Gracias por jugar, espero lo volvamos a hacer pronto!')
    break
  if user_wins == 2:
    print('Felicitaciones, has ganado!')
    print('Gracias por jugar, espero lo volvamos a hacer pronto!')
    break