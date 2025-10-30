#1
frutas = ["maçã", "banana" , "laranja" , "uva"]
print(frutas)
#2
frutas[0]
frutas[3]
#3
frutas.insert(4, "manga")
print(frutas)
#4
frutas.remove("banana")
print(frutas)
#5
frutas[2] = "abacaxi"
print(frutas)
#6
numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)  
#7
soma = sum(numeros)
print(soma)
#8
maior = max(numeros)
menor = min(numeros)
print("Seu maior número é:", maior)
print("Seu menor número é:", menor)
#9
numeros.reverse()
print(numeros)
#10
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
print(cidades)
#11
cidades.sort()
print(cidades)
#12
cidades.insert(4, "Porto Alegre")
print(cidades)
#13
indice = cidades.index("Curitiba")
print(indice)
#14
cidades.remove("Rio de Janeiro")
print(cidades)
#15
lista_1 = [1,2,3]
lista_2 = [4,5,6]
print(lista_1, lista_2)
#16
lista_3 = lista_1 + lista_2
print(lista_3)
#17
print(lista_3)
#18
animais_domesticos = ["cachorro", "gato", "coelho"] 
animais_selvagens = ["leão", "tigre", "urso"]
print(animais_domesticos,animais_selvagens)
#19
animais = animais_selvagens + animais_domesticos
print(animais)
#20
print(animais)
#21
nomes = ["Ana", "Pedro", "Maria", "João"]
print(nomes)
#22
for nome in nomes:print(nome)
#23
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)
#24
numeros2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(numeros2)
for num in numeros2:
    if num %2 == 0:
        print(num)
#25
quadrados = [num ** 2 for num in numeros2]
print(quadrados)
#26
palavras = ["python", "java", "c", "javascript"]
for palavra in palavras:
    print(f"{palavra} tem {len(palavra)} letras")
#27
idades = [12, 18, 25, 40, 60]
for idade in idades:
    if idade >= 18:
        print(f"{idade} é Maior de idade")
    else:
        print(f"{idade} é Menor de idade")
#28
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
for nota in notas:
    if nota >= 7:
        print(f"{nota} Aprovado")
    else:
        print(f"{nota} Reprovado")
#29
palavras2 = ["arara", "banana", "radar", "python"]
for palavra2 in palavras2:
    if palavra2 == palavra2 [:: -1]:
        print(palavra2, "é um palíndromo")
    else:
        print(palavra2, "Não é um palíndromo")
#30
compras = ["arroz", "feijão", "batata", "carne"]
for compra in compras:
    print(f"Preciso comprar {compra}")
#31
numero = 1
while numero<= 10:
    print(numero)
    numero +=1
#32
num = int(input("Digite um número"))
while num != 0:
    print(num)
    num = int(input("Digite um número inteiro"))
print("Programa encerrado")
#33
num1 = 1
soma = 0
while num1 <=100:
    soma = soma + num1
    num1 = num1 + 1
print(f"A soma dos números de 1 a 100 é:",soma)
#34
senha = int(input("Adivinhe o número secreto"))
while senha != 7:
    print("Número incorreto, tente novamente")
    senha = int(input("Adivinhe o número secreto"))
print("Acertou!")
#35
numeral = 2
while numeral <= 20:
    print(numeral)
    numeral = numeral + 2