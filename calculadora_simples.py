#atividade 1
def calculadora():
    print('Selecione a operação:')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')

    operacao = input('Digite o número da operação (1-2-3-4): ')

    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if operacao == '1':
        print(f'A soma dos números é: {soma(n1, n2)}')
    elif operacao == '2':
        print(f'A subtração dos números é: {subtracao(n1, n2)}')
    elif operacao == '3':
        print(f'A multiplicação dos números é: {multiplicacao(n1, n2)}')
    elif operacao == '4':
        print(f'A divisão dos números é: {divisao(n1, n2)}')
    else:
        print('Operação inválida')

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return 'ERRO'

calculadora()

