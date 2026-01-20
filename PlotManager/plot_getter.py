import plotly.express as px

def get_stages_barplot(data_to_plot,mes_seleccionado):
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
    fig = px.bar(data_to_plot, x="Etapa", y="Cantidad", text_auto=True, color = "Juzgado",barmode="group",color_discrete_sequence=["MediumPurple","PaleGreen"])
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
            'text': f"Gráfico Representativo de las Etapas de Procesamiento de las Presunciones/ Infracciones Berisso- {mes_seleccionado} 2025",
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(color='black')
        },
        legend_title_font=dict(color='black'),
    height=500)
    return fig