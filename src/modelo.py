import pyomo.environ as pyo
from utils import *
from restricoes import *
import pandas as pd
import numpy as np


model = pyo.ConcreteModel()
# Conjuntos 
model.J = pyo.Set(initialize=range(1, 6))  # Índices do vetor de decisão (armazéns)
model.I = pyo.Set(initialize=range(1, 6)) # Índices dos clientes (cidades)

# Parâmetros
model.custos_logisticos = pyo.Param(model.J, model.I,
                                    initialize=lambda m,i,j: custos_logisticos[j-1,i-1])
model.custos_construcao = pyo.Param(model.J, initialize=custos_construcao)
model.capacidades = pyo.Param(model.J, initialize=capacidades)
model.demanda = pyo.Param(model.I, initialize=demandas)

# Variáveis
# Ativa armazém na localidade j
model.X = pyo.Var(model.J, domain=pyo.Binary)
# Quantidade enviada de j para i
model.Y = pyo.Var(model.I, model.J, domain=pyo.NonNegativeReals)

# Função objetivo
custo_variavel = pyo.summation(model.custos_logisticos, model.Y)
custo_fixo = sum(model.custos_construcao[j]*model.X[j] for j in model.J)
model.obj = pyo.Objective(expr=custo_variavel + custo_fixo, sense=pyo.minimize)

# Restrições
model.restricao_demanda = pyo.Constraint(model.I, rule=restricao_demanda)
model.restricao_capacidade = pyo.Constraint(model.J, rule=restricao_capacidade)
model.ativacao_deposito = pyo.Constraint(model.I, model.J, rule=ativacao_deposito)
model.restricao_armazens = pyo.Constraint(expr=pyo.summation(model.X) == 3)

# Solver
solver = pyo.SolverFactory('glpk', validate=False,
                           executable=r'solver\glpsol.exe')

# Resultados
results = solver.solve(model, tee=True)

# Matriz Y[j,i]
Y_array = np.array([[model.Y[i,j].value for i in model.I] for j in model.J])
Y_df = pd.DataFrame(Y_array, index=local_armazens.values(),
                    columns=destinos.values())
print("\nY[i,j]:")
print(Y_df)

# Vetor X[j] e Series
X_array = np.array([model.X[j].value for j in model.J])
X_series = pd.Series(X_array, index=model.J)
print("\nX[j]:")
print(X_series)

# Verificar demanda de cada cidade
print('\n')
for i in model.I:
    total_recebido = sum(model.Y[i,j].value for j in model.J)
    print(f'Cidade {i}: total recebido = {total_recebido:.2f}, demanda = {model.demanda[i]}')

# Verificar capacidade de cada armazém
print('\n')
for j in model.J:
    total_enviado = sum(model.Y[i,j].value for i in model.I)
    print(f'Armazém {j}: total enviado = {total_enviado:.2f}, capacidade = {model.capacidades[j]}')

# Melhor solucão encontrada
print(f'\nMelhor solução: R$ {pyo.value(model.obj) / 1000} milhões')
