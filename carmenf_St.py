"""
Actividad relacionada con la Lección 13:
Creacion de una aplicacion para Visualizar  Datos de Impacto Social
en la formacion de Chicas en STEAM
"""

# _________________________Dependencias________________________
import pandas as pd
import streamlit as st
import os
import numpy as np
from PIL import Image
from datetime import datetime
import pytz
import pydeck as pdk

# Configuracion de los settings
st.set_page_config(layout="wide",
                   page_title=" Medicion de Impacto en Formacion STEAM",
                   page_icon=":taxi:")

# Definicion ruta de los archivos de acuerdo a la seleccion

MEDIA_ROOT = os.path.expanduser("~/Desktop/Actividad13/edades.csv")
MEDIA_ROOT1 = os.path.expanduser("~/Desktop/Actividad13/educacion.csv")
MEDIA_ROOT2 = os.path.expanduser("~/Desktop/Actividad13/indicadors.csv")
MEDIA_ROOT3 = os.path.expanduser("~/Desktop/Actividad13/mapa.csv")

# Titulo, Imagen y Fecha
st.write(datetime(2022, 5, 31, 10, 30, tzinfo=pytz.timezone("EST")))
img = Image.open("bitaminadas.png")
st.image(img, width=600)
st.title(" Medicion de Impacto de la formacion de Chicas en Steam")
st.write("***BITAMINADAS***")

#  Selector para el tipo de indicador
indicador = ("Edad", "Educacion", "STEAM")
opcion = st.selectbox("Seleccione el tipo de Indicador", indicador)


# Dependiendo de ;la seleccion se plotea  el dataset

if opcion == "Edad":
    st.write(" Variable Descriptiva : Edad")
    df = pd.read_csv(MEDIA_ROOT)
    st.bar_chart(df)
elif opcion == "Educacion":
    st.write(" Variable Descriptiva : Educacion")
    df = pd.read_csv(MEDIA_ROOT1)
    st.bar_chart(df)
else:
    st.write(" Variable Descriptivo : STEAM")
    df = pd.read_csv(MEDIA_ROOT2)
    st.line_chart(df)
st.write(df)
data = pd.read_csv(MEDIA_ROOT3)

st.map(data, zoom=None, use_container_width=True)

st.metric(label="Total chicas formadas 2018", value=60, delta=-0.5,
                delta_color="inverse")

st.metric(label="Total chicas formadas 2019", value=85, delta=0.5,
                delta_color="off")
