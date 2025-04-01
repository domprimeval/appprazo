# app.py
import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Calculadora de Prazos", layout="centered")
st.title("📅 Calculadora de Prazos Corridos com Ajuste para Dia Útil")

st.markdown("""
Esta ferramenta calcula o **vencimento de um prazo corrido**, iniciando **no dia seguinte ao ato** e 
**antecipando para o último dia útil anterior** caso o prazo final caia em um fim de semana.
""")

# Entrada de dados do usuário
data_ato = st.date_input("Selecione a data do ato:", format="DD/MM/YYYY")
dias_prazo = st.number_input("Informe o prazo (em dias corridos):", min_value=1, step=1)

# Função para cálculo do vencimento
def calcular_vencimento(data_ato: datetime, dias_prazo: int) -> datetime:
    data_inicio = data_ato + timedelta(days=1)
    data_final = data_inicio + timedelta(days=dias_prazo - 1)

    while data_final.weekday() in [5, 6]:  # sábado = 5, domingo = 6
        data_final -= timedelta(days=1)

    return data_final

# Ação ao clicar no botão
if st.button("Calcular Vencimento"):
    data_final = calcular_vencimento(data_ato, dias_prazo)
    st.success(f"📌 O vencimento ajustado é: **{data_final.strftime('%d/%m/%Y')}**")
