# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:00:34 2022

@author: jahop_fz60h0
"""

import json
import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    



lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_NEA1lt.json")
lottie_hello1 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jlmgqgx2.json")




st_lottie(lottie_hello, key = "hello")
st_lottie(lottie_hello1, key = "hello1")



st.title("De México para el mundo, listo el Aeropuerto Internacional Felipe Ángeles")


st.subheader("")


st.subheader("Las mejores frases")

st.subheader("")

st.subheader("Haiga sido como haiga sido.................. ya está en servicio el Aeropueto Internacional Felipe Ángeles")

st.subheader("")

st.subheader("Comes y te vas,.......... desde el Aeropuerto Felipe Ángeles")

st.subheader("")

st.subheader("Defenderé el Aeropuerto Internacional Felipe Ángeles, ...........como un perro")

st.subheader("")

st.subheader("No se hagan bolas,............. todos tomarán su vuelo desde el Aeropuerto Internacional Felipe Ángeles")

st.subheader("")

st.subheader("El que se mueve no sale en la foto,......... de la inauguración del Aeropuerto Felipe Ángeles")

st.subheader("")

st.subheader("Gracias mi rey,.................... por el Aeropuerto Internacional Felipe Ángeles")

st.subheader("")

st.subheader("NO TE CALIENTES GRANIZO,........ QUE YA ESTÁ FUNCIONANDO EL AEROPUERTO INTERNACIONAL FELIPE ÁNGELES")

st.subheader("")

st.subheader("Si te vas de viaje,..............zumbale por tu boleto al Aeropuerto Felipe Ángeles")

st.subheader("")

st.subheader("adiuuuuuuu, nos vemos en la próxima")

st.subheader("")
st.subheader("jahoperi chusconoticias")
st.subheader("")
st.subheader("21 de marzo del 2022")
st.subheader("")
st.subheader("jahoperi@gmail.com")

