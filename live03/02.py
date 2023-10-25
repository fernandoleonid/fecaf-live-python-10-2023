# Crie um programa que solicite ao usuário 
# uma lista de números inteiros até  
# o limite do usuário.

lista_numeros = []

# lista_numeros.append('Fernando')
# lista_numeros.insert(2, 'Hugo')

# lista_numeros.pop()
# lista_numeros.remove('Ana')

# print (len(lista_numeros))

# print(lista_numeros)

# print ('Hugo' in lista_numeros)

resposta = 's'
while resposta == 's':
    numero = input('Digite um número: ')
    lista_numeros.append(numero)
    resposta = input('Deseja continuar [s/n]: ')

print (lista_numeros)