"""Modelo MILP para localização de armazéns da CEARS."""

import numpy as np
import pandas as pd
import pyomo.environ as pyo

from restricoes import restricao_capacidade, restricao_demanda
from utils import (
    CAPACIDADES,
    CUSTOS_CONSTRUCAO,
    CUSTOS_LOGISTICOS,
    DEMANDAS,
    DESTINOS,
    LOCAL_ARMAZENS,
)

CAMINHO_SOLVER = r"solver\glpsol.exe"
QUANTIDADE_ARMAZENS = 3


def criar_modelo():
    """Cria o modelo de programação linear inteira mista da CEARS."""
    model = pyo.ConcreteModel()

    model.J = pyo.Set(initialize=LOCAL_ARMAZENS.keys())
    model.I = pyo.Set(initialize=DESTINOS.keys())

    model.custos_logisticos = pyo.Param(
        model.I,
        model.J,
        initialize=lambda _, destino, armazem: CUSTOS_LOGISTICOS[
            armazem - 1,
            destino - 1,
        ],
    )
    model.custos_construcao = pyo.Param(
        model.J,
        initialize=CUSTOS_CONSTRUCAO,
    )
    model.capacidades = pyo.Param(model.J, initialize=CAPACIDADES)
    model.demanda = pyo.Param(model.I, initialize=DEMANDAS)

    model.X = pyo.Var(model.J, domain=pyo.Binary)
    model.Y = pyo.Var(model.I, model.J, domain=pyo.NonNegativeReals)

    custo_variavel = sum(
        model.custos_logisticos[destino, armazem]
        * model.Y[destino, armazem]
        for destino in model.I
        for armazem in model.J
    )
    custo_fixo = sum(
        model.custos_construcao[armazem] * model.X[armazem]
        for armazem in model.J
    )
    model.obj = pyo.Objective(
        expr=custo_variavel + custo_fixo,
        sense=pyo.minimize,
    )

    model.restricao_demanda = pyo.Constraint(
        model.I,
        rule=restricao_demanda,
    )
    model.restricao_capacidade = pyo.Constraint(
        model.J,
        rule=restricao_capacidade,
    )
    model.restricao_armazens = pyo.Constraint(
        expr=(
            sum(model.X[armazem] for armazem in model.J)
            == QUANTIDADE_ARMAZENS
        ),
    )

    return model


def resolver_modelo(model):
    """Resolve o modelo com GLPK usando o executável local glpsol."""
    solver = pyo.SolverFactory(
        "glpk",
        validate=False,
        executable=CAMINHO_SOLVER,
    )
    return solver.solve(model, tee=True)


def imprimir_resultados(model):
    """Imprime a solução encontrada e verificações de demanda e capacidade."""
    y_array = np.array(
        [
            [model.Y[destino, armazem].value for destino in model.I]
            for armazem in model.J
        ]
    )
    y_df = pd.DataFrame(
        y_array,
        index=LOCAL_ARMAZENS.values(),
        columns=DESTINOS.values(),
    )

    print("\nY[i,j]:")
    print(y_df)

    x_array = np.array([model.X[armazem].value for armazem in model.J])
    x_series = pd.Series(x_array, index=LOCAL_ARMAZENS.values())

    print("\nX[j]:")
    print(x_series)

    print()
    for destino in model.I:
        total_recebido = sum(
            model.Y[destino, armazem].value for armazem in model.J
        )
        print(
            f"Cidade {destino}: total recebido = {total_recebido:.2f}, "
            f"demanda = {model.demanda[destino]}"
        )

    print()
    for armazem in model.J:
        total_enviado = sum(
            model.Y[destino, armazem].value for destino in model.I
        )
        print(
            f"Armazém {armazem}: total enviado = {total_enviado:.2f}, "
            f"capacidade = {model.capacidades[armazem]}"
        )

    print(f"\nMelhor solução: R$ {pyo.value(model.obj) / 1000:.2f} milhões")


def main():
    """Executa a criação, solução e impressão dos resultados do modelo."""
    model = criar_modelo()
    resolver_modelo(model)
    imprimir_resultados(model)


if __name__ == "__main__":
    main()
