import operator
# Calculadora Básica Python

global a, b;

# 1 = soma
# 2 = subtração
# 3 = multiplicação
# 4 = divisão
# 5 = loop

operacao = 5;
reset = 2;
while operacao == 5:
    print("\nBoas vindas à Calculadora Python 1.0!\nProjeto criado por Jânio Areias\n");
    operacao = 7;
    operacao = int(input("Primeiramente, insira qual operação você deseja calcular:\n\n1 para SOMA\n2 para SUBTRAÇÃO\n3 para MULTIPLICAÇÃO\n4 para DIVISÃO\n\nMinha escolha é "));



def operadores():
    print("_________________");
    a = int(input("\nInsira o primeiro número a ser calculado: "));
    b = int(input("\nInsira o segundo número a ser calculado: "));
    print("_________________");
    return a, b;

a, b = operadores();

if operacao == 1:
    print(f"\n\n>>> O resultado de {a} + {b} é", operator.add(a,b));
elif operacao == 2:
    print(f"\n\n>>> O resultado de {a} - {b} é", operator.sub(a,b));
elif operacao == 3:
    print(f"\n\n>>> O resultado de {a} * {b} é", operator.mul(a,b));
elif operacao == 4:
    print(f"\n\n>>> O resultado de {a} / {b} é", operator.truediv(a,b));