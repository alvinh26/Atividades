'''
QUESTAO 01

numero = 0
while numero <= 100:
    print(numero)
    numero += 1
'''
#---------------------------------------------------------------------------------------
'''
QUESTÃO 02

numero = 0
n = int(input("Insira o limite: "))

while numero <= n:
    print(numero)
    numero += 1
'''
#--------------------------------------------------------------------------------------
'''
QUESTÃO 03
print("OPERAÇÃO - ADIÇÃO")

rep = 'S'
while rep == 'S':

    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    n = a+b

    print(f"A soma: {a} + {b} = {n}")

    rep = input("Deseja realizar mais uma soma? (S ou N)\n Resposta: ").upper()

print("Programa encerrado.")
'''
#--------------------------------------------------------------------------------------
'''
QUESTÃO 01 - DESAFIO

a, b = 0,1

while a <= 500:
    print(a)
    a,b = b, a+b
'''
#--------------------------------------------------------------------------------------
'''
QUESTÃO 02 - DESAFIO

numeros = []
n = int(input("Digite a quantidade de números do conjunto: "))

for i in range(n):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)
soma = menor + maior

print(f"\n O maior número é: {maior}")
print(f"\n O menor número é: {menor}")
print(f"\n A soma dos dois é: {soma}")
'''
#--------------------------------------------------------------------------------------
'''
QUESTÃO 03 - DESAFIO

numeros = []
n = int(input("Digite a quantidade de números do conjunto: "))

for i in range(n):
    while True:
        numero = int(input("Digite um número: "))
        if 0 <= numero <= 1000:
            break
        else:
            print("Número inválido! Digite novamente.")
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)
soma = menor + maior

print(f"\n O maior número é: {maior}")
print(f"\n O menor número é: {menor}")
print(f"\n A soma dos dois é: {soma}")
'''
#--------------------------------------------------------------------------------------
'''
QUESTÃO 04 - DESAFIO

nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("Nome inválido! Digite novamente.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade <= 0 or idade > 150:
    print("Idade inválida! Digite novamente.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: R$ "))
while salario <= 0:
    print("Salário inválido! Digite novamente.")
    salario = float(input("Digite seu salário: R$ "))

sex = input("Digite seu sexo (F ou M): ").lower()
while sex not in ('f', 'm'):
    print("Sexo inválido! Digite novamente.")
    sex = input("Digite seu sexo (F ou M): ").lower()

estado_civil = input("Digite seu estado civil (S, C, V, D): ").lower()
while estado_civil not in ('s', 'c', 'v','d'):
    print("Estado civil inválido! Digite novamente.")
    estado_civil = input("Digite seu estado civil (S, C, V, D): ").lower()

dados = [nome, idade, salario, sex, estado_civil]
print(f"\n Lista com os dados: \n{dados}")
'''
#--------------------------------------------------------------------------------------
'''
QUESTÃO 05 - DESAFIO

numero = int(input("Digite um número: "))

if numero < 2:
    print(f"{numero} não é primo.")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
'''