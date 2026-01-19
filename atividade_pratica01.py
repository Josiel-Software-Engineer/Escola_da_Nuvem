""" 1- Programa de Saudação
  * Crie um programa que imprima a mensagem "Olá, mundo!" na tela.
"""
print("Olá, mundo!")

""" 2- Calculadora de Soma
  * Desenvolva um programa que soma dois números. Use as variáveis numero1 = 12 e
numero2 = 14. O programa deve calcular a soma e exibir o resultado.
"""

numero1 = 12
numero2 = 14
soma = numero1 + numero2
print("A soma de 12 + 14 é ", soma, ".")

""" 3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:
* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³.
"""

comprimento = 12 #int(input("Qual é o comprimento? "))
largura = 14 #int(input("Qual é a largura? "))
altura = 20 #int(input("Qual é a altura? "))
volume = comprimento * largura * altura

print("O volume da caixa d'água é de ", volume, "cm³." )

""" 4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra.
Use as seguintes informações:
* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações,
incluindo o resultado final.
"""

produto = "Cadeira Infantil"
preco = 12.40
quantidade = 3 

print(f"Produto: {produto}\n"
      f"Preço: R${preco}\n"
      f"Quantidade: {quantidade}\n"
      f"Valor total: R${preco * quantidade}"
)