from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Dados da QP3
grupos = [
    {
        "segmentos": [
            ("Concreto público", ["S07", "S08", "S15"]),
            ("Contreto não-público", ["S01", "S06", "S16", "S18"]),
        ],
    },
    {
        "segmentos": [
            (
                "Conceitual/metodológico",
                ["S02", "S03", "S05", "S09", "S10", "S11", "S12", "S14", "S17"],
            ),
        ],
    },
    {
        "segmentos": [
            ("Sem artefato principal", ["S04", "S13"]),
        ],
    },
]

# Cores fixas por tipo de segmento
cores = {
    "Concreto público": "#4C78A8",
    "Contreto não-público": "#A0CBE8",
    "Conceitual/metodológico": "#F58518",
    "Sem artefato principal": "#B0B0B0",
}

total_estudos = 18
largura = 0.55
x = np.arange(len(grupos))

plt.figure(figsize=(7, 4.6))

labels_usados = set()

for i, grupo in enumerate(grupos):
    base = 0

    for nome_segmento, estudos in grupo["segmentos"]:
        label = nome_segmento if nome_segmento not in labels_usados else None
        labels_usados.add(nome_segmento)

        for estudo in estudos:
            plt.bar(
                x[i],
                1,
                largura,
                bottom=base,
                label=label,
                color=cores[nome_segmento],
                edgecolor="black",
            )

            plt.text(x[i], base + 0.5, estudo, ha="center", va="center", fontsize=9)

            base += 1
            label = None

    total = base
    percentual = total / total_estudos * 100
    rotulo = f"{total} ({percentual:.1f}%)".replace(".", ",")

    plt.text(x[i], total + 0.25, rotulo, ha="center", va="bottom", fontsize=10)

plt.xticks([0, 1, 2], ["Artefato concreto", "Conceitual/metodológico", "Sem artefato"])
plt.ylabel("Quantidade de estudos")
plt.ylim(0, 10.5)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2, frameon=False)

plt.tight_layout()

saida = Path("./output/")
saida.mkdir(parents=True, exist_ok=True)
plt.savefig(saida / "fig-qp3-materialidade.pdf", bbox_inches="tight")
plt.savefig(saida / "fig-qp3-materialidade.png", dpi=300, bbox_inches="tight")

plt.show()
