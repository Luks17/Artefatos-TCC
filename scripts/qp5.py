from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
import numpy as np

# Dados da QP5
grupos = [
    {
        "nome": "Isolamento e interferência entre tenants",
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
            "S12",
            "S13",
            "S14",
            "S15",
            "S16",
        ],
        "cor": "#4C78A8",
    },
    {
        "nome": "Dinamismo, não-determinismo e reprodutibilidade do teste",
        "estudos": [
            "S02",
            "S03",
            "S04",
            "S05",
            "S06",
            "S07",
            "S08",
            "S09",
            "S12",
            "S13",
            "S14",
            "S15",
            "S17",
        ],
        "cor": "#F58518",
    },
    {
        "nome": "Variabilidade e explosão combinatória",
        "estudos": [
            "S02",
            "S03",
            "S06",
            "S08",
            "S11",
            "S13",
            "S14",
            "S16",
            "S17",
            "S18",
        ],
        "cor": "#54A24B",
    },
]

total_estudos = 18
largura = 0.58
x = np.arange(len(grupos))

fig, ax = plt.subplots(figsize=(9.8, 6.2))

for i, grupo in enumerate(grupos):
    estudos = grupo["estudos"]
    base = 0

    for estudo in estudos:
        ax.bar(
            x[i],
            1,
            largura,
            bottom=base,
            color=grupo["cor"],
            edgecolor="black",
            linewidth=0.8,
        )

        ax.text(
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

    ax.text(
        x[i],
        total + 0.25,
        rotulo,
        ha="center",
        va="bottom",
        fontsize=11.5,
    )

rotulos_x = [fill(grupo["nome"], width=28) for grupo in grupos]

ax.set_xticks(x)
ax.set_xticklabels(rotulos_x, fontsize=11)
ax.set_ylabel("Quantidade de estudos")
ax.set_ylim(0, 16.2)
ax.grid(axis="y", linestyle="--", alpha=0.4)

fig.tight_layout()

saida = Path("./output/")
saida.mkdir(parents=True, exist_ok=True)
fig.savefig(saida / "fig-qp5-desafios.png", dpi=300, bbox_inches="tight")
fig.savefig(saida / "fig-qp5-desafios.pdf", bbox_inches="tight")

plt.show()
