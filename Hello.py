print('Hola desde mi maquina')

def counter_word(text):
    word = 'a'
    counter = 0
    for i in text:
        if i.lower() == word:
            counter += 1
    return counter

print(counter_word('Azulaaaaaaa'))

def reversed_word(text):
    texto_inverso = ''
    for l in text:
        texto_inverso = l + texto_inverso
    return texto_inverso

print(reversed_word('Estoy Aprendiendo a Programar'))

def mayor_num(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(mayor_num(45,56))


def mayot_num_3(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    
print(mayot_num_3(67,97,46))


def calcular_longitud(cadena):
    counter = 0
    for l in cadena:
        if l != ' ':
            counter += 1
    return counter
  
        

print(calcular_longitud('Era se una vez en la mancha'))


def vocal_meter(caracter):
    if caracter in 'aeiouAEIOU':
        return True
    return False
    
print(vocal_meter('P'))


def generar_n_caracteres(caracter,n):
    return caracter * n

print(generar_n_caracteres('j',17))