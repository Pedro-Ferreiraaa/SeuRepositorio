#1
aluno = {
    "nome": "peter",
    "idade": 18,
    "curso": "economia"
}
print(aluno)
#2
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto["marca"] = "Warrior"
produto["preco"] = 320.00
produto["estoque"] = 8
del produto["marca"]
print(produto)
#3
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
for alunos, nota in notas.items():
    print(alunos,nota)
soma = sum(notas.values())
quantidade = len(notas)
media = soma/quantidade
print("A media das notas é:", media)
#4
numeros = {
    "a": 10, "b": 20, "c": 30
}
soma = sum(numeros.values())
print("A soma dos números é", soma)
#5
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for frutas in lista:
    if frutas in frequencia:
        frequencia[frutas] = frequencia[frutas] + 1
    else:
        frequencia[frutas] = 1
print(frequencia)
#6
produtos = {
    "caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000
    }
for produto, preco in produtos.items():
    if preco >= 50:
        print(produto, "Custa mais de 50 reais")
#7      
tradutor = {"table": "mesa", "woman": "mulher", "kid": "crianca"}
palavra = input("digite uma palavra: ")

if palavra in tradutor:
    print("A tradução é", tradutor[palavra])
else:
    print("Essa palavra não está na lista.")
#8
    
    