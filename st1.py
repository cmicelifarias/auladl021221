import streamlit as st
import yfinance as yf

st.write("""
Brincando com a bolsa de valores

só para começar

""")

acao = "NFLX"
dado = yf.Ticker(acao)

acaodf = dado.history(period="1d", start="2011-11-30", end="2012-12-1")

st.write("""
Preco de fechamento
""")
st.line_chart(acaodf.Close)

st.write("""
Volume da acao
""")
st.line_chart(acaodf.Volume)