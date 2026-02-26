import pandas as pd

from Functions.functions import traducir_mes


def get_resumen_mensual_dataframe():
    df = pd.read_csv(
        "Files/Book 10(resumen_mensuales).csv",
        encoding="latin-1",
        sep=";",
    thousands=".",
    decimal=","
    )

    # Normalizar Mes
    df["Mes"] = df["Mes"].astype(str).str.capitalize().str.strip()

    # Convertir TODAS las columnas a string
    df = df.astype(str)

    return df


def get_info_camaras():
    df = pd.read_csv(
        "Files/Book 10(info_camaras).csv",
        encoding="latin-1",
        sep=";",
    thousands=".",
    decimal=","
    )

    # Normalizar columnas
    df.columns = df.columns.str.strip()

    # LIMPIEZA FUERTE de Tipo Infraccion
    df["Tipo Infraccion"] = (
        df["Tipo Infraccion"]
        .astype(str)
        .str.replace('"', '', regex=False)  # quitar comillas
        .str.replace("\r\n", "\n", regex=False)
        .str.replace("\r", "\n", regex=False)
        .str.replace("\n ", "\n", regex=False)  # saltos con espacios
        .str.strip()
    )
    df = df.astype(str)
    return df


def get_resumen_infracciones():
    df = pd.read_csv(
        "Files/Book 10(resumen_infracciones).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.astype(str)
    return df


def get_infracciones_por_camara():
    df = pd.read_csv(
        "Files/Book 10(infracciones_por_camara).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.astype(str)
    return df


def get_recaudacion_detallada():
    df = pd.read_csv(
        "Files/Book 10(recaudacion).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.astype(str)
    return df


def get_canales_de_pago():
    df = pd.read_csv(
        "Files/Book 10(canales_de_pago).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.astype(str)
    return df


def get_recaudacion():
    df = pd.read_csv(
        "Files/Book 10(recaudacion).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.astype(str)
    return df


def get_movimientos_juzgados():
    df = pd.read_csv(
        "Files/Book 10(movimientos_juzgados).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.astype(str)
    return df


def get_actas_juzgados_bajas():
    df = pd.read_csv(
        "Files/Book 10(actas_juzgados_bajas).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.astype(str)
    return df


def get_actas_juzgados_altas():
    df = pd.read_csv(
        "Files/Book 10(actas_juzgados_altas).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.rename(columns={"Cant. de actas": "Cantidad de actas"})
    df = df.astype(str)
    return df


def get_valores_infracciones():
    df = pd.read_csv(
        "Files/Book 10(valores_infracciones).csv",
        encoding="latin-1", sep=";",
    thousands=".",
    decimal=","
    )
    # df.columns = df.columns.str.capitalize().str.strip()
    df["Mes"] = df["Mes"].str.capitalize().str.strip()
    df = df.astype(str)
    return df


def get_lotes_en_mes(mes_seleccionado):
    df = pd.read_excel("Files/lotes_filtrados (7).xlsx")
    df["Mes"] = pd.to_datetime(df["Fecha Impresión"]).dt.month_name().map(traducir_mes)
    df["Año"] = pd.to_datetime(df["Fecha Impresión"]).dt.year
    df = df.rename(columns ={"ID":"Lote"})

    return df.loc[
        (df["Mes"] == mes_seleccionado) & (df["Año"] == 2025)]
