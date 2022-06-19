"""
Exercicio 1
Implementacao do algortimo para imprimir e somar todos
os numeros menores ou iguais a um determinado numero
"""
x = input("Escreva um numero inteiro maior que 0: ")
y = 0
for i in range(1, int(x) + 1):
    y = y + i
    print('i=', i, '\ty=', y)

print('Total=', y)
