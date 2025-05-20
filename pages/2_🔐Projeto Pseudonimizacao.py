import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🔐 Projeto Pseudonimiação", page_icon="🔐")

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
    "🔐Projeto Pseudonimização"
    "</div>",
    unsafe_allow_html=True
)

st.write("\n **Superintendência:** SUPEX \\" 
"\n **Gerência:** Jurídica e Compliance e DPO\\"
"\n **Proponente:** Raquel Araújo\\"
"\n **Problema Identificado:** (PREENCHER)**\\"
"\n **Objetivo da proposta:**\\"
"\n **Solução sugerida:**\\"
"\n **Resultados esperados:**\\"
"\n **Principais recursos envolvidos:**\\"
"\n **Prazo estimado de execução:**")
st.link_button("Forms do Projeto", "https://docs.google.com/forms/d/e/1FAIpQLScPJUWHcnSDBV2HKEHPqUg9OOfQKl3tPqCs7KlqpvGB6b7BTA/viewform")

# Título
st.markdown(
    "<div style='text-align: center; color: #4B0082; font-size: 20px;'>"
    "🎯 Avaliação Projeto Pseudonimização"
    "</div>",
    unsafe_allow_html=True
)


#st.title("🎯 Avaliação Projeto Pseudonimização")
#st.subheader("SUPEX - Gerência Jurídica - Raquel")

nomes_usuarios = ["Nome","Aline Oliveira","André Diniz", "Guilherme Carrijo","Leonardo Briza", "Marcelo Gallo","Monica Vargas", "Patricia Testai", "Paulo Ravagnani", "Teste", "Teste1", "Teste2"]
avaliador = st.selectbox("Escolha o seu nome", nomes_usuarios)

#avaliador = st.text_input("Identificação do Avaliador")

# === PROBLEMA ===
st.markdown(
    "<div style='text-align: center; color: #011B70; font-size: 15px;'>"
    "Critérios - Problema"
    "</div>",
    unsafe_allow_html=True
) 

with st.expander("**Descrição do problema:**"):
    st.write("\n A proposta levanta o problema dos **riscos do não cumprimento integral da LGPD em nossos Sistemas, como possíveis sanções pela ANPD e dificuldades para estarmos aderentes ao self assesment de empresas parceiras ou potenciais parceiras.** O problema foi avaliado como **GRAVE** pela CIP, com aparente tendência de **PIORA**.")

#with st.expander("**Observações:**"):
    #st.write("\n O problema específico que o projeto quer resolver não está claro; há uma descrição genérica e ampla sobre como o projeto pode resolver potenciais problemas que o não cumprimento integral da LGPD em nossos sistemas podem acarretar, como possíveis sanções pela ANPD e dificuldades para estarmos aderentes ao self assesment de empresas parceiras ou potenciais parceiras. Assim, antes de pensar em como o projeto soluciona diversos aspectos, falta pensar e definir melhor o problema para estruturar e priorizar de forma mais assertiva a implementação. Por fim, sem o cenário concreto é mais difícil avaliar sua real gravidade atual, bem como a tendência de piora (que, genericamente, tende a piorar com o acúmulo de casos que podem aparecer).")


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
with st.expander("**Descrição da Solução:**"):
    st.write("A solução proposta é **“criar formas sistêmicas e automatizadas da pseudononimização dos dados, hoje inexistente”** para **“cumprimento de exigência legal”** Essa solução se alinha com a prioridade estratégica **“Assegurar um superávit estável”**, focada na redução de riscos e custos (processos e resolução de conflitos) e **“Mais Eficiência / Produtividade”**, por liberar mão de obra de colaboradores que precisam tratar manualmente caso a caso. Também está associada a: Melhor qualificação da base de estudantes, Atualização tecnológica, Tirar o máximo de cada ferramenta tecnológica, Reorganização / Descentralização e Outro (estar em conformidade com as diretrizes da LGPD). A proposta, na visão da CIP tem um impacto **GRANDE** para o CIEE parece ter **ALTA** viabilidade, quando analisamos potenciais custos, prazos e riscos. Além disso aparenta ter influência **POSITIVA** na cultura e ambiente organizacional, ser uma proposta que traz **BAIXO** grau de inovação, abrangência **GRANDE** em termos de alcance de público e territorial e **ALTA** adaptabilidade e resistência a mudanças sejam elas tecnológicas, regulatórias, culturais, etc..")

#with st.expander("**Observações:**"):
    #st.write("\n A solução que o projeto quer resolver não foi descrita; quais seriam, do ponto de vista da área proponente, as “formas sistêmicas e automatizadas da pseudononimização dos dados”? Há ferramentas, benchmarks, exemplos que ilustrem o que a área espera e onde estarão estas funcionalidades nos sistemas? Há diretrizes técnicas / boas práticas levantadas para serem usadas como premissas? Sem isso minimamente estabelecido, qualquer estimativa de prazo ou solicitação de recursos e priorização fica difícil e acaba sendo muito “chutada”. O impacto potencial pode ser alto, com influência positiva na cultura organizacional relacionada à privacidade e segurança da informação, mas a forma da solução precisa estar mais clara. Dessa forma, a medição dos impactos traz uma resposta inadequada para a pergunta, que busca refletir sobre indicadores - quali ou quanti - para acompanhamento dos resultados esperados descritos. Por fim, parece ser uma aplicação com baixo grau de inovação, voltada para uma implementação de ferramentas ou práticas já bem definidas no mercado, e potencialmente com boa resiliência para mudanças tecnológicas e regulatórias, a depender do uso dessa premissa para elaboração da solução. ")

st.markdown(
    "<div style='text-align: center; color: #011B70; font-size: 15px;'>"
    "Critérios - Solução"
    "</div>",
    unsafe_allow_html=True
)
st.write(" ")

viabilidade_solucao = st.slider("\n**Viabilidade da Solução (Custo, Prazo, Riscos, etc.) - Peso: 0,30**\\"
                                "\n A proposta é realista? Considera bem os custos, prazos e riscos?"
                                , 0.0, 5.0, 0.0, step=0.5)
resultados_esperados = st.slider("\n**Resultados Esperados - Peso: 0,30**\\"
                                 "\nOs resultados estão bem descritos? São mensuráveis e alinhados com o objetivo do projeto?"
                                 , 0.0, 5.0, 0.0, step=0.5)
impacto_solucao = st.slider("\n**Impacto da Solução - Peso 0,20**\\"
                            "\n**A solução trará benefícios concretos para o CIEE? Vai melhorar processos, resultados ou experiências?** "
                            , 0.0, 5.0, 0.0, step=0.5)
alinhamento_estrategico = st.slider("\n**Alinhamento Estratégico e Estatutário - Peso 0,10**\\"
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

### Pensar no Campo observações !!!!

observacoes = st.text_area("Deixe a sua opinião sobre o projeto avaliado:")

# === SALVAR ===
if st.button("Salvar Avaliação"):
    dados = {
        "Avaliador": [avaliador],
        "Gravidade": [gravidade],
        "Urgência": [urgencia],
        "Tendência": [tendencia],
        "Média Problema": [media_problema],
        "Viabilidade da Solução": [viabilidade_solucao],
        "Impacto da Solução": [impacto_solucao],
        "Alinhamento Estratégico e Estatutário": [alinhamento_estrategico],
        "Abrangência (Publico/Território)": [abrangencia],
        "Média Solução": [media_solucao],
        "Resultados Esperados": [resultados_esperados],
        "Média Final": [media_geral],
        "Observação" : [observacoes]
    }

    df = pd.DataFrame(dados)
    arquivo = "avaliacoes.xlsx"

    if os.path.exists(arquivo):
        df_existente = pd.read_excel(arquivo)
        df = pd.concat([df_existente, df], ignore_index=True)

    df.to_excel(arquivo, index=False)
    st.success("Avaliação salva com sucesso!")

st.caption("CIP - Central de Inovações e Projetos")