import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="📈Ranking", page_icon="📈")

st.title("📈Ranking")

# Importando Arquivos DF
arquivo1 = "avaliacoes.xlsx"
arquivo2 = "avaliacoesAVIA.xlsx"

# Colunas Desejadas
colunas_desejadas =[
    "Média Problema",
    "Média Solução",
    "Média Formulário",
    "Média Final",
    "Avaliador"
]

# Verificação dos arquivos
if not os.path.exists(arquivo1) or not os.path.exists(arquivo2):
    st.error("Arquivos não encontrados")
else:
    df1 = pd.read_excel(arquivo1)
    df2 = pd.read_excel(arquivo2)
    st.success("Arquivos carregados com sucesso !")

    # Ranking Geral
    if "Média Final" in df1.columns and "Média Final" in df2.columns:
        st.subheader("Ranking Geral")

        media_geral_1 = df1["Média Final"].mean()
        media_geral_2 = df2["Média Final"].mean()

        ranking_df = pd.DataFrame({
            "Tabela": ["Projeto Pseudonimização", "Analista Virtual (IA)"],
            "Média Final Geral" : [media_geral_1, media_geral_2]
        }).sort_values(by="Média Final Geral", ascending=False).reset_index(drop=True) 

        ranking_df.index = ranking_df.index +1
        ranking_df.name= "Posição"

        st.dataframe(ranking_df.style.format({"Média Final Geral": "{:.2f}"})) 
        #st.table(ranking_df.to_dict(orient="records"))

        st.subheader("Comparação Visual")
        fig_rank = px.bar(
            ranking_df,
            x= "Tabela",
            y="Média Final Geral",
            color="Tabela",
            text="Média Final Geral",
            title="Média Final Geral",
            labels={"Média Final Geral": "Média"},
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_rank.update_traces(texttemplate='%{text:.2f}',textposition='outside')
        fig_rank.update_layout(yaxis_range=[0, max(ranking_df["Média Final Geral"] * 1.1)])
        st.plotly_chart(fig_rank, use_container_width=True)

        #Verifica colunas em comum
colunas_comuns = df1.columns.intersection(df2.columns)
colunas_validas = [col for col in colunas_desejadas if col in colunas_comuns]

if not colunas_validas:
    st.warning("Nenhuma das colunas desejadas está presente em ambos os arquivos.")
else:
    st.info(f"Colunas a serem comparadas: { ', '.join(colunas_validas)}")
    
    for coluna in colunas_validas:
        if pd.api.types.is_numeric_dtype(df1[coluna]) and pd.api.types.is_numeric_dtype(df2[coluna]):
            if "Avaliador" in df1.columns and "Avaliador" in df2.columns:
                st.subheader(f"Média por avaliador - {coluna}")

                media1 = df1.groupby("Avaliador")[coluna].mean()
                media2 = df2.groupby("Avaliador")[coluna].mean()

                comparacao = pd.concat([media1,media2], axis=1, keys=["Projeto Pseudononimização", "Projeto Analista Virtual (IA)"]).dropna()

                if not comparacao.empty:
                    comparacao_reset = comparacao.reset_index().melt(
                        id_vars="Avaliador",
                        var_name="Tabela",
                        value_name="Média"
                    )
                    fig = px.bar(
                        comparacao_reset,
                        x="Tabela",
                        y="Média",
                        color="Avaliador",
                        barmode="group",
                        title=f"Média por avaliador - {coluna}",
                        text_auto= ".2f",
                        color_discrete_sequence= px.colors.qualitative.Pastel
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info(f"Nenhum avaliador comum entre as duas tabelas para a coluna {coluna}.")
        elif coluna == "Avaliador":
            st.subheader("Lista de Avaliadores")
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Projeto Pseudonimização**")
                st.dataframe(df1[["Avaliador"]].drop_duplicates().reset_index(drop=True))
            with col2:
                st.write("**Projeto Analista Virtual (IA)**")
                st.dataframe(df2[["Avaliador"]].drop_duplicates().reset_index(drop=True)) 
        else:
            st.warning(f"A coluna {coluna} não é numérica.")           
st.caption("CIP - Central de Inovações e Projetos")







   