from utils import *

def restricao_capacidade(model, j):
    return  sum(model.Y[i,j] for i in model.I) <= model.capacidades[j]


def restricao_demanda(model, i):
    return sum(model.Y[i,j] for j in model.J) == model.demanda[i]


def ativacao_deposito(model, i, j):
    M = max(capacidades.values())
    return model.Y[i,j] <= M * model.X[j]