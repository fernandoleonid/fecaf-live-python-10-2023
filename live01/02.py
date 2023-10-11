# Uma empresa quer calcular o salário de seus 
# funcionários com base em sua carga horária 
# semanal e o valor da hora de trabalho. 
# Além disso, a empresa oferece um bônus 
# de 10% para aqueles funcionários que 
# trabalharem mais de 40 horas por semana.

carga_horaria = int(input('Digite sua carga horária: '))
valor_hora = float(input('Digite seu valor hora: '))

salario_bruto = carga_horaria * valor_hora

if carga_horaria > 40:
    salario_bruto *= 1.10

print (f'Seu salário é: {salario_bruto:.2f}')