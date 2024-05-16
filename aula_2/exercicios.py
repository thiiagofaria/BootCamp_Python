import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero_1 = int(input("escreva o número: "))
# numero_2 = int(input("escreva o número: "))
# soma = numero_1+numero_2
# print(f"A soma dos dois números é: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# CONSTANTE = 5
# numero = int(input("Digite um número: "))
# resto_da_divisão = numero % CONSTANTE
# print(f"{resto_da_divisão}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero_1 = int(input("escreva o número: "))
# numero_2 = int(input("escreva o número: "))
# resultado = numero_1*  numero_2
# print(f"O resultado é {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero_1 = int(input("escreva o número: "))
# numero_2 = int(input("escreva o número: "))
# resultado = numero_1// numero_2
# print(f"O resultado é {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero_1 = int(input("escreva o número: "))
# resultado = numero_1 ** 2
# print(f"O resultado é {resultado}")


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero_1 = float(input("escreva o número: "))
# numero_2 = float(input("escreva o número: "))
# resultado = numero_1+numero_2
# print(f"O resultado é {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero_1 = float(input("escreva o número: "))
# numero_2 = float(input("escreva o número: "))
# resultado = (numero_1+numero_2)/2
# print(f"O resultado é {resultado}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# numero_1 = float(input("escreva a base: "))
# numero_2 = float(input("escreva o expoente: "))
# resultado = numero_1 ** numero_2
# print(f"O resultado é {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# numero_1 = float(input("insira a temperatura em Celsius: "))
# temperatura_fahrenheit = (numero_1*9/5)+32
# print(f"A temperatura em fahrenheit é {temperatura_fahrenheit:.2f}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Digite o raio do circulo: "))
# área = math.pi * (raio ** 2)
# print(f"A área do circulo é {área:.2f}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# string = input("Escreva alguma coisa: ")
# string_tratada = string.upper()
# print(string_tratada)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# string = input("Escreva alguma coisa: ")
# string_tratada = string.lower()
# print(string_tratada)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# string = input("Escreva alguma coisa que tenha espaço em branco no início e no final: ")
# string_tratada = string.strip()
# print(string_tratada)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no formato de dd/mm/aaaa: ")
# data_tratada = data.split("/")
# print(f"O dia é {data_tratada[0]}, o mês é {data_tratada[1]} e o ano é {data_tratada[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# string_1 = input("Digite alguma coisa: ")
# string_2 = input("Digite alguma outra coisa: ")
# soma_strings = string_1 + " " + string_2
# print(soma_strings)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# expressao1 = input("Digite a primeira expressão booleana (True ou False): ").lower()
# expressao2 = input("Digite a segunda expressão booleana (True ou False): ").lower()
# resultado = expressao1 and expressao2
# print("O resultado da operação AND é:", resultado)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# expressao1 = input("Digite a primeira expressão booleana (True ou False): ").lower()
# expressao2 = input("Digite a segunda expressão booleana (True ou False): ").lower()
# resultado = expressao1 and expressao2
# print("O resultado da operação or é:", resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# expressao1 = input("Digite a primeira expressão booleana (True ou False): ").lower()
# resultado_not = not expressao1
# print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# expressao1 = input("Digite um número: ")
# expressao2 = input("Digite um número: ")
# resultado_igualdade = (expressao1 == expressao2)
# print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# expressao1 = input("Digite um número: ")
# expressao2 = input("Digite um número: ")
# resultado_igualdade = (expressao1 != expressao2)
# print("Resultado da igualdade:", resultado_igualdade)

# #### try-except e if

# 21: Conversor de Temperatura


# try :
#     temperatura_celsius = float(input("Digite a temperatura em graus celsius: "))
#     temperatura_fareheint = ((9/5 * temperatura_celsius) + 32)
#     print(f"A tempertura de {temperatura_celsius} celsius equivale a {temperatura_fareheint} fareheint.")
# except ValueError:
#     print("Entrada inválida")


# 22: Verificador de Palíndromo

# try:
#     palavra = input("Digite uma palavra: ")
#     if isinstance(palavra,str):
#         formatado = palavra.replace(" ","").lower()
#         if formatado == formatado[::-1]:
#             print("Essa palavra é um palíndromo")
#         else:
#             print("Não é um palídromo")
#     else:
#         print("Entrada inválida")
# except ValueError:
#     print("Entrada inválida")

# 23: Calculadora Simples

# try:
#     num_1 = float(input("Digite o número: "))
#     num_2 = float(input("Digite o número: "))
#     operador = input("Digite o operador que deseja realizar(+,-,/,*):")
#     if operador == '+':
#         print(num_1+num_2)
#     elif operador == '-':
#         print(num_1-num_2)
#     elif operador == "*":
#         print(num_1*num_2)
#     elif operador == "/" and num_2 != 0:
#         print(num_1/num_2)
#     else:
#         print("operador inválido ou divisor é 0")
# except ValueError:
#     print("Entrada inválida")

# 24: Classificador de Números

# try:
#     número = float(input("Digite qualquer número: "))
#     if número > 0:
#         if número % 2 == 0:
#             print("Número é positivo e par")
#         else:
#             print("Número é positivo e impar")
#     elif número < 0:
#         if número % 2 == 0:
#             print("Número é negativo e par")
#         else:
#             print("Número é negativo e impar")
#     else:
#         print("Número é 0")
# except ValueError:
#     print("Entrada inválida")

# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separada por virgula: ")
números_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in números_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")