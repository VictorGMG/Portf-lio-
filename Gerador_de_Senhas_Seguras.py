import streamlit as st
import random
import string

st.title("Gerador De Senhas ")
slide_caracteres = st.slider("Selecione a Quantidade De Caracteres Que Deseja Para Sua Senha ", max_value = 32, min_value = 6, value = 12)

if st.button("Gerar Senha"):
    
    caracteres = string.ascii_letters + string.punctuation + string.digits
    senha = [random.choice(caracteres) for _ in range(slide_caracteres)]
    senha_final = "".join(senha)
    st.write(f"A Senha Gerada é {senha_final}")
    