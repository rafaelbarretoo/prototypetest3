import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(page_title="🔐 Projeto Pseudonimiação", page_icon="🔐")

def calcular_media(notas, pesos):
    return sum(n * p for n, p in zip(notas, pesos))

#Saudações

image = Image.open('headerav.png')
st.image(image, caption='')

#st.markdown(
    #"<div style='text-align: center; color: #4B0082; font-size: 30px;'>"
    #"Bem Vindo(a) ao Sistema de Avaliação de Projetos da CIP !"
    #"</div>",
    #unsafe_allow_html=True)



st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 40px;'>"
    "🔐Projeto Pseudonimização"
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 15px;'>"
    "SUPEX - Ger. Jurídica, Compliance e DPO - Raquel/Elissa"
    "</div>",
    unsafe_allow_html=True
)
st.write("")

with st.expander("\n **Resumo do Projeto**"):
    st.write("\n **Problema Identificado:**  \\"
        "\n **Recursos financeiros previstos:** \\"
        "\n **Prazo estimado de execução:**  \\"
        "\n **Resultados esperados:**\\" 
        "\n • \\"
        "\n • \\" 
        "\n • \\"
        "\n • \\"
        "\n • \\"
        "\n • \\"
        "\n • \\"
        "\n • \\"
        "\n **Áreas envolvidas:** ")
    
with st.expander("\n **Roadmap do Projeto**"):
    st.write("\n **Início do Projeto:**  \\"
        "\n • \\"
        "\n • \\"
        "\n •\\" 
        "\n • \\"
        "\n • \\" 
        "\n • \\"
        "\n • \\"
        "\n • \\"
        "\n • \\"
        "\n • \\"
        "\n • \\"
        "\n **Término do Projeto:** ")

with st.expander("**Observações CIP**"):
    st.write("Considerações da CIP referente a proposta de projetos")

st.link_button("Forms do Projeto", "https://docs.google.com/spreadsheets/d/1EOTViNNpObQ7Yz4kqWLp_S_lLkdlzqf3-3qhh_KULbA/edit?gid=1884140145#gid=1884140145")


# Título
st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 20px;'>"
    "🎯 Avaliação do Projeto Pseudonimização (Ana-IA)"
    "</div>",
    unsafe_allow_html=True
)



nomes_usuarios = ["Aline Oliveira","André Diniz", "Guilherme Carrijo","Leonardo Briza", "Marcelo Gallo","Monica Vargas", "Patricia Testai", "Paulo Ravagnani"]
avaliador = st.selectbox("Escolha o seu nome", nomes_usuarios)

st.markdown(
    "<div style='text-align: center; color: #011B70; font-size: 15px;'>"
    "Critérios - Problema"
    "</div>",
    unsafe_allow_html=True
)

#avaliador = st.text_input("Identificação do Avaliador")

# === PROBLEMA ===

#with st.expander("**Descrição do Problema:**"):
         #st.write("\nA proposta levanta o problema **da sobrecarga enfrentada pela equipe responsável pelas análises de contratos e licitações do CIEE, bem como do prazo extenso que temos para dar devolutiva às empresas que nos contratam. Além disso, a automação minimiza o risco de erros humanos, evita retrabalho, contribui para uma atuação mais alinhada às normas e fluxos internos, e torna a área mais resiliente diante de oscilações de demanda.** O problema foi avaliado como **GRAVE** pela CIP, com aparente tendência de **ESTABILIDADE**. ")

#with st.expander("**Observações:**"):
    #st.write(" \n Observações: o problema específico que o projeto quer resolver está claro; ")


st.write(" ")
st.write("**Atribua a sua avaliação !**")
gravidade = st.slider("\n**Gravidade do problema - Peso: 0,50**\\"
                      "\nO problema é sério? Pode trazer impactos relevantes se não for resolvido?"
                      , 0.0, 5.0, 0.0, step=0.5)
urgencia = st.slider("\n**Urgência de Solução do Problema - Peso: 0,30**\\"
                     "\nEssa é uma situação que exige ação imediata ou pode esperar ?"
                     , 0.0, 5.0, 0.0, step=0.5)
tendencia = st.slider("\n**Tendência do Problema - Peso: 0,20**\\"
                      "\nSe nada for feito, o problema tende a piorar, estagnar ou se resolver por contra própria? "
                      , 0.0, 5.0, 0.0, step=0.5)

notas_problema = [gravidade, urgencia, tendencia]
pesos_problema = [0.50, 0.30, 0.20]
media_problema = calcular_media(notas_problema, pesos_problema)
st.metric("Média - Problema", f"{media_problema:.2f}")

# === SOLUÇÃO ===
st.markdown(
    "<div style='text-align: center; color: #011B70; font-size: 15px;'>"
    "Critérios - Solução"
    "</div>",
    unsafe_allow_html=True
)

#with st.expander(" Descrição da Solução:"):
    #st.write("\nA solução proposta é **implementar um avatar “analista virtual”, baseado em inteligência artificial, que ficará disponível para todas as Unidades do CIEE. Esse analista virtual terá como função principal realizar a análise automática de documentos como contratos, editais e termos de referência, além de sanar dúvidas e orientar corretamente os colaboradores quanto aos fluxos internos, possibilidades de contratação, evidenciação de riscos.** Essa solução se alinha com a prioridade estratégica **“Atualização tecnológica”**, focada na redução de custos (análise de contratos) e **“Mais Eficiência / Produtividade”**, por liberar mão de obra de colaboradores que precisam tratar manualmente caso a caso, do início ao fim. A proposta, na visão da CIP tem um impacto **GRANDE** para o CIEE parece ter viabilidade **RAZOÁVEL**, quando analisamos potenciais custos, prazos e riscos. Além disso aparenta ter influência **NEUTRA** na cultura e ambiente organizacional, ser uma proposta que traz **ALTO** grau de inovação, abrangência **GRANDE** em termos de alcance de público e territorial e **MÉDIA** adaptabilidade a mudanças sejam elas tecnológicas, regulatórias, culturais, etc.")
    
#with st.expander("Observações:"):    
    #st.write(" A solução que o projeto quer implementar é descrita de forma detalhada, contribuindo de forma direta para a produtividade, segurança, inovação, evolução dos processos internos e fortalecimento do CIEE como um todo. Impacto e resultados esperados bem modelados, com espaço para ampliar indicadores - quali ou quanti - para acompanhamento dos resultados esperados descritos. Há ferramentas, benchmarks, exemplos que ilustrem o que a área espera e onde estarão estas funcionalidades nos sistemas? Apesar de não haver dados para estimar os prazos e custos da implementação, o que seria necessário para começar a implementação este ano, não parece haver subsídio ou fontes para essa estimativa antes da decisão sobre se o desenvolvimento será interno ou externo e o desenvolvedor tomar pé do escopo do projeto (o que só deve acontecer após sua aprovação). De qualquer forma, o prazo de 4 a 8 meses parece verossímil para a proposta. O início em agosto de 2025 também, apesar de depender de outros fatores, como a priorização do presente projeto.")


st.write(" ")

viabilidade_solucao = st.slider("\n**Viabilidade da Solução (Custo, Prazo, Riscos, etc.) - Peso: 0,30**\\"
                                "\n A proposta é realista? Considera bem os custos, prazos e riscos?"
                                , 0.0, 5.0, 0.0, step=0.5)
resultados_esperados = st.slider("\n**Resultados Esperados - Peso: 0,30**\\"
                                 "\nOs resultados estão bem descritos? São mensuráveis e alinhados com o objetivo do projeto?"
                                 , 0.0, 5.0, 0.0, step=0.5)
impacto_solucao = st.slider("\n**Impacto da Solução - Peso 0,20**\\"
                            "\nA solução trará benefícios concretos para o CIEE? Vai melhorar processos, resultados ou experiências? "
                            , 0.0, 5.0, 0.0, step=0.5)
alinhamento_estrategico = st.slider("\n**Alinhamento Estratégico - Peso 0,10**\\"
                                    "\n A proposta está conectada com o planejamento estratégico ou com compromissos institucionais?"
                                    , 0.0, 5.0, 0.0, step=0.5)
abrangencia = st.slider("\n**Abrangência (Público e Território) - Peso: 0,10**\\"
                        "\n O projeto atinge um grande número de pessoas, áreas ou regiões? Ou tem escopo mais limitado?"
                        , 0.0, 5.0, 0.0, step=0.5)


notas_solucao = [viabilidade_solucao, resultados_esperados, impacto_solucao, alinhamento_estrategico, abrangencia]
pesos_solucao = [0.30, 0.30, 0.20, 0.10, 0.10]
media_solucao = calcular_media(notas_solucao, pesos_solucao)
st.metric("Média - Solução", f"{media_solucao:.2f}")
### Pensar no Campo observações !!!!

observacoes = st.text_area("Deixe a sua opinião sobre o projeto avaliado:")

# === MÉDIA FINAL ===
media_geral = calcular_media(
    [media_problema, media_solucao],
    [0.50, 0.50]
)
st.subheader("Resultado Final")
st.metric("Média Final", f"{media_geral:.2f}")

if media_geral <2:
    st.write("De acordo com a sua avaliação o projeto foi **REPROVADO**")
elif media_geral <4:
    st.write("De acordo com a sua avaliação o projeto precisa ser **REVISADO**")
else:
    st.write("De acordo com a sua avaliação o projeto foi **APROVADO**")



# === SALVAR ===
if st.button("Salvar Avaliação"):
    criterios = [gravidade, urgencia,tendencia,viabilidade_solucao,resultados_esperados,
                 impacto_solucao, alinhamento_estrategico, abrangencia]
    if any(valor == 0.0 for valor in criterios):
        st.warning("Por favor, preencha todos os critérios com notas maiores que 0,0 !" )
        
    else: 
        dados = {
        "Avaliador": [avaliador],
        "Gravidade": [gravidade],
        "Urgência": [urgencia],
        "Tendência": [tendencia],
        "Média Problema": [media_problema],
        "Viabilidade da Solução": [viabilidade_solucao],
        "Resultados Esperados": [resultados_esperados],
        "Impacto da Solução": [impacto_solucao],
        "Alinhamento Estratégico e Estatutário": [alinhamento_estrategico],
        "Abrangência (Publico/Território)": [abrangencia],
        "Média Solução": [media_solucao],
        "Média Final": [media_geral],
        "Observação" : [observacoes]
    }

    df = pd.DataFrame(dados)
    arquivo = "avaliacoes.xlsx"

    if os.path.exists(arquivo):
        df_existente = pd.read_excel(arquivo)

        if avaliador in df_existente["Avaliador"].values:
            st.error("Este avaliador já preencheu a avaliação. Cada Avaliador só pode avaliar cada projeto uma vez.")
        else:
            df=pd.concat([df_existente,df], ignore_index=True)
            df.to_excel(arquivo, index=False)
            st.success("Avaliação salva com sucesso !")    
       
    else:
        df.to_excel(arquivo, index=False)
        st.success("Avaliação salva com sucesso!")

st.caption("CIP - Central de Inovações e Projetos")