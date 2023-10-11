# 2. Faça um programa que solicite dois
# números ao usuário e exiba o maior deles.

numero1 = int(input('Digite o primeiro Número: '))
numero2 = int(input('Digite o segundo Número: '))

# 1 - primeiro é maior
# 2 - segundo é maior
# 3 - são iguais

if numero1 > numero2:
    print('O primeiro número é maior!')
elif numero2 > numero1:
    print('O segundo número é maior!')
else:
    print('Os números são iguais!')