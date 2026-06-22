from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
import numpy as np

# Dados da QP4
atributos = [
    {
        "nome": "Desempenho, escalabilidade e uso de recursos",
        "estudos": ["S02", "S04", "S06", "S07", "S10", "S12", "S14", "S15", "S16"],
    },
    {
        "nome": "Confiabilidade, robustez e disponibilidade",
        "estudos": ["S02", "S09", "S10", "S11", "S12", "S13", "S15", "S16", "S17"],
    },
    {
        "nome": "Corretude funcional e falhas dependentes de interação",
        "estudos": ["S03", "S08", "S09", "S11", "S13", "S17", "S18"],
    },
    {
        "nome": "Isolamento e integridade de dados",
        "estudos": ["S02", "S03", "S08", "S09", "S13"],
    },
    {
        "nome": "Segurança e vulnerabilidades",
        "estudos": ["S01", "S02", "S03", "S05"],
    },
    {
        "nome": "Configurabilidade e variabilidade",
        "estudos": ["S02", "S03", "S16", "S17"],
    },
]

# Cores fixas por atributo
cores = {
    "Desempenho, escalabilidade e uso de recursos": "#4C78A8",
    "Confiabilidade, robustez e disponibilidade": "#F58518",
    "Corretude funcional e falhas dependentes de interação": "#54A24B",
    "Isolamento e integridade de dados": "#B279A2",
    "Segurança e vulnerabilidades": "#E45756",
    "Configurabilidade e variabilidade": "#72B7B2",
}

total_estudos = 18
largura = 0.58
x = np.arange(len(atributos))

plt.figure(figsize=(10.5, 5.2))

for i, atributo in enumerate(atributos):
    nome = atributo["nome"]
    estudos = atributo["estudos"]
    base = 0

    for estudo in estudos:
        plt.bar(
            x[i],
            1,
            largura,
            bottom=base,
            color=cores[nome],
            edgecolor="black",
            linewidth=0.8,
        )

        plt.text(
            x[i],
            base + 0.5,
            estudo,
            ha="center",
            va="center",
            fontsize=9.5,
        )

        base += 1

    total = len(estudos)
    percentual = total / total_estudos * 100
    rotulo = f"{total} ({percentual:.1f}%)".replace(".", ",")

    plt.text(
        x[i],
        total + 0.25,
        rotulo,
        ha="center",
        va="bottom",
        fontsize=10.5,
    )

rotulos_x = [fill(a["nome"], width=22) for a in atributos]

plt.xticks(x, rotulos_x, fontsize=9.5)
plt.ylabel("Quantidade de estudos")
plt.ylim(0, 10.5)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

saida = Path("./output/")
saida.mkdir(parents=True, exist_ok=True)
plt.savefig(saida / "fig-qp4-atributos.pdf", bbox_inches="tight")
plt.savefig(saida / "fig-qp4-atributos.png", dpi=300, bbox_inches="tight")

plt.show()
