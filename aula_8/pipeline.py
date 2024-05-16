from etl import calcular_kpi_de_vendas

caminho_pasta = "data"
formato_de_saida = ['csv', 'parquet']

calcular_kpi_de_vendas(caminho_pasta, formato_de_saida)
