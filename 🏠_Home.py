import streamlit as st
from PIL import Image

st.set_page_config(page_title="🏠 Home", page_icon="🏠")

image = Image.open('header.png')
st.image(image, caption='')
st.write("\n Nesta plataforma, sua tarefa é avaliar cada proposta de projeto em **duas dimensões:**\\"
         "\n **1** - O problema que o projeto busca resolver\\"
         "\n **2** - A solução proposta")

st.write("\nAtribua **uma nota de 0 a 5** para cada critério:\\"
         "\n •   0 -  Não atende ao critério(nota mínima)\\"
         "\n •   5 -  Atende plenamente ao critério(nota máxima)\\"
         "\n A avaliação será calculada automaticamente conforme os pesos pré definidos."
         )