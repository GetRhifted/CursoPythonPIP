def calculadora_de_edad():
    año_actual = 2023
    contador = 0
    resultados = []
    while contador < 3:
        entrada = input('Dime tu nombre y año de nacimiento separados por una coma: ')
        nombre, año_nacimiento = entrada.split(',')
        edad = año_actual - int(año_nacimiento.strip())
        mensaje = f"¡Hola {nombre.strip()}! Este año de curso cumplirás {edad} años."
        resultados.append(mensaje)
        contador += 1
    return resultados

print(calculadora_de_edad())


