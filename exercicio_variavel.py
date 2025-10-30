nome = "Pedro"
altura = 1.84
idade = 18
eh_estudante = True
type(idade)
type(nome)
type(altura)
type(eh_estudante)

idade = input("Digite sua idade:")
idade = int(idade)
print("Sua idade é:", idade)
print("SUa idade daqui 5 anos será:", idade + 5)

num1 = input("Digite o primeiro número")
num2 = input("Digite o segundo número")
num1 = int(num1)
num2 = int(num2)
soma = num1 + num2
soma = int(soma)
print("A soma dos números é:", soma)

num1 = input("Digite o primeiro número")
num2 = input("Digite o segundo número")
num3 = input("Digite o terceiro número")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
média = (num1 + num2 + num3)/3
print("A média dos números é:", média)

AP1 = input("Digite sua nota da AP1")
AP2 = input("Digite sua nota da AP2")
AC = input("Digite sua nota da AC")
AP1 = float(AP1)
AP2 = float(AP2)
AC = float(AC)
média = float(média)
média = (AP1 * 0.4 + AP2 * 0.4 + AC * 0.2)
print("Sua média final é:" , média)

nome = input("Digite seu nome completo")
nome.upper()
print("Seu nome em maiúsculo é:" , nome.upper())
primeiro_nome = nome.split()[0]
print("Seu primeiro nome é:" , primeiro_nome)
quantidade_letras = len(nome.replace(" ", ""))
print("Seu nome tem" , quantidade_letras , "letras")