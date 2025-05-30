import streamlit as st
import pandas as pd
import os
import io
import plotly.express as px

st.set_page_config(page_title="📊 Projeto Pseudonimização", page_icon="📊")


st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 40px;'>"
    "Resultados das Avaliações" "<br>"
    "Projeto Pseudonimização (Ana IA)"
    "</div>",
    unsafe_allow_html=True
)

#st.title("📊 Resultados das Avaliações - Analista Virtual (Ana - IA)")

arquivo = "avaliacoes.xlsx"

df= pd.read_excel(arquivo)



media_geral_final = df["Média Final"].mean()
media_problema = df["Média Problema"].mean()
media_solucao = df["Média Solução"].mean()

col4, col5, col6, col7 = st.columns(4)
with col4:
    st.metric("Média Problema", f"{media_problema:.2f}")
with col5:
    st.metric("Média Solução", f"{media_solucao:.2f}")
with col6:
    st.metric("Média Geral", f"{media_geral_final:.2f}")
with col7:
    status = "Aprovada" if media_geral_final >= 4 else "Revisão" if media_geral_final >2 else "Reprovada"
    cor = "🟢" if media_geral_final >= 4 else "🟡" if media_geral_final >2 else "🔴"
    st.metric("Status do Projeto", f"{cor} {status}")




st.markdown("")

if os.path.exists(arquivo):
    df = pd.read_excel(arquivo)
   

    # Tabela de médias
    
    colunas_medias = [
        "Avaliador",
        "Média Problema",
        "Média Solução",
        "Média Final"
    ]
    df_medias = df[colunas_medias]
    

    # Gráfico com as médias
    st.subheader("📊 Gráfico de Médias por Avaliador")
    df_plot = df_medias.melt(id_vars=["Avaliador"], var_name="Critério", value_name="Nota")
    fig = px.bar(df_plot, x="Avaliador", y="Nota", color="Critério", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Tabela de Médias por Avaliador")
    st.dataframe(df_medias)


# Tabela completa
    st.subheader("📋 Tabela Completa")

    df.index = df.index +1
    df.name= "Posição"

    st.dataframe(df)

    media_colunas = df.mean(numeric_only= True)

    st.write("Média de cada critério")
    st.dataframe(media_colunas.to_frame(name="Média").T)

#Gráfico de matriz

st.markdown("## Matriz de Análise (Problema x Impacto)")
if "Média Problema" in df.columns and "Média Solução" in df.columns:
    fig_matrix = px.scatter(
        df,
        x="Média Problema",
        y= "Impacto da Solução",
        color = "Avaliador",
        size = "Média Final",
        hover_data=["Média Solução"],
        title= "Matriz: Gravidade do Problema vs Impacto da Solução"
    )
    st.plotly_chart(fig_matrix, use_container_width= True)
else:
    st.info("Colunas necessárias para a matriz não estão disponíveis.")

    
st.markdown("## Estatísticas por Critério")
estatisticas = df.describe().T[["mean", "50%", "std"]].rename(columns={"mean":"Média", "50%": "Mediana", "std":"Desvio Padrão"})
st.dataframe(estatisticas.style.format("{:.2f}"), use_container_width= True)



avaliadores_esperados = 8 #lembrar de substituir
total_avaliadores = df["Avaliador"].nunique()
avaliadores_pendentes = max(0, avaliadores_esperados - total_avaliadores)

col1, col2 = st.columns(2)
with col1:
    st.metric("Avaliaçõs Realizadas", total_avaliadores)
with col2:
    st.metric("Avaliações Pendentes", avaliadores_pendentes)

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
            st.write(f"**Avaliador:** {row['Avaliador']}")
            st.warning(">Não registrou comentários !")
            st.markdown("----------")
            
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


if media_geral_final <= 2:
    mensagem = "Proposta de Projeto **reprovada**"
elif 2 < media_geral_final <= 4:
    mensagem = "Proposta de projeto precisa de uma **revisão**"
else:
    mensagem = "Proposta de projeto **aprovada**"


st.markdown(f"""
            Sua média final foi: {media_geral_final:.2f}""")
st.markdown(mensagem)


st.caption("CIP - Central de Inovações e Projetos")