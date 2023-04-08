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


