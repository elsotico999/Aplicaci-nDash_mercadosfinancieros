import streamlit as st
import yfinance as yf

st.title("Gráfica con Streamlit para cotización en bolsa de varias empresas")
empresas = ("AMZN", "FB2A.BE", "PAH3.F", "RACE", "SPOT")

opcion = st.selectbox("Selecciona una de las siguientes empresas:", empresas)
st.write("Has elegido:", opcion)

años = st.slider("Número de años que quieres observar y analizar:", 1,5,1)
st.write("Has elegido:", años, "años")

año_final = 2015 + años
st.write("año final:", año_final)

data = yf.download(opcion, "2015-1-1", f"{año_final}-12-31")
st.write(data.head())

data = data[["Close"]]
st.write(data)

st.line_chart(data)

mensaje = st.selectbox("¿Tienes pensando invertir en la bolsa?",("Si","No"))
st.write("Tu respuesta ha sido:", mensaje)