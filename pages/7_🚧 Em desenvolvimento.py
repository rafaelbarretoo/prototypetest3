import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("Comparativo de Resultados")

arquivo1 = "avaliacoes.xlsx"
arquivo2 = "avaliacoesAVIA.xlsx"

colunas_desejadas =[
    "Média Problema",
    "Média Solução",
    "Média Formulário",
    "Média Final",
    "Avaliador"
]

if not os.path.exists(arquivo1) or not os.path.exists(arquivo2):
    st.error("Arquivos não encontrados")
else:
    df1 = pd.read_excel(arquivo1)
    df2 = pd.read_excel(arquivo2)
    st.success("Arquivos carregados com sucesso !")


    colunas_comuns = df1.columns.intersection(df2.columns)
    colunas_validas = [col for col in colunas_desejadas if col in colunas_comuns]

    if not colunas_validas:
        st.warning("Nenhuma das colunas desejadas está presente em ambos os arquivos.")
    else:
        st.info(f"Colunas a serem comparadas: {', '.join(colunas_validas)}")

        for coluna in colunas_validas:
            if pd.api.types.is_numeric_dtype(df1[coluna]) and  pd.api.types.is_numeric_dtype(df2[coluna]):
                if "Avaliador" in df1.columns and "Avaliador" in df2.columns:
                    st.subheader(f"Média por Avaliador - {coluna} ")

                    media1 = df1.groupby("Avaliador")[coluna].mean()
                    media2 = df2.groupby("Avaliador")[coluna].mean()

                    comparacao = pd.concat([media1, media2], axis=1, keys=["Pseudonimização", "Agente de IA"])
                    comparacao = comparacao.dropna()

                    if not comparacao.empty:
                        fig, ax = plt.subplots(figsize=(10, 4))
                        comparacao.plot(kind="bar", ax=ax)
                        ax.set_ylabel("Média")
                        ax.set_xlabel("Avaliador")
                        ax.set_title(f'Média por Avaliador - {coluna}')
                        ax.legend()
                        plt.xticks(rotation=45, ha='right')
                        st.pyplot(fig)
                    else:
                        st.info(f"Nenhum avaliador comum entre as duas tabelas para a coluna ´{coluna}´")
            elif coluna == "Avaliador":
                st.subheader("Lista de Avaliadores")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("** Projeto Pseudonimização **")
                    st.dataframe(df1[["Avaliador"]].drop_duplicates().reset_index(drop=True))
                with col2:
                   st.write("** Projeto Agente de IA **")
                   st.dataframe(df2[["Avaliador"]].drop_duplicates().reset_index(drop=True)) 
            else:
                st.warning(f'A Coluna ´{coluna}´ não é numérica.')


if "Média Final" in df1.columns and "Média Final" in df2.columns:
    st.subheader("Ranking")

    media_geral_1 = df1["Média Final"].mean()
    media_geral_2 = df2["Média Final"].mean()

    ranking_df = pd.DataFrame({
        "Tabela": ["Projeto Pseudonimização", "Projeto Agente de IA"],
        "Média Final Geral": [media_geral_1, media_geral_2]
    }).sort_values(by="Média Final Geral", ascending=False).reset_index(drop=True)

    st.dataframe(ranking_df.style.format({"Média Final Geral": "{:.2f}"}))

    #Gráfico de Barras Simples

    st.subheader("Comparativo Visual - Projetos Avaliados")
    fig, ax = plt.subplots()
    ax.bar(ranking_df["Tabela"], ranking_df["Média Final Geral"], color=["#1f77b4","#ff7f0e"])
    ax.set_ylabel("Média Final")
    ax.set_title("Comparativo de Média Final entre Projetos")
    st.pyplot(fig)