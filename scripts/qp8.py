from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
import numpy as np

# Dados da QP8
grupos = [
    {
        "nome": "Desempenho, escalabilidade e isolamento",
        "estudos": ["S04", "S07", "S10", "S12", "S14", "S15", "S16"],
        "cor": "#F58518",
    },
    {
        "nome": "Ampliação e generalização empírica das avaliações",
        "estudos": ["S02", "S04", "S10", "S12", "S13", "S15"],
        "cor": "#E45756",
    },
    {
        "nome": "Segurança, falhas e interações problemáticas",
        "estudos": ["S01", "S03", "S07", "S08", "S13", "S17"],
        "cor": "#B279A2",
    },
    {
        "nome": "Automação e integração ao ciclo de desenvolvimento",
        "estudos": ["S02", "S06", "S09", "S11", "S16", "S18"],
        "cor": "#72B7B2",
    },
    {
        "nome": "Ambientes realistas e reprodutíveis de teste",
        "estudos": ["S06", "S08", "S09", "S15"],
        "cor": "#54A24B",
    },
    {
        "nome": "Fuzzing e técnicas adaptativas/inteligentes",
        "estudos": ["S01", "S05"],
        "cor": "#4C78A8",
    },
]

total_estudos = 18
largura = 0.58
x = np.arange(len(grupos))

plt.figure(figsize=(10.5, 5.2))

for i, grupo in enumerate(grupos):
    estudos = grupo["estudos"]
    base = 0

    for estudo in estudos:
        plt.bar(
            x[i],
            1,
            largura,
            bottom=base,
            color=grupo["cor"],
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

rotulos_x = [fill(g["nome"], width=22) for g in grupos]

plt.xticks(x, rotulos_x, fontsize=9.5)
plt.ylabel("Quantidade de estudos")
plt.ylim(0, 8.5)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

saida = Path("./output/")
saida.mkdir(parents=True, exist_ok=True)
plt.savefig(saida / "fig-qp8-lacunas-tendencias.pdf", bbox_inches="tight")
plt.savefig(saida / "fig-qp8-lacunas-tendencias.png", dpi=300, bbox_inches="tight")

plt.show()
