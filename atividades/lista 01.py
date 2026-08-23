'''
QUESTAO 01

numerador = int(input("Digite um numero:    "))
denominador = int(input("Digite outro numero:    "))
if numerador % denominador == 0:
    print("O numero é par")
else:
    print("O numero é impar")
'''
# -----------------------------------------------------------------------------------------
'''
QUESTAO 02

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    print(numero1)
else:
    print(numero2)
'''
# -----------------------------------------------------------------------------------------
'''
QUESTAO 03

letra = input("Digite uma letra: ").strip().lower()
if len(letra) != 1 or not letra.isalpha():
    print("Digite apenas uma letra")
elif letra in "aeiou":
    print(f"Sua letra {letra} é uma vogal")
else:
    print(f"Sua letra {letra} é uma consoante")
'''
# -----------------------------------------------------------------------------------------
'''
QUESTAO 04

nota = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota + nota2) / 2

if media == 10:
    print("Aprovado com distinção!")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
'''
# -----------------------------------------------------------------------------------------
'''
QUESTÃO 05

n = int(input("Digite um número: "))
n_2 = int(input("Digite outro número: "))
n_3 = int(input("Digite o terceiro número: "))

maior = n

if n_2 > maior:
    maior = n_2
if n_3 > maior:
    maior = n_3

print(maior)
'''
# -----------------------------------------------------------------------------------------
'''
QUESTAO 06

turno = input("Olá, em qual turno você estuda?\n M - matutino\n V - vespertino\n N - noturno\n Digite: ").upper()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print ("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")
else:
    print("Valor Inválido!")
'''
# -----------------------------------------------------------------------------------------
'''
QUESTÃO 07

perguntas = 0
print("Olá, você é supeito de um crime, responda as perguntas com sim ou não para o seu veredito.")

a = input("Telefonou para a vítima? ").lower()
if a == 'sim':
    perguntas += 1

b = input("Esteve no local do crime? ").lower()
if b == 'sim':
    perguntas += 1

c = input("Mora perto da vítima? ").lower()
if c == 'sim':
    perguntas += 1

d = input("Devia para a vítima? ").lower()
if d == 'sim':
    perguntas += 1

e = input("Já trabalhou com a vítima? ").lower()
if e == 'sim':
    perguntas += 1

if perguntas == 5:
    print("Culpado! Você é o ASSASSINO.")
elif perguntas >= 3:
    print("Culpado! Você foi CÚMPLICE.")
elif perguntas == 2:
    print("Você é SUSPEITO! A investigação vai continuar.")
else:
    print("Você é INOCENTE")
'''