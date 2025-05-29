import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🤖 Projeto Analista Virtual (Ana IA)", page_icon="🤖")

def calcular_media(notas, pesos):
    return sum(n * p for n, p in zip(notas, pesos))

#Saudações
st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 30px;'>"
    "Bem Vindo(a) ao Sistema de Avaliação de Projetos da CIP !"
    "</div>",
    unsafe_allow_html=True
)

st.write("\n Nesta plataforma, sua tarefa é avaliar cada proposta de projeto em **duas dimensões**\\"
         "\n **1** - O problema que o projeto busca resolver\\"
         "\n **2** - A solução proposta")

st.write("\nAtribua **uma nota de 0 a 5** para cada critério:\\"
         "\n •   0 -  Não atende ao critério(nota mínima)\\"
         "\n •   5 -  Atende plenamente ao critério(nota máxima)\\"
         "\n A avaliação será calculada automaticamente conforme os pesos pré definidos."
         )

st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 40px;'>"
    "🤖Projeto Analista Virtual (ANA - IA)"
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 15px;'>"
    "SUPEX - Ger. Jurídica, Compliance e DPO / Sup. de Administração de Contratos e CNL - Fabrício Canonaco"
    "</div>",
    unsafe_allow_html=True
)
st.write("")

with st.expander("\n **Resumo do Projeto**"):
    st.write("\n **Problema Identificado:** Gargalos operacionais (sobrecarga da equipe de análises de contratos e licitações), que geram SLA extenso nas respostas às Unidades de Operação e empresas. \\"
        "\n **Solução sugerida:** Implementação de analista virtual baseado em IA em ambiente digital acessível (portal, chat ou widget) para realizar a análise automática de documentos como contratos, editais e termos de referência, além de sanar dúvidas e orientar corretamente os colaboradores quanto aos fluxos internos, possibilidades de contratação, evidenciação de riscos. \\"
        "\n **Recursos financeiros previstos:** Não previsto.\\"
        "\n **Prazo estimado de execução:** 4-8 Meses \\"
        "\n **Resultados esperados:**\\" 
        "\n • Maior produtividade;\\"
        "\n • Maior satisfação dos clientes internos e externos;\\" 
        "\n • Respostas instantâneas e padronizadas;\\"
        "\n • Suporte em tempo real para dúvidas operacionais, contratações e interpretação de documentos durante as negociações com os parceiros;\\"
        "\n • Redução de riscos jurídicos e administrativos, como erros humanos, inconsistências e retrabalho;\\"
        "\n • Mapeamento de possíveis riscos ou exigências em cada situação;\\"
        "\n • Relatórios gerenciais sobre tipos de solicitações e demandas processadas;\\"
        "\n • Escalabilidade compatível com demanda crescente.\\"
        "\n **Áreas envolvidas:** Sup. de Administração de Contratos e CNL, Ger. de Tecnologia, Sup. de Cloud Computing e Suporte de TI, Sup. de Desenvolvimento de Sistemas e Processos de Atendimento, Sup. de Segurança da Informação, Sup. de Governança de Dados e DB Analytics, Ger. Jurídica e Compliance e DPO, Ger. Regional de Atendimento SP e Capital. ")

with st.expander("**Observações CIP**"):
    st.write("Problema bem definido (alguns quantitativos poderiam ajudar a ilustrar ainda melhor); solução clara com etapas bem definidas para implementação (roadmap com 7 etapas / entregas); prazo de 4 a 8 meses parece verossímil para a proposta; interessante para pilotar uso de IA nos fluxos e processos da organização; impacto e resultados esperados bem mapeados, com espaço para ampliar indicadores - quali ou quanti - para acompanhamento dos resultados esperados descritos. Incluir ferramentas, benchmarks, exemplos que ilustrem o que a área espera e as funcionalidades no sistema. Para desenvolvimento terceirizado e início em 2025, é imprescindível orçar e incluir os custos na revisão orçamentária; incluir áreas da SUNOA para acompanhar o desenvolvimento da solução e o setor de Governança de Dados e DBA.")

st.link_button("Forms do Projeto", "https://docs.google.com/spreadsheets/d/1EOTViNNpObQ7Yz4kqWLp_S_lLkdlzqf3-3qhh_KULbA/edit?gid=1884140145#gid=1884140145")


# Título
st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 20px;'>"
    "🎯 Avaliação do Projeto Analista Virtual (Ana-IA)"
    "</div>",
    unsafe_allow_html=True
)

#st.title("🎯 Avaliação Projeto Pseudonimização")
#st.subheader("SUPEX - Gerência Jurídica - Raquel")

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
    arquivo = "avaliacoesAVIA.xlsx"

    if os.path.exists(arquivo):
        df_existente = pd.read_excel(arquivo)
        df = pd.concat([df_existente, df], ignore_index=True)

    df.to_excel(arquivo, index=False)
    st.success("Avaliação salva com sucesso!")

st.caption("CIP - Central de Inovações e Projetos")