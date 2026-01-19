# 1 - Classificador de Idade

"""
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança(0-12 anos),
*Adolescente(13-17 anos),
*Adulto(18-59 anos) ou
*Idoso(60 anos ou mais).
"""

def classificar_idade():
    print("Classificador de Idade\n")

    while True:
        entrada = input("Digite sua idade (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break

        try:
            idade = int(entrada)

            if idade < 0:
                print("Idade inválida. Digite um número positivo.\n")
            elif idade <= 12:
                print("Categoria: Criança 🧒\n")
            elif idade <= 17:
                print("Categoria: Adolescente 👦\n")
            elif idade <= 59:
                print("Categoria: Adulto 👨\n")
            else:
                print("Categoria: Idoso 👴\n")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.\n")


# Executar o programa
classificar_idade()


# 2 - Calculadora de IMC
"""
Desenvolva um programa que calcule o Índice de Massa Corporal(IMC) de uma pessoa.
O programa deve solicitar o peso(em kg) e a altura(em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

def calcular_imc():
    print("Calculadora de IMC (Índice de Massa Corporal)\n")

    while True:
        try:
            peso = float(input("Digite seu peso em kg (ex: 70.5): "))
            altura = float(input("Digite sua altura em metros (ex: 1.75): "))

            if peso <= 0 or altura <= 0:
                print("Erro: Peso e altura devem ser maiores que zero.\n")
                continue

            imc = peso / (altura ** 2)

            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 25:
                classificacao = "Peso normal"
            elif imc < 30:
                classificacao = "Sobrepeso"
            else:
                classificacao = "Obeso"

            print(f"\nSeu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}\n")
            break

        except ValueError:
            print("Erro: Entrada inválida. Digite valores numéricos válidos.\n")


# # Executar o programa
calcular_imc()


# 3 - Conversor de Temperatura
"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32


def celsius_para_kelvin(c):
    return c + 273.15


def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9


def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15


def kelvin_para_celsius(k):
    return k - 273.15


def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def conversor_temperatura():
    print("Conversor de Temperatura")
    print("Unidades disponíveis: Celsius (C), Fahrenheit (F), Kelvin (K)\n")

    while True:
        try:
            valor = float(input("Digite a temperatura: "))
            origem = input(
                "Digite a unidade de origem (C/F/K): ").strip().upper()
            destino = input(
                "Digite a unidade de destino (C/F/K): ").strip().upper()

            if origem == destino:
                print(
                    f"A temperatura permanece a mesma: {valor:.2f}°{destino}\n")
                continue

            if origem == 'C':
                if destino == 'F':
                    convertido = celsius_para_fahrenheit(valor)
                elif destino == 'K':
                    convertido = celsius_para_kelvin(valor)
                else:
                    raise ValueError("Unidade de destino inválida.")
            elif origem == 'F':
                if destino == 'C':
                    convertido = fahrenheit_para_celsius(valor)
                elif destino == 'K':
                    convertido = fahrenheit_para_kelvin(valor)
                else:
                    raise ValueError("Unidade de destino inválida.")
            elif origem == 'K':
                if destino == 'C':
                    convertido = kelvin_para_celsius(valor)
                elif destino == 'F':
                    convertido = kelvin_para_fahrenheit(valor)
                else:
                    raise ValueError("Unidade de destino inválida.")
            else:
                raise ValueError("Unidade de origem inválida.")

            print(f"Temperatura convertida: {convertido:.2f}°{destino}\n")
            break

        except ValueError as e:
            print(f"Erro: {e}\nDigite novamente.\n")


# # Executar o programa
conversor_temperatura()


# 4 - Verificador de Ano Bissexto
"""
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários(divisíveis por 100) que não são divisíveis por 400.
"""

def verificar_ano_bissexto():
    print("Verificador de Ano Bissexto\n")

    while True:
        entrada = input("Digite um ano (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break

        try:
            ano = int(entrada)
            if ano < 0:
                print("Ano inválido. Digite um ano positivo.\n")
                continue

            # Verificação do ano bissexto
            if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
                print(f"O ano {ano} É bissexto.\n")
            else:
                print(f"O ano {ano} NÃO é bissexto.\n")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o ano.\n")


# # Executar o programa
verificar_ano_bissexto()