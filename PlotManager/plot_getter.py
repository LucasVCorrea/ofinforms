import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


def get_seaborn_barplot_resumee(data_to_plot, mes_seleccionado, output_path):
    plt.figure(figsize=(10, 6))
    data_to_plot["Cantidad"] = data_to_plot["Cantidad"].astype(float)
    data_to_plot["Categoria"] = data_to_plot["Categoria"].replace({"Presunciones Captadas": "Presunciones\nCaptadas",
                                                                   "Imágenes Aceptadas por Auditoría Interna": "Imágenes\nAceptadas por\nAuditoría Interna",
                                                                   "Imágenes Rechazadas por Auditoría Interna": "Imágenes\nRechazadas por\nAuditoría Interna",
                                                                   "Imágenes Rechazadas por El Municipio": "Imágenes\nRechazadas por\nEl Municipio",
                                                                   "Imágenes Validadas por El Municipio": "Imágenes\nValidadas por\nEl Municipio"})
    sns.barplot(
        data=data_to_plot,
        x="Categoria",
        y="Cantidad",
        color="LightCoral",
        edgecolor="black",
        linewidth=0.5,
    )
    for container in plt.gca().containers:
        plt.gca().bar_label(container, fontsize=9.5, color='black', label_type="edge")

    for text in plt.gca().texts:
        valor = float(text.get_text())
        if valor < 0:
            text.set_text('')
        else:
            text.set_text(f'{valor:.0f}')
    plt.title(
        f"Gráfico Representativo de las Etapas de Procesamiento de las\nPresunciones/Infracciones\nBerisso-{mes_seleccionado} 2025")
    sns.despine(top=True, right=True)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close()

    return output_path


def get_seaborn_barplot_acta_por_tipo(data_to_plot, mes_seleccionado, output_path):
    plt.figure(figsize=(10, 6))
    data_to_plot["value"] = data_to_plot["value"].astype(float)
    data_to_plot = data_to_plot.groupby("variable").agg({"value": ["sum"]}).reset_index()
    data_to_plot.columns = ["variable", "value"]

    data_to_plot["variable"] = data_to_plot["variable"].replace({
        "Cruzar con luz roja": "Cruzar con luz roja",
        "Giro indebido": "Giro indebido",
        "No detenerse en linea de frenado o sobre senda peatonal": "No detenerse en linea\nde frenado o sobre\nsenda peatonal",
        "Sin casco y/o chaleco reflectante (conductor o acompañanate)": "Sin casco y/o chaleco\nreflectante (conductor\no acompañante)"})

    sns.barplot(
        data=data_to_plot,
        x="variable",
        y="value",
        color="PaleTurquoise",
        edgecolor="black",
        linewidth=0.5,
    )
    for container in plt.gca().containers:
        plt.gca().bar_label(container, fontsize=9.5, color='black', label_type="edge")

    for text in plt.gca().texts:
        valor = float(text.get_text())
        if valor < 0:
            text.set_text('')
        else:
            text.set_text(f'{valor:.0f}')
    plt.title(
        f"Actividad de los juzgados mes de {mes_seleccionado} 2025")
    sns.despine(top=True, right=True)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close()

    return output_path


def get_seaborn_barplot_judge_activity(data_to_plot, mes_seleccionado, output_path):
    plt.figure(figsize=(10, 6))
    data_to_plot["Cantidad"] = data_to_plot["Cantidad"].astype(float)
    data_to_plot["Etapa"] = data_to_plot["Etapa"].replace({
        "Canceladas por fallo ( todas en 0)": "Canceladas por\nfallo\n(todas en 0)",
        "Reduccion por fallo": "Reduccion por\nfallo",
        "Amonestaciones ( solo gasto administrativo)": "Amonestaciones\n(solo gasto\nadministrativo)",
        "Pago total por fallo": "Pago total por\nfallo"})
    sns.barplot(
        data=data_to_plot,
        x="Etapa",
        y="Cantidad",
        hue="Juzgado",
        palette=["MediumPurple", "PaleGreen"],
        edgecolor="black",
        linewidth=0.5,
    )
    for container in plt.gca().containers:
        plt.gca().bar_label(container, fontsize=9.5, color='black', label_type="edge")

    for text in plt.gca().texts:
        valor = float(text.get_text())
        if valor < 0:
            text.set_text('')
        else:
            text.set_text(f'{valor:.0f}')
    plt.title(
        f"Actividad de los juzgados mes de {mes_seleccionado} 2025")
    sns.despine(top=True, right=True)

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close()

    return output_path



import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

def get_seaborn_piechart_payments(data_to_plot, mes_seleccionado, output_path):
    plt.figure(figsize=(8, 8))

    # Limpieza y conversión
    data_to_plot["value"] = (
        data_to_plot["value"]
        .str.replace("$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    labels = data_to_plot["variable"]
    values = data_to_plot["value"]

    # Colores pasteles
    colors = [
        "#AEC6CF",  # azul
        "#FFB7B2",  # rojo
        "#B5EAD7",  # verde
        "#C7CEEA",  # violeta
        "#FFF1C1",  # amarillo
        "#FFD6A5",  # naranja
    ]

    wedges, _ = plt.pie(
        values,
        startangle=90,
        counterclock=False,
        colors=colors[:len(values)],
        wedgeprops={"edgecolor": "white", "linewidth": 1}
    )

    total = values.sum()

    # Valores y porcentajes por fuera (sin nombre)
    for wedge, value in zip(wedges, values):
        angle = (wedge.theta2 + wedge.theta1) / 2
        x = np.cos(np.deg2rad(angle))
        y = np.sin(np.deg2rad(angle))

        ha = "left" if x > 0 else "right"

        plt.annotate(
            f"$ {value:,.0f}\n({value / total * 100:.1f}%)",
            xy=(x, y),
            xytext=(1.25 * x, 1.25 * y),
            ha=ha,
            va="center",
            fontsize=10,
            arrowprops=dict(
                arrowstyle="-",
                color="gray",
                linewidth=0.8
            )
        )

    # Leyenda (hue)
    plt.legend(
        wedges,
        labels,
        title="Medio de Pago",
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        frameon=False
    )

    plt.title(
        f"Desglose de Pagos - {mes_seleccionado} 2025",
        fontsize=12
    )

    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

    return output_path





def get_stages_barplot(data_to_plot, mes_seleccionado):
    fig = px.bar(data_to_plot, x="Categoria", y="Cantidad", text_auto=True, color_discrete_sequence=["LightCoral"])
    fig.update_traces(marker=dict(line=dict(color='gray', width=0.5)),
                      textfont=dict(color="black", size=12),
                      textposition='outside'
                      )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='black'),
        xaxis=dict(
            title=dict(font=dict(color='black')),
            tickfont=dict(color='black'),
            linecolor='black',
            gridcolor='rgba(0,0,0,0)',
        ),
        yaxis=dict(
            title=dict(font=dict(color='black')),
            tickfont=dict(color='black'),
            linecolor='black',
            gridcolor='rgba(0,0,0,0)',
        ),
        title={
            'text': f"Gráfico Representativo de las Etapas de Procesamiento de las Presunciones/ Infracciones Berisso- {mes_seleccionado} 2025",
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(color='black')
        },
        legend_title_font=dict(color='black'),
        height=500)

    return fig


def get_activity_by_judge(data_to_plot, mes_seleccionado):
    fig = px.bar(data_to_plot, x="Etapa", y="Cantidad", text_auto=True, color="Juzgado", barmode="group",
                 color_discrete_sequence=["MediumPurple", "PaleGreen"])
    fig.update_traces(
        textfont=dict(color="black", size=12),
        textposition='outside'
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='black'),
        xaxis=dict(
            title=dict(font=dict(color='black')),
            tickfont=dict(color='black'),
            linecolor='black',
            gridcolor='rgba(0,0,0,0)',
        ),
        yaxis=dict(
            title=dict(font=dict(color='black')),
            tickfont=dict(color='black'),
            linecolor='black',
            gridcolor='rgba(0,0,0,0)',
        ),
        title={
            'text': f"Actividad de los juzgados mes de {mes_seleccionado} 2025",
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(color='black')
        },
        legend_title_font=dict(color='black'),
        height=500)
    return fig


def get_actas_by_infraccion(data_to_plot, mes_seleccionado):
    data_to_plot["value"] = data_to_plot["value"].astype(float)
    data_to_plot = data_to_plot.groupby("variable").agg({"value": ["sum"]}).reset_index()
    data_to_plot.columns = ["variable", "value"]
    fig = px.bar(data_to_plot.loc[data_to_plot["value"] > 0], x="variable", y="value",
                 color_discrete_sequence=["PaleTurquoise"], text_auto=True)
    fig.update_traces(
        textfont=dict(color="black", size=12),
        textposition='outside'
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='black'),
        xaxis=dict(
            title=dict(font=dict(color='black')),
            tickfont=dict(color='black'),
            linecolor='black',
            gridcolor='rgba(0,0,0,0)',
        ),
        yaxis=dict(
            title=dict(font=dict(color='black')),
            tickfont=dict(color='black'),
            linecolor='black',
            gridcolor='rgba(0,0,0,0)',
        ),
        title={
            'text': f"Cantidad de Actas por Tipo de Infraccion<br>{mes_seleccionado} 2025",
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(color='black')
        },
        legend_title_font=dict(color='black'),
        height=500)
    return fig

def get_piechart_payments(data_to_plot,mes_seleccionado):
    data_to_plot["value"] = (
        data_to_plot["value"]
        .str.replace("$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    fig = px.pie(
        data_to_plot,
        names="variable",
        values="value",
        color="variable",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )


    fig.update_traces(
        texttemplate="%{label}<br>$%{value:,.0f}<br>(%{percent:.1%})",
        textposition="inside",
        textfont=dict(color="black", size=14),
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='black'),
        xaxis=dict(
            title=dict(font=dict(color='black')),
            tickfont=dict(color='black'),
            linecolor='black',
            gridcolor='rgba(0,0,0,0)',
        ),
        yaxis=dict(
            title=dict(font=dict(color='black')),
            tickfont=dict(color='black'),
            linecolor='black',
            gridcolor='rgba(0,0,0,0)',
        ),
        title={
            'text': f"Desglose de Pagos - {mes_seleccionado} 2025",
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(color='black')
        },
        legend_title_font=dict(color='black'),
        height=500)
    return fig
