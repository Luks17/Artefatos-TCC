from pathlib import Path
from textwrap import fill

import matplotlib.pyplot as plt
import numpy as np

# Categorias multirrótulo conforme a extração da QP2.
categorias = [
    {
        "nome": "Geração de entradas ou casos de teste",
        "estudos": ["S01", "S04", "S16"],
        "cor": "#4C78A8",
    },
    {
        "nome": "Automação e execução de testes",
        "estudos": ["S01", "S03", "S04", "S09", "S13", "S18"],
        "cor": "#72B7B2",
    },
    {
        "nome": "Geração de carga ou simulação de usuários",
        "estudos": ["S06", "S10", "S12", "S15", "S16"],
        "cor": "#F58518",
    },
    {
        "nome": "Provisionamento ou orquestração do ambiente",
        "estudos": ["S08", "S09", "S15"],
        "cor": "#54A24B",
    },
    {
        "nome": "Monitoramento, coleta de métricas e observabilidade",
        "estudos": ["S07", "S11", "S16"],
        "cor": "#B279A2",
    },
]

total_estudos = 18
largura = 0.58
x = np.arange(len(categorias))

plt.figure(figsize=(10.8, 5.4))

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

rotulos_x = [fill(c["nome"], width=24) for c in categorias]

plt.xticks(x, rotulos_x, fontsize=8.5)
plt.ylabel("Quantidade de estudos")
plt.ylim(0, 7.2)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()

saida = Path("./output/")
saida.mkdir(parents=True, exist_ok=True)
plt.savefig(saida / "fig-qp2-ferramentas.pdf", bbox_inches="tight")
plt.savefig(saida / "fig-qp2-ferramentas.png", dpi=300, bbox_inches="tight")

plt.show()
