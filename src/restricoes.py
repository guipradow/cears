"""Regras de restrição do modelo de localização de armazéns."""


def restricao_capacidade(model, armazem):
    """Limita o volume enviado à capacidade do armazém aberto."""
    return (
        sum(model.Y[destino, armazem] for destino in model.I)
        <= model.capacidades[armazem] * model.X[armazem]
    )


def restricao_demanda(model, destino):
    """Garante que a demanda de cada destino seja atendida integralmente."""
    return (
        sum(model.Y[destino, armazem] for armazem in model.J)
        == model.demanda[destino]
    )
