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

st.markdown("<h1 style='text-align: center;'>Propostas de projeto em aberto</h1>", unsafe_allow_html=True)

st.subheader("Projeto 1")
st.write("\n Superintendência:  \\" 
"\n Gerência: \\"
"\n Proponente: \\"
"\n Conheça melhor a proposta: LINK DO FORMS")
st.page_link("pages/Avaliacao Projetos.py", label="Avaliação Projeto 1")

st.subheader("Projeto 2")
st.write("\n Superintendência:  \\" 
"\n Gerência: \\"
"\n Proponente: \\"
"\n Conheça melhor a proposta: LINK DO FORMS")
st.page_link("pages/Avaliacao Projetos.py", label="Avaliação Projeto 2")

st.subheader("Projeto 3")
st.write("\n Superintendência: \\" 
"\n Gerência: \\"
"\n Proponente: \\"
"\n Conheça melhor a proposta: ")
st.page_link("pages/Avaliacao Projetos.py", label="Avaliação Projeto 3")

st.subheader("Projeto 4")
st.write("\n Superintendência: \\" 
"\n Gerência: \\"
"\n Proponente: \\"
"\n Conheça melhor a proposta: ")
st.page_link("pages/Avaliacao Projetos.py", label="Avaliação Projeto 4")

st.subheader("Projeto 5")
st.write("\n Superintendência: \\" 
"\n Gerência: \\"
"\n Proponente: \\"
"\n Conheça melhor a proposta: ")
st.page_link("pages/Avaliacao Projetos.py", label="Avaliação Projeto 5")

st.subheader("Projeto 6")
st.write("\n Superintendência: \\" 
"\n Gerência: \\"
"\n Proponente: \\"
"\n Conheça melhor a proposta: ")
st.page_link("pages/Avaliacao Projetos.py", label="Avaliação Projeto 6")