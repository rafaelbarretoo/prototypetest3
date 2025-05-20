import streamlit as st
import pandas as pd
import os
import io
import plotly.express as px

st.set_page_config(page_title="📊 Projeto Pseudonimização", page_icon="📊")


st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 40px;'>"
    "Resultados das Avaliações" "<br>"
    "Projeto Pseudonimização"
    "</div>",
    unsafe_allow_html=True
)
#st.title("📊 Resultados das Avaliações - Projeto Pseudonimização")

arquivo = "avaliacoes.xlsx"

df= pd.read_excel(arquivo)
media_geral_final = df["Média Final"].mean()

st.markdown(f"""
            Após as avaliações, a média geral das avaliações foi: {media_geral_final:.2f}""")

if media_geral_final <= 2:
    mensagem = st.warning("Proposta de Projeto **reprovada**")
elif 2 < media_geral_final <= 4:
    mensagem ="Proposta de projeto precisa de uma **revisão**"
else:
    mensagem = st.success("Proposta de projeto **aprovada**")

st.markdown(mensagem)

st.markdown("")

if os.path.exists(arquivo):
    df = pd.read_excel(arquivo)

# Tabela completa
    st.subheader("📋 Tabela Completa")

    df.index = df.index +1
    df.name= "Posição"

    st.dataframe(df)

    # Tabela de médias
    st.subheader("📈 Tabela de Médias por Avaliador")
    colunas_medias = [
        "Avaliador",
        "Média Problema",
        "Média Solução",
        "Média Final"
    ]
    df_medias = df[colunas_medias]
    
    #df_medias.index = df_medias.index +1
    #df_medias.name= "Posição"

    st.dataframe(df_medias)

    # Gráfico com as médias
    st.subheader("📊 Gráfico de Médias por Avaliador")
    df_plot = df_medias.melt(id_vars=["Avaliador"], var_name="Critério", value_name="Nota")
    fig = px.bar(df_plot, x="Avaliador", y="Nota", color="Critério", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    

    # Média geral final
    media_geral_final = df["Média Final"].mean()
    st.success(f"🎯 Média Geral Final (todos os avaliadores): {media_geral_final:.2f}")

# Comentários e Observações 
if "Avaliador" in df.columns and "Observação" in df.columns:
    st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 25px;'>"
    "Observações e comentários"
    "</div>",
    unsafe_allow_html=True
)

    for index, row in df.iterrows():
        if pd.notna(row["Observação"]):
            with st.container():
                st.write(f"**Avaliador:** {row['Avaliador']} ")
                st.info(f">{row['Observação']}")
                st.markdown("----------")
        else:
            st.warning("Não foram registradas observações e comentários !")



    # Botões de download
    st.subheader("⬇️ Exportar Tabelas")

    # CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    st.download_button("Download CSV", csv_buffer.getvalue(), file_name="avaliacoes.csv", mime="text/csv")

    # Excel
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    st.download_button("Download Excel", excel_buffer.getvalue(), file_name="avaliacoes.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

else:
    st.warning("Ainda não há avaliações salvas.")



#if media_geral_final <= 2:
    #mensagem = "Proposta de Projeto **reprovada**"
#elif 2 < media_geral_final <= 4:
    #mensagem = "Proposta de projeto precisa de uma **revisão**"
#else:
    #mensagem = "Proposta de projeto **aprovada**"


#st.markdown(f"""
            #Sua média final foi: {media_geral_final:.2f}""")
#st.markdown(mensagem)


st.caption("CIP - Central de Inovações e Projetos")
 