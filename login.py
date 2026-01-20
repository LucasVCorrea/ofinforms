import streamlit as st
import pandas as pd
from Functions.functions import generar_docx_informe
from DataManager.file_reader import get_resumen_mensual_dataframe, get_info_camaras, get_resumen_infracciones, \
    get_infracciones_por_camara, get_recaudacion_detallada, get_canales_de_pago, get_recaudacion, \
    get_movimientos_juzgados, get_actas_juzgados_bajas, get_valores_infracciones, get_actas_juzgados_altas, \
    get_lotes_en_mes
from Functions.functions import get_meses_ordenados
from PlotManager.plot_getter import get_stages_barplot, get_activity_by_judge

st.set_page_config(layout="wide")
cola, colb = st.columns(2)
mes_seleccionado = cola.selectbox("Seleccione una opción", options=get_meses_ordenados(), key="opcion_seleccionada")

resumen_infracciones = get_resumen_infracciones()
resumen_general = get_resumen_mensual_dataframe()
infracciones_por_camara = get_infracciones_por_camara()
recaudacion_detallada = get_recaudacion_detallada()
canales_de_pago = get_canales_de_pago()
recaudacion = get_recaudacion()
movimientos_juzgados = get_movimientos_juzgados()
actas_juzgados_bajas = get_actas_juzgados_bajas()
actas_juzgados_altas = get_actas_juzgados_altas()
valores_infracciones = get_valores_infracciones()
info_camaras = get_info_camaras()

resumen_infracciones_selected = (resumen_infracciones.loc[resumen_infracciones["Mes"] == mes_seleccionado])
resumen_general_selected = (resumen_general.loc[resumen_general["Mes"] == mes_seleccionado])
infracciones_por_camara_selected = (infracciones_por_camara.loc[infracciones_por_camara["Mes"] == mes_seleccionado])
recaudacion_detallada_selected = (recaudacion_detallada.loc[recaudacion_detallada["Mes"] == mes_seleccionado])
canales_de_pago_selected = (canales_de_pago.loc[canales_de_pago["Mes"] == mes_seleccionado])
recaudacion_selected = (recaudacion.loc[recaudacion["Mes"] == mes_seleccionado])
movimientos_juzgados_selected = (movimientos_juzgados.loc[movimientos_juzgados["Mes"] == mes_seleccionado])
actas_juzgados_bajas_selected = (actas_juzgados_bajas.loc[actas_juzgados_bajas["Mes"] == mes_seleccionado])
actas_juzgados_altas_selected = (actas_juzgados_altas.loc[actas_juzgados_altas["Mes"] == mes_seleccionado])

valores_infracciones_selected = (valores_infracciones.loc[valores_infracciones["Mes"] == mes_seleccionado])
camaras_del_mes = infracciones_por_camara.loc[infracciones_por_camara["Mes"] == mes_seleccionado][
    "Ubicación física"].unique()
info_camaras_selected = (info_camaras.loc[info_camaras["Ubicación"].isin(camaras_del_mes)])
st.markdown("##### 1. Detalle del Equipamiento Tecnológico Utilizado para el Servicio")

st.markdown(
    """
Se procede a especificar las características tecnológicas de los equipos empleados, 
incluyendo el número de serie, la descripción de la cámara, la marca y el modelo 
correspondiente.
También se proporciona información detallada sobre el uso del equipamiento, 
ubicación, fechas de inicio, tipo de montaje, cantidad de equipos por punto de ubicación y 
el juzgado responsable. En cuanto al uso del equipamiento, se detallará su propósito 
específico para su correcta operación. La ubicación del equipamiento se especificará 
claramente, indicando su posición física exacta. Se proporcionarán mapas o diagramas 
detallados para facilitar su localización. Las fechas de inicio de la actividad se registrarán 
meticulosamente, junto con cualquier información relevante. El tipo de montaje necesario 
para el equipamiento se describirá en función de las especificaciones técnicas de las cámaras.
"""
)

with st.container():
    st.markdown("###### 1.1 Descripción del equipo")
    col_left, col_center, col_right = st.columns([1, 3, 1])
    with col_center:
        st.dataframe(
            info_camaras_selected[
                ["Número de serie", "Marca", "Modelo"]
            ].reset_index(drop=True), hide_index=True
        )

with st.container():
    st.markdown("###### 1.2 Estado y características de los equipos")

    col_left, col_center, col_right = st.columns([1, 3, 1])
    with col_center:
        tabla_estado = info_camaras_selected[
            [
                "Ubicación",
                "Tipo de montaje",
                "Inicio de actividad",
                "Número de cámaras",
                "Tipo Infraccion",
            ]
        ].astype(str).reset_index(drop=True)

        st.dataframe(tabla_estado, hide_index=True)
st.markdown(
    f"##### II. Clasificación de las infracciones de Tránsito / Cuadro Tarifario {mes_seleccionado} 2025.")
st.markdown(
    "El informe que se presenta a continuación tiene como objetivo exponer una tabla que detalla la clasificación de las infracciones de tránsito y su correspondiente cuadro tarifario. Esta información proporciona detalles precisos sobre, el valor de la multa en unidades fijasy su equivalente en pesos.")
col_left, col_center, col_right = st.columns([1, 3, 1])
with col_center:
    st.dataframe(
        valores_infracciones_selected.drop(columns=["Año", "Mes"]).reset_index(drop=True), hide_index=True
    )
st.markdown(
    f"##### III. Procesamiento de infracciones")
st.markdown(
    "El equipo técnico de la Universidad Nacional de La Matanza ha desplegado un conjunto integral de procedimientos de adquisición de imágenes, diseñados para optimizar el funcionamiento del sistema de registro de infracciones de tránsito.Estos procedimientos abarcan una variedad de tecnologías, cámaras de diferente tipo de infracción instaladas en semáforos.En paralelo, se ha establecido un sólido sistema de registro de infracciones de tránsito que se integra perfectamente con los diversos mecanismos de adquisición de imágenes. Este sistema se caracteriza por su precisión y confiabilidad en la recopilación de datos, lo que permite una gestión eficiente de las infracciones viales.Para garantizar la integridad y precisión de este proceso, se ha implementado un proceso de auditoría que abarca todas las etapas del sistema. Esta auditoría comprende la verificación meticulosa de la calibración y funcionamiento de los dispositivos de captura de imágenes, así como una revisión detallada de los datos recopilados. Además, se lleva a cabo una validación rigurosa de la información registrada, junto con la detección y corrección de posibles discrepancias o irregularidades.Gracias a este enfoque integral de fiscalización, se han alcanzado resultados notables en términos de mejora continua y eficacia operativa. La combinación de diversos procedimientos de adquisición de imágenes, un sistema de registro de infracciones de tránsito bien estructurado y un proceso detallado de auditoría ha sido fundamental para lograr resultados destacados en la gestión del tráfico y la seguridad vial en los municipios y sus alrededores.")
st.markdown("###### III.I Descripción de las etapas del procesamiento de lo producido.")
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    resumen_general_selected.columns = ["Año", "Mes", "Presunciones Captadas",
                                        "Imágenes Aceptadas por Auditoría Interna",
                                        "Imágenes Rechazadas por Auditoría Interna",
                                        "Imágenes Rechazadas por El Municipio", "Imágenes Validadas por El Municipio",
                                        "Actas Fehacientes", "Valor UF"]
    st.dataframe(
        resumen_general_selected.drop(columns=["Año", "Mes", "Actas Fehacientes", "Valor UF"]).reset_index(drop=True),
        hide_index=True)
    data_to_plot = resumen_general_selected.drop(columns=["Año", "Mes", "Actas Fehacientes", "Valor UF"]).T
    data_to_plot = data_to_plot.reset_index()
    data_to_plot.columns = ["Categoria", "Cantidad"]
    st.plotly_chart(get_stages_barplot(data_to_plot, mes_seleccionado), use_container_width=True)
st.markdown(f"##### V. Efectividad Recaudatoria {mes_seleccionado} 2025 Berisso.")
st.markdown(
    "En relación con la generación de ingresos, es importante destacar que los pagos realizados por la cancelación de las infracciones registradas por el sistema de captación de la Universidad Nacional de La Matanza están sujetos a una serie de procedimientos de control para garantizar su adecuada gestión, como así también la integración con los diferentes sistemas de gestión de infracciones Nacionales y Provinciales. Estos procedimientos se traducen en una recopilación detallada de los montos recaudados por el Municipio, los cuales se presentan a continuación en forma de cuadros y gráficos para una mejor comprensión y análisis.A continuación, se detallan los montos recaudados por el Municipio, según los diferentes procedimientos de control aplicados a los pagos efectuados por la cancelación de las infracciones registradas por el sistema de captación de la Universidad Nacional de La Matanza.Estos datos reflejan la eficacia de los procedimientos de control implementados en la gestión de los pagos por cancelación de infracciones, proporcionando una visión clara y precisa de los ingresos generados. La transparencia en la presentación de esta información es fundamental para una adecuada rendición de cuentas y una gestión financiera responsable por parte del Municipio y la Universidad Nacional de la Matanza")

st.markdown("###### V.I Descripción de la producción por punto de Infracción para las cámaras de tipo Semáforo.")
col_left, col_center, col_right = st.columns([1, 8, 1])
with col_center:
    st.dataframe(
        infracciones_por_camara_selected.drop(columns=["Año", "Mes", "Valor uf"]).reset_index(drop=True),
        hide_index=True
    )

st.markdown(f"###### VI Detalle de los medios de pagos utilizados por el municipio de Berisso- {mes_seleccionado} 2025")
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    st.dataframe(canales_de_pago_selected.drop(
        columns=["Año", "Mes", "Sugit s/ ga", "Desglose gastos administ bocas de recaudación",
                 "Desglose gastos administ sugit"]).reset_index(drop=True), hide_index=True)

st.markdown(f"##### VII. Detalles de actas del mes de - {mes_seleccionado} 2025")
st.markdown(f"###### VII.I Detalle de Actividad de los Juzgados Mes de {mes_seleccionado} 2025")
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    st.dataframe(movimientos_juzgados_selected.drop(columns=["Año", "Mes"]), hide_index=True)
    data_to_plot = pd.melt(movimientos_juzgados_selected.drop(columns=["Año", "Mes"]), id_vars="Juzgado",
                           var_name="Etapa", value_name="Cantidad")
    data_to_plot["Juzgado"] = "Juzgado " + data_to_plot["Juzgado"].astype(str)
    st.plotly_chart(get_activity_by_judge(data_to_plot, mes_seleccionado), use_container_width=True)

st.markdown("###### VII.II Detalle del SUGIT.")
st.dataframe(actas_juzgados_altas_selected[["Año", "Mes", "Cantidad de actas"]], hide_index=True)
st.markdown("###### VII. III Detalle del SUGIT bajas.")
st.dataframe(actas_juzgados_bajas_selected.drop(columns="Cantidad de actas"), hide_index=True)

st.markdown("##### VIII. Detalle de Notificaciones")
st.write(f"Las notificaciones de las actas realizadas en el mes de {mes_seleccionado}")
dataframe_lotes = get_lotes_en_mes(mes_seleccionado)
col_left, col_center, col_right = st.columns([1, 2, 1])

col_center.dataframe(dataframe_lotes[["Lote", "Fecha Impresión", "Fecha Vencimiento", "Cantidad de Actas"]],
                     hide_index=True)
col_center.markdown(
    f"VIII. I Notificaciones realizadas en el mes de {mes_seleccionado}: **{int(dataframe_lotes['Cantidad de Actas'].sum())}**")

if st.button("Generar Word del informe", icon=":material/text_snippet:"):
    ruta_docx = f"informe_{mes_seleccionado}.docx"

    generar_docx_informe(
        ruta_docx,
        mes_seleccionado,
        info_camaras_selected,
        valores_infracciones_selected,
        resumen_general_selected,
        infracciones_por_camara_selected,
        canales_de_pago_selected,
        movimientos_juzgados_selected,
        actas_juzgados_altas_selected,
        actas_juzgados_bajas_selected,
        dataframe_lotes,
    )

    with open(ruta_docx, "rb") as f:
        st.download_button(
            "⬇ Descargar Word",
            data=f,
            file_name=ruta_docx,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
