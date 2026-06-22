from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
import numpy as np

# Dados da QP7
categorias = [
    {
        "nome": "Experimento comparativo ou controlado",
        "estudos": [
            "S01",
            "S04",
            "S05",
            "S06",
            "S08",
            "S10",
            "S12",
            "S13",
            "S15",
            "S17",
            "S18",
        ],
        "cor": "#4C78A8",
    },
    {
        "nome": "Estudo de caso demonstrativo ou prova de conceito",
        "estudos": ["S07", "S09", "S14"],
        "cor": "#F58518",
    },
    {
        "nome": "Estudo de caso industrial",
        "estudos": ["S11", "S16"],
        "cor": "#54A24B",
    },
    {
        "nome": "Evidência exploratória para taxonomia",
        "estudos": ["S03"],
        "cor": "#B279A2",
    },
    {
        "nome": "Sem avaliação empírica / avaliação conceitual",
        "estudos": ["S02"],
        "cor": "#E45756",
    },
]

total_estudos = 18
largura = 0.58
x = np.arange(len(categorias))

plt.figure(figsize=(10.5, 5.2))

for i, categoria in enumerate(categorias):
    estudos = categoria["estudos"]
    base = 0

    for estudo in estudos:
        plt.bar(
            x[i],
            1,
            largura,
            bottom=base,
            color=categoria["cor"],
            edgecolor="black",
            linewidth=0.8,
        )

        plt.text(
            x[i],
            base + 0.5,
            estudo,
            ha="center",
            va="center",
            fontsize=10.5,
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
        fontsize=11.5,
    )

rotulos_x = [fill(c["nome"], width=24) for c in categorias]

plt.xticks(x, rotulos_x, fontsize=10.5)
plt.ylabel("Quantidade de estudos")
plt.ylim(0, 12.5)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

saida = Path("./output/")
saida.mkdir(parents=True, exist_ok=True)
plt.savefig(saida / "fig-qp7-avaliacao-propostas.pdf", bbox_inches="tight")
plt.savefig(saida / "fig-qp7-avaliacao-propostas.png", dpi=300, bbox_inches="tight")

plt.show()
