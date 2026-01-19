def calculadora():
    while True:
        print("\nOperações: +  -  *  /  | Digite 'sair' para encerrar.")
        operacao = input("Escolha a operação: ")
        if operacao == 'sair':
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                print("Resultado:", num1 + num2)
            elif operacao == '-':
                print("Resultado:", num1 - num2)
            elif operacao == '*':
                print("Resultado:", num1 * num2)
            elif operacao == '/':
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("Erro: Divisão por zero.")
            else:
                print("Operação inválida.")
        except ValueError:
            print("Entrada inválida. Digite números válidos.")


calculadora()


def calcular_media_turma():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota registrada.")


calcular_media_turma()


def senha_forte(senha):
    return len(senha) >= 8 and any(char.isdigit() for char in senha)


while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        break
    if senha_forte(senha):
        print("Senha forte!")
        break
    else:
        print(
            "Senha fraca. Deve ter pelo menos 8 caracteres e conter pelo menos um número.")
        
        
def analisar_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
                print(f"{numero} é par.")
            else:
                impares += 1
                print(f"{numero} é ímpar.")
        except ValueError:
            print("Digite um número válido.")

    print(f"\nTotal de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")


analisar_numeros()