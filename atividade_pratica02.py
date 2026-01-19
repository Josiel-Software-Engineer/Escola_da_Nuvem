""" 1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros.
Use os seguintes dados:
* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos,
arredondando para duas casas decimais.
"""

real = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolar = real/taxa_dolar
euro = real/taxa_euro
print(f"O valor do Dolar é ${dolar:.2f}\n"
      f"O valor do Euro é €{euro:.2f}")

"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja.
Use as seguintes informações:
* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final,
exibindo todos os detalhes.
"""

produto = "Camiseta"
preco = 50
taxa_desconto = 0.20
desconto = preco * taxa_desconto
p_final = preco - desconto
print(f"Produto: {produto}\n"
      f"Preço: R${preco:.2f}\n"
      f"Desconto: {taxa_desconto * 100:.0f}%\n"
      f"Valor promocional: R${p_final:.2f}"
)

"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno.
Use as seguintes notas:
* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final,
arredondando para duas casas decimais.
"""

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print(f"A nota 1 foi {nota1:.2f}\n"
      f"A nota 2 foi {nota2:.2f}\n"
      f"A nota 3 foi {nota3:.2f}")
if media >= 7.0:
    print(f"O aluno teve uma média de {media:.2f}, está aprovado.")
elif media >= 6.0:
    print(f"O aluno teve uma média de {media:.2f}, está em recuperação.")
else:
    print(f"O aluno teve uma média de {media:.2f}, está reprovado.")

"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo.
Use os seguintes dados:
* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem,
incluindo o resultado final arredondado para duas casas decimais.
"""

distancia = 300
consumo = 25
media = distancia / consumo

print(f"Distância percorrida: {distancia} Km\n"
      f"Combustível gasto: {consumo} litros\n"
      f"Consumo médio de {media:.2f} Km/l."
)
