def practice():
  name = input('¿Cual es tu nombre? ')
  name = name.capitalize()
  age = int(input('Indicamen tu edad '))
  year = 2023 - age + 100
  print(name, ', si te cuidas bien, llegaras a tener 100 años en', year)
  
  
  number = int(input('Dime un numero! '))
  if number % 2 == 0:
    print('Este es un numero par!')
  elif number % 4 == 0:
    print('Este es un numero par!')
    print('Ademas, es multiplo de 4!')
  else:
    print('Este es un numero impar!')
    
if __name__ == '__main__':
  practice()   