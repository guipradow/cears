import numpy as np

# Localidade dos armazéns
local_armazens = {
    1:'Alegrete',
    2:'Caçapava do Sul',
    3:'Tupanciretá',
    4:'Vacaria',
    5:'Santa Rosa'
}

# Destinos
destinos = {
    1:'Uruguaiana',
    2:'Pelotas',
    3:'Caxias do Sul',
    4:'Passo Fundo',
    5:'Porto Alegre'
}

# Custos Logísticos entre origem i e destino j (custo variável)
custos_logisticos = np.array([
    [2.1, 6.3, 7.8, 6.3, 7.5],
    [5.7, 2.7, 4.5, 4.5, 3.78],
    [5.4, 5.58, 4.38, 2.88, 4.80],
    [10.20, 6.54, 1.14, 2.4, 3.],
    [5.58, 7.86, 6., 3.48, 6.84]
])

# Custos de construção dos depósitos (custo fixo)
custos_construcao = {1:7000, 2:5000, 3:9000, 4:6000, 5:4000}
# Capacidade potencial dos depósitos
capacidades = {1:600, 2:750, 3:350, 4:450, 5:400}
# Demandas por destino
demandas = {1:150, 2:450, 3:300, 4:250, 5:500}