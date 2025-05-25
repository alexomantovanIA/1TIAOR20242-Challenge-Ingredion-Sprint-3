import pandas as pd
import random

# Simulação de dados por talhão com base em 6 anos e 9 talhões (3x3 grade visual da imagem)
anos = [2018, 2019, 2020, 2021, 2022, 2023]
talhoes = [f"Talhao_{i}" for i in range(1, 10)]
simulated_rows = []

# Valores reais médios por ano (dados IBGE consolidados)
ndvi_ano = {
    2018: 0.694,
    2019: 0.652,
    2020: 0.628,
    2021: 0.586,
    2022: 0.554,
    2023: 0.677
}

prod_ano = {
    2018: 14700,
    2019: 12558,
    2020: 17850,
    2021: 12900,
    2022: 9396,
    2023: 12528
}

rend_ano = {
    2018: 2100,
    2019: 1560,
    2020: 2100,
    2021: 1500,
    2022: 1080,
    2023: 1440
}

# Gerar variações realistas por talhão
for ano in anos:
    for talhao in talhoes:
        ndvi = round(ndvi_ano[ano] + random.uniform(-0.015, 0.015), 3)
        prod_total = prod_ano[ano] / len(talhoes)
        prod = round(prod_total + random.uniform(-300, 300), 1)
        rendimento = round(rend_ano[ano] + random.uniform(-100, 100), 1)
        simulated_rows.append([talhao, ano, ndvi, prod, rendimento])

df_talhoes = pd.DataFrame(simulated_rows, columns=["Talhao", "Ano", "NDVI", "Produtividade_ton", "Rendimento_kg_ha"])

# Exportar CSV
df_talhoes.to_csv("datasets/dados_simulados_por_talhao.csv", index=False)
