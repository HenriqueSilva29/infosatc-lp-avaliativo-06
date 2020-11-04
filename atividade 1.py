#O método abs () retorna o valor absoluto do número fornecido.
# Exemplo : 
# integer = -20
#print('Absolute value of -20 is:', abs(integer))

numero=0
lista = [2,4,6,8]


def rotacionar(lista, numero):
    numero=int(input("Algum número positivo ou negativo :"))
    if numero >= 0:
        for i in range(numero):
            ultimoNumero = lista.pop(-1)
            lista.insert(0, ultimoNumero)
    else:
        for i in range(abs(numero)):
            primeiroNumero = lista.pop(0)
            lista.append(primeiroNumero)
            return

rotacionar(lista, numero)
print (lista) 
    

