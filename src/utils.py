"""Dados de entrada para o problema de localização de armazéns da CEARS."""

import numpy as np


LOCAL_ARMAZENS = {
    1: "Alegrete",
    2: "Caçapava do Sul",
    3: "Tupanciretã",
    4: "Vacaria",
    5: "Santa Rosa",
}

DESTINOS = {
    1: "Uruguaiana",
    2: "Pelotas",
    3: "Caxias do Sul",
    4: "Passo Fundo",
    5: "Porto Alegre",
}

# Linhas: armazéns candidatos; colunas: cidades de destino.
CUSTOS_LOGISTICOS = np.array(
    [
        [2.10, 6.30, 7.80, 6.30, 7.50],
        [5.70, 2.70, 4.50, 4.50, 3.78],
        [5.40, 5.58, 4.38, 2.88, 4.80],
        [10.20, 6.54, 1.14, 2.40, 3.00],
        [5.58, 7.86, 6.00, 3.48, 6.84],
    ]
)

# Custos fixos de construção dos armazéns, em milhares de reais.
CUSTOS_CONSTRUCAO = {
    1: 7000,
    2: 5000,
    3: 9000,
    4: 6000,
    5: 4000,
}

# Capacidade potencial dos armazéns, em milhares de toneladas.
CAPACIDADES = {
    1: 600,
    2: 750,
    3: 350,
    4: 450,
    5: 400,
}

# Demandas anuais por destino, em milhares de toneladas.
DEMANDAS = {
    1: 150,
    2: 450,
    3: 300,
    4: 250,
    5: 500,
}
