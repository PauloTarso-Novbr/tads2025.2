import streamlit as st
from functions.ploty import plot_ts

st.title("historico de cotacoes")
st.write("Vislumbre o historico de cotacoes")

ticker = st.sidebar.text_input(
    'Escolha o ticker', value = 'AAPL'
)

fig = plot_ts(ticker)

st.plotly_chart(fig)