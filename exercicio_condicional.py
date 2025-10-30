#1
num = int(input("Digite seu número"))
if num %2 == 0:
    print("Seu número é par")
else:
    print("Seu número é impar")

#2
num = float(input("Digite sua nota final"))
if num >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#3
valor = int(input("Qual o valor da sua compra?"))
desconto = valor - valor/10
if valor > 100:
    print("O valor final da sua compra é:", desconto)
else:
    print("O valor final da sua compra é:", valor)

 #4   
Celcius = int(input("Digite a temperatura em Celcius"))
Fahrenheit = (Celcius * 9/5) + 32
print("Sua temperatura em Fahrenheit é igual a:", Fahrenheit)

#5
num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))
if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os dois números são iguais")

#6
num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))
num3 = int(input("Digite o terceiro numero"))
if num1 > num2 and num1 > num3:
    print("O maior número é:", num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é:", num2)
elif num3 > num1 and num3 > num2:
    print("O maior número é:", num3)
else:
    print("Os números são iguais")

#7
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro")
else:
    print("Operação inválida!")

#9
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")

#10
idade = int(input("Digite sua idade:"))
if idade >= 18 and idade <= 65:
    print("Dentro da faixa permitida")
else:
    print("Fora da faixa permitida")

#11
usuario = input("Digite seu nome de usuário:")
senha = input("Digite sua senha:")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")

#12
idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Não vota")
elif (idade >= 18 and idade <= 70):  
    print("Voto obrigatório")
elif (idade == 16 or idade == 17 or idade > 70):
    print("Voto facultativo")

#13
numero = int(input("Digite um número de 10 a 50: "))
if numero >= 10 and numero <= 50:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")

#14
media = float(input("Digite sua média:"))
if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")