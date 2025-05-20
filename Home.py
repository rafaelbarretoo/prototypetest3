import streamlit as st
from PIL import Image

st.set_page_config(page_title="🏠 Home", page_icon="🏠")

image = Image.open('LogoCIP.png')
st.image(image, caption='')
#st.title("Central de Inovações e Projetos")
st.markdown("<h2 style='text-align: center;'>Sistema Para Avaliação e Priorização de Projetos Estratégicos do CIEE </h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Comissão de Avaliação de Propostas de Projetos - CAPP </h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>- Central de Inovação e Projetos - CIP -</h3>", unsafe_allow_html=True)