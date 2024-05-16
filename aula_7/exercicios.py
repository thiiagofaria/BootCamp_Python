### 1 - Calcular Média de Valores em uma Lista

# from typing import List

# def calcular_media(valores: List[float]) -> float:
#     return sum(valores) / len(valores)

# lista = [0,1,2,3,4,5,6,7,8,9]

# print(calcular_media(lista))

### 2 - Filtrar Dados Acima de um Limite

# from typing import List

# def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
#     resultado = []
#     for valor in valores:
#         if valor >= limite:
#             resultado.append(valor)
#     return resultado

# lista = [0,1,2,3,4,5,6,7,8,9]
# limite = 2

# print(filtrar_acima_de(lista, limite))

### 3 - Contar Valores Únicos em uma Lista

# from typing import List

# def contar_valores_unicos(lista: List[int]) -> int:
#     return len(set(lista))

# lista = [0,1,2,3,4,1,2,3,4,5,6,7,8,9,23]

# print(contar_valores_unicos(lista))

### 4 - Converter Celsius para Fahrenheit em uma Lista

# from typing import List

# def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
#     return [(9/5) * temp + 32 for temp in temperaturas_celsius]

# lista = [12,13,41]

# print(celsius_para_fahrenheit(lista))

### 5 - Calcular Desvio Padrão de uma Lista

# from typing import List

# lista = [12,22,43,12,44]

# def calcular_desvio_padrao(valores: list[float]) -> float:
#     media = sum(valores) / len(valores)
#     variancia = sum((x - media) ** 2 for x in valores) / len (valores)
#     return variancia ** 0.5

# print(calcular_desvio_padrao(lista))

### 6 - Encontrar Valores Ausentes em uma Sequência

# from typing import List

# def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
#     completo = set(range(min(sequencia), max(sequencia) + 1))
#     return list(completo - set(sequencia))

# lista = [22,32,45,100000]

# print(encontrar_valores_ausentes(lista))

