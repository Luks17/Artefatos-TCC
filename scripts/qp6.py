from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
import numpy as np

# Dados da QP6
atributos = [
    {
        "nome": "Seleção e geração direcionada de testes",
        "estudos": ["S01", "S05", "S11", "S17", "S18"],
        "cor": "#F58518",
    },
    {
        "nome": "Avaliação estruturada de desempenho e escalabilidade",
        "estudos": ["S07", "S12", "S14", "S16"],
        "cor": "#E45756",
    },
    {
        "nome": "Isolamento, particionamento e gerenciamento de recursos",
        "estudos": ["S02", "S06", "S10"],
        "cor": "#72B7B2",
    },
    {
        "nome": "Medição empírica de efeitos em ambientes multi-tenant",
        "estudos": ["S04", "S15"],
        "cor": "#B279A2",
    },
    {
        "nome": "Critérios e cenários específicos de teste multi-tenant",
        "estudos": ["S03", "S09"],
        "cor": "#4C78A8",
    },
    {
        "nome": "Controle da execução e interação entre tenants",
        "estudos": ["S08", "S13"],
        "cor": "#54A24B",
    },
]

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
            color=atributo["cor"],
            edgecolor="black",
            linewidth=0.8,
        )

        plt.text(
            x[i],
            base + 0.5,
            estudo,
            ha="center",
            va="center",
            fontsize=8.5,
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
        fontsize=9.5,
    )

rotulos_x = [fill(a["nome"], width=22) for a in atributos]

plt.xticks(x, rotulos_x, fontsize=8.5)
plt.ylabel("Quantidade de estudos")
plt.ylim(0, 10.5)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

saida = Path("./output/")
saida.mkdir(parents=True, exist_ok=True)
plt.savefig(saida / "fig-qp6-solucoes.pdf", bbox_inches="tight")
plt.savefig(saida / "fig-qp6-solucoes.png", dpi=300, bbox_inches="tight")

plt.show()
