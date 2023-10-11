# 4 - Crie um programa que gere uma tabuada,
# onde o usuário poderá determinar o início 
# e fim da tabuada.

numero = int(input('Digite um número para a tabuada: '))
inicio =  int(input('Em qual número quer iniciar: '))
fim =  int(input('Em qual número quer terminar: '))


for contador in range(inicio, fim + 1):
    resultado = contador * numero
    print(f'{contador} x {numero} = {resultado}')