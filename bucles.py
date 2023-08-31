mensajes = ['ataque', 'defensa', 'retirada', 'guardia', 'extra']

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

corrimiento = int(input('Ingrese el numero de corrimiento: '))

encriptado = ''

for i in range(len(mensajes)): 
    mensaje = mensajes[i]
    for j in range(len(mensaje)):

        encriptado = encriptado + alfabeto[(alfabeto.index(mensaje[j]) + corrimiento) % 27]

        if(j == len(mensaje) - 1):
            print(encriptado)

    encriptado = ''  