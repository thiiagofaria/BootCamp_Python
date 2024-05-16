# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# numeros = list(range(1, 11))
# print(numeros)
# for numero in numeros:
#     print(numero ** 2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# linguagens = ["Python", "Java", "C++", "JavaScript"]
# print(linguagens)

# linguagens.remove("C++")
# print(linguagens)

# linguagens.append("Ruby")
# print(linguagens)

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# livro = {
#     'titulo' : 'Teste',
#     'autor' : 'thiago faria',
#     'ano publicação' : '1997'
# }
# print(livro)

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# dicionário = {}
# for i in "engenharia de dados":
#     dicionário[i] = dicionário.get(i,0) + 1

# print(dicionário)

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# lista  = ["maçã", "banana", "cereja"]
# dicionário = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# #preço_tt_lista = sum(dicionário[item] for item in lista)

# #print(f"preço final é {preço_tt_lista:.2f}")