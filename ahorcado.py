from random import choice

lista_palabras = ['perro', 'gato', 'gallo', 'rata', 'pajaro', 'mapache', 'hamster', 'vibora', 'raton']
letras_incorrectas = []
letras_correctas = []
intentos = 6
aciertos = 0
juego_terminado = False
vidas = 7

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

def letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
        letra_elegida = input('Introduzca una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No haz elegido una letra correcta')
    return letra_elegida

def mostrar_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))

def chequeo_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has encontrado esa letra, intenta con otra')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -=1

    if vidas == 0:
        fin = perder()
        print('¡Ya no le quedan vidas, se terminó el juego!')
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    
    return vidas, fin, coincidencias

def perder():
    print('Te has quedado sin vidas')
    print('La palabra era '+palabra)
    return True

def ganar(palabra_descubierta):
    mostrar_tablero(palabra_descubierta)
    print('Felicitaciones! Has encontrado la palabra!')
    return True

palabra, letras_unicas = elegir_palabra(lista_palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_tablero(palabra)
    print('\n')
    print('Letras incorrectas: '+'-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letras = letra()

    intentos, terminado, aciertos = chequeo_letra(letras, palabra, intentos, aciertos)

    juego_terminado = terminado