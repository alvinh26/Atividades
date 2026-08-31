'''
REVISAO - Q 1

n = int(input("Digite um número: "))
listaimpar = []
listapar = []

for i in range(1, n + 1):
    if i % 2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)

print("Números pares:", listapar)
print("Números ímpares:", listaimpar)
'''
#--------------------------------------------------------------------------------------------------
'''
REVISAO - Q 2

n1 = float(input("Digite uma nota:"))
n2 = float(input("Digite uma nota:"))
n3 = float(input("Digite uma nota:"))

media = (n1 + n2 + n3) / 3

if media < 4:
    print(f"Reprovado com média {media:.2f}")
elif media < 7:
    print(f"Recuperação com média {media:.2f}")
else:
    print(f"Aprovado com média {media:.2f}")
'''
#--------------------------------------------------------------------------------------------------
'''
REVISAO - Q 3

n = int(input("Digite um número: "))

lista = [] 

for i in range(1, n + 1):
     dobro = i * 2
     lista.append(dobro)

print(f"O dobro dos números de 1 a {n} é: {lista}")
'''
#--------------------------------------------------------------------------------------------------
'''
REVISAO - Q 4


print("\n === Menu de opções === \n")

while True:
    print("1. Converta de Celsius para Fahrenheit")
    print("2. Converta de Fahrenheit para Celsius")
    print("3. Sair")

    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == "1":
        c = float(input("\nDigite a temperatura em Celsius: "))
        f = (c * 9/5) + 32
        print(f"\n A temperatura em Fahrenheit é: {f:.2f}°F\n")

    elif opcao == "2":
        f = float(input("\nDigite a temperatura em Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"\nA temperatura em Celsius é: {c:.2f}°C\n")

    elif opcao == "3":
        print("\nSaindo do programa...\n")
        break

    else:
        print("\nOpção inválida\n")
'''
#--------------------------------------------------------------------------------------------------
'''
REVISAO - Q 5


produtos = [
    {
        "nome": "Produto 1",
        "valor": 5.50
    },
    {
        "nome": "Produto 2",
        "valor": 10.00
    },
    {
        "nome": "Produto n",
        "valor": 7.25
    }
]

for produto in produtos:
    print(f"{produto['nome']} - {produto['valor']:.2f} R$")
'''
#--------------------------------------------------------------------------------------------------
'''
REVISAO - Q 6


contatos = [
    {
        "nome": "joao",
        "telefone": "8211111",
        "email": "joao@email.com"
    },
    {
        "nome": "maria",
        "telefone": "823333",
        "email": "maria@email.com"
    }
]

busca = input("Digite o nome do contato que deseja buscar: ").lower()

for contato in contatos:
    if contato["nome"] == busca:
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        break
else:
    print("Contato não encontrado")
'''
