""" Como um exercício, escreva um laço que
percorra a lista anterior e exiba o comprimento de cada
elemento.
O que acontece se você manda um inteiro para
len? """

lista_1 = ["spam!" , 1 , ['Brie', 'Roquefort', 'Pol lê Veq'], [1,2,3]]
i = 0

while i < len(lista_1):
    print (len(lista_1[i]))
    i = i + 1
