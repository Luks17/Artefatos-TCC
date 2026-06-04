from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Dados da QP1
total_estudos = 18
largura = 0.58

niveis = [
    {
        "nome": "Teste de sistema",
        "estudos": [
            "S03",
            "S04",
            "S05",
            "S06",
            "S07",
            "S08",
            "S10",
            "S12",
            "S14",
            "S15",
            "S16",
        ],
        "cor": "#4C78A8",
    },
    {
        "nome": "Teste de integração",
        "estudos": ["S03", "S09", "S17", "S18"],
        "cor": "#F58518",
    },
    {
        "nome": "Teste de aceitação",
        "estudos": ["S03", "S13"],
        "cor": "#54A24B",
    },
    {
        "nome": "Teste de unidade",
        "estudos": ["S03"],
        "cor": "#B279A2",
    },
    {
        "nome": "Não especificado",
        "estudos": ["S01", "S02", "S11"],
        "cor": "#E45756",
    },
]

objetivos = [
    {
        "nome": "Teste não funcional",
        "estudos": [
            "S01",
            "S02",
            "S03",
            "S04",
            "S05",
            "S06",
            "S07",
            "S08",
            "S10",
            "S12",
            "S14",
            "S15",
            "S16",
        ],
        "cor": "#4C78A8",
    },
    {
        "nome": "Teste de configuração",
        "estudos": ["S02", "S07", "S09", "S12", "S15", "S16", "S17"],
        "cor": "#F58518",
    },
    {
        "nome": "Teste de segurança",
        "estudos": ["S01", "S03", "S05", "S08", "S09", "S13"],
        "cor": "#E45756",
    },
    {
        "nome": "Teste de priorização",
        "estudos": ["S02", "S06", "S11", "S16", "S17", "S18"],
        "cor": "#72B7B2",
    },
    {
        "nome": "Teste de regressão",
        "estudos": ["S02", "S03", "S16", "S18"],
        "cor": "#54A24B",
    },
    {
        "nome": "Teste de privacidade",
        "estudos": ["S03", "S08", "S09", "S13"],
        "cor": "#B279A2",
    },
    {
        "nome": "Teste de interface e de API",
        "estudos": ["S08", "S09", "S11"],
        "cor": "#FF9DA6",
    },
    {
        "nome": "Teste de conformidade",
        "estudos": ["S02", "S12"],
        "cor": "#9D755D",
    },
]

# No gráfico de técnicas, a cor representa a classificação complementar:
# caixa-preta, caixa-branca ou caixa-cinza.
cores_caixa = {
    "caixa-preta": "#333333",
    "caixa-branca": "#FF9DA6",
    "caixa-cinza": "#4C78A8",
}

tecnicas = [
    {
        "nome": "Técnicas baseadas em especificação",
        "estudos": [
            "S01",
            "S02",
            "S03",
            "S04",
            "S05",
            "S06",
            "S07",
            "S08",
            "S09",
            "S10",
            "S13",
            "S14",
            "S15",
            "S16",
            "S17",
            "S18",
        ],
        "tipo_caixa": "caixa-preta",
    },
    {
        "nome": "Técnicas baseadas em conhecimento derivado",
        "estudos": ["S02", "S05", "S07", "S12", "S14", "S16", "S17"],
        "tipo_caixa": "caixa-cinza",
    },
    {
        "nome": "Técnicas baseadas em estrutura",
        "estudos": ["S01", "S05", "S14", "S18"],
        "tipo_caixa": "caixa-branca",
    },
    {
        "nome": "Técnicas baseadas no uso",
        "estudos": ["S02", "S06", "S11", "S16"],
        "tipo_caixa": "caixa-preta",
    },
    {
        "nome": "Técnicas baseadas em falhas e mutação",
        "estudos": ["S08", "S17"],
        "tipo_caixa": "caixa-branca",
    },
]


def formatar_percentual(total):
    percentual = total / total_estudos * 100
    return f"{total} ({percentual:.1f}%)".replace(".", ",")


def cor_texto_para_fundo(cor):
    if cor == cores_caixa["caixa-preta"]:
        return "white"
    return "black"


def plotar_categorias(ax, categorias, titulo, largura_rotulo=24, usar_tipo_caixa=False):
    x = np.arange(len(categorias))

    for i, categoria in enumerate(categorias):
        estudos = categoria["estudos"]
        base = 0

        if usar_tipo_caixa:
            cor = cores_caixa[categoria["tipo_caixa"]]
            cor_texto = cor_texto_para_fundo(cor)
        else:
            cor = categoria["cor"]
            cor_texto = "black"

        for estudo in estudos:
            ax.bar(
                x[i],
                1,
                largura,
                bottom=base,
                color=cor,
                edgecolor="black",
                linewidth=0.8,
            )

            ax.text(
                x[i],
                base + 0.5,
                estudo,
                ha="center",
                va="center",
                fontsize=8.2,
                color=cor_texto,
            )

            base += 1

        rotulo = formatar_percentual(len(estudos))

        ax.text(
            x[i],
            len(estudos) + 0.25,
            rotulo,
            ha="center",
            va="bottom",
            fontsize=9.3,
        )

    rotulos_x = [fill(c["nome"], width=largura_rotulo) for c in categorias]

    ax.set_title(titulo, fontsize=12, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(rotulos_x, fontsize=8.4)
    ax.set_ylabel("Quantidade de estudos")
    ax.set_ylim(0, max(len(c["estudos"]) for c in categorias) + 1.7)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)


fig, axes = plt.subplots(3, 1, figsize=(15, 17.5))

plotar_categorias(
    axes[0],
    niveis,
    "Níveis de teste",
    largura_rotulo=22,
)

plotar_categorias(
    axes[1],
    objetivos,
    "Objetivos de teste",
    largura_rotulo=20,
)

plotar_categorias(
    axes[2],
    tecnicas,
    "Técnicas de teste",
    largura_rotulo=24,
    usar_tipo_caixa=True,
)

legenda_tecnicas = [
    Patch(
        facecolor=cores_caixa["caixa-preta"],
        edgecolor="black",
        label="caixa-preta",
    ),
    Patch(
        facecolor=cores_caixa["caixa-branca"],
        edgecolor="black",
        label="caixa-branca",
    ),
    Patch(
        facecolor=cores_caixa["caixa-cinza"],
        edgecolor="black",
        label="caixa-cinza",
    ),
]

axes[2].legend(
    handles=legenda_tecnicas,
    title="Classificação complementar",
    loc="upper right",
    frameon=True,
)

plt.tight_layout()

saida = Path("./output/")
saida.mkdir(parents=True, exist_ok=True)
plt.savefig(saida / "fig-qp1-niveis-objetivos-tecnicas.pdf", bbox_inches="tight")
plt.savefig(
    saida / "fig-qp1-niveis-objetivos-tecnicas.png", dpi=300, bbox_inches="tight"
)

plt.show()
