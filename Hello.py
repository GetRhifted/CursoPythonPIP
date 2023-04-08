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
