import streamlit as st
import pandas as pd
import os
from PIL import Image

# Configuração da página com layout mais amplo
st.set_page_config(
    page_title="Sistema Para Consultas de Parceiros CIEE", 
    page_icon="🔐",
    layout="wide"
)

def calcular_media(notas, pesos):
    return sum(n * p for n, p in zip(notas, pesos))

# ESTILOS E CSS CUSTOMIZADO
st.markdown("""
    <style>
        /* Estilos gerais */
        .stApp {
            background-color: #f8f9fa;
        }
        
        /* Cabeçalhos */
        .main-header {
            color: #4B0082;
            text-align: center;
            padding: 1rem;
            border-bottom: 2px solid #4B0082;
            margin-bottom: 2rem;
        }
        
        /* Cards */
        .custom-card {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            background: white;
            border-left: 4px solid #4B0082;
        }
        
        /* Sliders */
        .stSlider {
            margin-bottom: 1.5rem;
        }
        
        /* Botões */
        .stButton>button {
            background-color: #4B0082;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            margin-top: 1rem;
        }
        
        /* Expanders */
        .stExpander {
            margin-bottom: 1rem;
        }
        
        /* Métricas */
        .stMetric {
            border-radius: 5px;
            padding: 1rem;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO

# Imagem de cabeçalho
image = Image.open('headerav.png')
st.image(image, use_container_width=True)

# Título principal com destaque - Inserir nome e ícone que represente o projeto
st.markdown("""
    <div class="main-header">
        <h1 style='margin:0;'>Projeto - Sistema Para Consultas de Parceiros CIEE</h1> 
        <p style='margin:0; font-size:1.1rem;'>SUPEX - Marcelo Gallo</p>
    </div>
""", unsafe_allow_html=True)

# SEÇÃO DE INFORMAÇÕES DO PROJETO

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    with st.expander("🧱 **Problema Identificado**", expanded=False):
        st.markdown("""
- Falta de exigência e/ou dificuldade de incluir como um dos critérios no processo de tomada de decisão para contratação de fornecedores e prestadores de serviço, se os candidatos já são ou não parceiros do CIEE.
- Perda de oportunidades nos fluxos de contratação / compras para buscar novas parcerias (ou reconstrução de parcerias antigas) a partir de negociações com fornecedores que precisamos contratar (necessário envolvimento do Atendimento / SUNOA)
             """)

with col2:
    with st.expander("💡 **Solução Proposta**", expanded=False):
        st.markdown("""
- Criar um sistema simples de consulta de parceiros para ser usado como um dos critérios no processo de tomada de decisão para contratação de fornecedores e prestadores de serviço;
- Campos para consulta: CNPJ e/ou Nome da empresa
- Campos de retorno: Status da parceria (ativa / inativa); Número de aprendizes (por faixa); Número de estagiários (por faixa); Receita mensal da aprendizagem; Receita mensal do estágio; Consultor responsável; Unidade; Gerência; Segmento; Receita mensal; com possibilidade de acréscimo ou remoção de campos conforme o andamento do projeto
- Desenho de fluxo com alçadas para exigir a inclusão desse critério na tomada de decisão para contratação de fornecedores e prestadores de serviço;

OBS: consulta prévia realizada com SI, Compras e Atendimento, com sugestões já incorporadas ao escopo atual  
OBS2: protótipo preliminar (https://drive.google.com/file/d/1jH-PVBRKL0uqrzPIvzsXY29ddHy-r_0d/view?usp=drive_link )          
        """)

with col3: 
    with st.expander("🗺️ **Roadmap do Projeto**", expanded=False):
        st.markdown("""
            **Início do Projeto: 04/Agosto/2025**
            - Etapa 1:
               Alinhamentos entre todas as áreas envolvidas (apresentação da proposta + contribuições e sugestões)
            - Etapa 2:
                   Definição de escopo final
            - Etapa 3:
                    Construção de cronograma 
            - Etapa 4:
                    Prototipação final 
            - Etapa 5:
                    Desenho de fluxo operacional
            - Etapa 6:
                    Implementação
            - Etapa 7:
                    Testes e ajustes 
            - Etapa 8:
                    Divulgação interna (orientativa)     
            - Etapa 9:
                    Definição e início do monitoramento dos resultados
            - Etapa 10:
                    Encerramento e lições aprendidas  
            **Término do Projeto: 03/Outubro/2025**
        """)

           
     
    
col4, col5, col6, col7 = st.columns([1, 1, 1, 1])

with col4:
    with st.expander("💰 **Recursos Financeiros Previstos**", expanded=False):
        st.markdown("""
**Zero**
""")
        
with col5:
    with st.expander("🎯 **Resultados Esperados**", expanded=False):
        st.markdown("""
**Financeiro:**   
Aumento de receita  
**Marca:**    
Aumento de reputação, satisfação do cliente, foco em uma atividade mais estratégica relacionada ao atendimento a clientes
**Indicadores:**     
- Número de parcerias conseguidas a partir do fluxo de contratação / compras;  
- Número de estagiários conseguidos a partir do fluxo de contratação / compras;  
- Número de aprendizes conseguidos a partir do fluxo de contratação / compras;  
- Receita adicional conseguida a partir do fluxo de contratação / compras;  
- Número de acionamentos para negociações dos consultores com parceiros a partir do fluxo de contratação / compras.  
 """)

with col6:
    with st.expander("🤝 **Áreas Envolvidas**", expanded=False):
        st.markdown("""
            - SAFIN: Gerência Administrativa, de Serviços Patrimoniais e Compras / Supervisão de Gestão de Contratos Patrimonais e Compras, 
            - SUPIN: Gerência de Comunicação
            - SUPEX: Gerência de Tecnologia / Supervisão de Segurança da Informação / Supervisão de Governança de Dados e DB Analytics, 
            - SUPEX: Gerência Jurídica e Compliance e DPO / Supervisão Jurídica e de Compliance
            - SUPEX: Gerência de Pessoas / Supervisão de Desenvolvimento Humano e Organizacional
        """)


with col7:
    st.link_button("📝 Acessar Forms do Projeto", "https://docs.google.com/spreadsheets/d/1ClQ05Den_0FnNw0CBhABqRPo99xst5glGoJCoMCkRHo/edit?gid=1068529281#gid=1068529281",
                  use_container_width=True)


# SEÇÃO DE AVALIAÇÃO

st.markdown("""
    <div class="custom-card">
        <h2 style='color: #4B0082; text-align: center;'>🎯 Avaliação do Projeto </h2>
    </div>
""", unsafe_allow_html=True)

# Seleção de avaliador
nomes_usuarios = ["Aline Oliveira","André Diniz", "Guilherme Carrijo","Leonardo Briza", 
                 "Marcelo Gallo","Monica Vargas", "Patricia Testai", "Paulo Ravagnani", "Rodrigo Dib", "Usuário Teste"]
avaliador = st.selectbox("**Selecione seu nome:**", nomes_usuarios, index=None, placeholder="Escolha seu nome...")

# Opção para abster-se
if avaliador:
    abster = st.checkbox("Desejo me abster desta votação (minhas avaliações serão desconsideradas)")
else:
    abster = False

# Mostrar os critérios apenas se não estiver abstendo
if avaliador and not abster:
    # CRITÉRIOS - PROBLEMA
    st.markdown("""
        <div class="custom-card">
            <h3 style='color: #011B70; text-align: center;'>Critérios - Problema</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        gravidade = st.slider(
            "**Gravidade do problema - Peso: 0,50**\n"
            "\nO problema é sério? Pode traver impactos relevantes se não for resolvido?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixa gravidade | 5 = Extremamente grave"
        )

    with col2:
        urgencia = st.slider(
            "**Urgência de Solução do Problema - Peso: 0,30**\n"
            "\nEssa é uma situação que exige ação imediata ou pode esperar?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixa urgência | 5 = Muita urgência"
        )

    with col3:
        tendencia = st.slider(
            "**Tendência do Problema - Peso: 0,20**\n"
            "\nSe nada for feito, o problema tende a piorar, estagnar ou se resolver?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixa tendência de piora | 5 = Alta tendência de piora"
        )

    # Cálculo da média do problema
    notas_problema = [gravidade, urgencia, tendencia]
    pesos_problema = [0.50, 0.30, 0.20]
    media_problema = calcular_media(notas_problema, pesos_problema)

    # Exibição com estilo
    st.markdown(f"""
        <div class="custom-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin:0;">Média - Problema</h4>
                <div style="font-size: 1.5rem; font-weight: bold; color: {"#28a745" if media_problema >= 4 else "#ffc107" if media_problema >= 2 else "#dc3545"}">
                    {media_problema:.2f}
                </div>
            </div>
            <div style="margin-top: 0.5rem;">
                <progress value="{media_problema}" max="5" style="width:100%; height:10px; border-radius:5px; color: {"#28a745" if media_problema >= 4 else "#ffc107" if media_problema >= 2 else "#dc3545"}"></progress>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # CRITÉRIOS - SOLUÇÃO
    st.markdown("""
        <div class="custom-card">
            <h3 style='color: #011B70; text-align: center;'>Critérios - Solução</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        viabilidade_solucao = st.slider(
            "**Viabilidade da Solução - Peso: 0,30**\n"
            "\nA proposta é realista? Considera bem custos, prazos e riscos?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Inviável | 5 = Totalmente viável"
        )

        resultados_esperados = st.slider(
            "**Resultados Esperados - Peso: 0,30**\n"
            "\nOs resultados estão bem descritos? São mensuráveis?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Indefinidos | 5 = Bem definidos e mensuráveis"
        )

        impacto_solucao = st.slider(
            "**Impacto da Solução - Peso 0,20**\n"
            "\nA solução trará benefícios concretos para o CIEE?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixo impacto | 5 = Alto impacto "
        )

    with col2:
        alinhamento_estrategico = st.slider(
            "**Alinhamento Estratégico - Peso 0,10**\n"
            "\nConectada com planejamento estratégico ou compromissos institucionais?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Sem alinhamento | 5 = Totalmente alinhado"
        )

        abrangencia = st.slider(
            "**Abrangência (Público e Território) - Peso: 0,10**\n"
            "\nO projeto atinge muitas pessoas/áreas ou tem escopo limitado?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixa abrangência | 5 = Alta abrangência"
        )

    # Cálculo da média da solução
    notas_solucao = [viabilidade_solucao, resultados_esperados, impacto_solucao, alinhamento_estrategico, abrangencia]
    pesos_solucao = [0.30, 0.30, 0.20, 0.10, 0.10]
    media_solucao = calcular_media(notas_solucao, pesos_solucao)

    # Exibição com estilo
    st.markdown(f"""
        <div class="custom-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin:0;">Média - Solução</h4>
                <div style="font-size: 1.5rem; font-weight: bold; color: {"#28a745" if media_solucao >= 4 else "#ffc107" if media_solucao >= 2 else "#dc3545"}">
                    {media_solucao:.2f}
                </div>
            </div>
            <div style="margin-top: 0.5rem;">
                <progress value="{media_solucao}" max="5" style="width:100%; height:10px; border-radius:5px; color: {"#28a745" if media_solucao >= 4 else "#ffc107" if media_solucao >= 2 else "#dc3545"}"></progress>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # OBSERVAÇÕES
    observacoes = st.text_area(
        "**Deixe sua opinião sobre o projeto avaliado:**",
        placeholder="Descreva aqui suas observações, sugestões ou considerações adicionais...",
        height=200
    )

    # RESULTADO FINAL
    media_geral = calcular_media([media_problema, media_solucao], [0.50, 0.50])

    # Definir cor e status com base na média
    if media_geral < 2:
        cor_status = "#dc3545"
        status = "REPROVADO"
    elif media_geral < 4:
        cor_status = "#ffd900f6"
        status = "REVISÃO NECESSÁRIA"
    else:
        cor_status = "#28a745"
        status = "APROVADO"

    st.markdown(f"""
        <div class="custom-card">
            <h3 style='text-align: center;'>Resultado Final Individual</h3>
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="font-size: 2rem; font-weight: bold; color: {cor_status};">
                    {media_geral:.2f}
                </div>
                <div style="font-size: 1.5rem; font-weight: bold; color: {cor_status}; margin-top: 0.5rem;">
                    {status}
                </div>
                <progress value="{media_geral}" max="5" style="width:80%; height:15px; border-radius:5px; margin-top:1rem;"></progress>
            </div>
        </div>
    """, unsafe_allow_html=True)

# SALVAR AVALIAÇÃO
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("💾 Salvar Avaliação", use_container_width=True):
        if not avaliador:
            st.error("Por favor, selecione seu nome antes de salvar.")
        elif abster:
            # Se optou por abster-se, salva apenas o nome e a flag de abstenção
            dados = {
                "Avaliador": [avaliador],
                "Abstenção": ["Sim"],
                "Gravidade": [None],  # Usando None para deixar vazio
                "Urgência": [None],
                "Tendência": [None],
                "Média Problema": [None],
                "Viabilidade da Solução": [None],
                "Resultados Esperados": [None],
                "Impacto da Solução": [None],
                "Alinhamento Estratégico": [None],
                "Abrangência": [None],
                "Média Solução": [None],
                "Média Final": [None],
                "Observação": ["Avaliador optou por abster-se"]
            }
            
            df = pd.DataFrame(dados)
            arquivo = "avaliacoes01.xlsx"

            if os.path.exists(arquivo):
                df_existente = pd.read_excel(arquivo)
                if avaliador in df_existente["Avaliador"].values:
                    st.error("Este avaliador já preencheu a avaliação. Cada avaliador só pode avaliar cada projeto uma vez.")
                else:
                    df = pd.concat([df_existente, df], ignore_index=True)
                    df.to_excel(arquivo, index=False)
                    st.success("✅ Abstenção registrada com sucesso!")
            else:
                df.to_excel(arquivo, index=False)
                st.success("✅ Abstenção registrada com sucesso!")
                
        elif 'media_geral' not in locals():
            st.error("Por favor, preencha todos os critérios de avaliação.")
        else:
            # Código original para salvar avaliação normal
            dados = {
                "Avaliador": [avaliador],
                "Abstenção": ["Não"],
                "Gravidade": [gravidade],
                "Urgência": [urgencia],
                "Tendência": [tendencia],
                "Média Problema": [media_problema],
                "Viabilidade da Solução": [viabilidade_solucao],
                "Resultados Esperados": [resultados_esperados],
                "Impacto da Solução": [impacto_solucao],
                "Alinhamento Estratégico": [alinhamento_estrategico],
                "Abrangência": [abrangencia],
                "Média Solução": [media_solucao],
                "Média Final": [media_geral],
                "Observação": [observacoes]
            }

            df = pd.DataFrame(dados)
            arquivo = "avaliacoes02.xlsx"

            if os.path.exists(arquivo):
                df_existente = pd.read_excel(arquivo)
                if avaliador in df_existente["Avaliador"].values:
                    st.error("Este avaliador já preencheu a avaliação. Cada avaliador só pode avaliar cada projeto uma vez.")
                else:
                    df = pd.concat([df_existente, df], ignore_index=True)
                    df.to_excel(arquivo, index=False)
                    st.success("✅ Avaliação salva com sucesso!")
            else:
                df.to_excel(arquivo, index=False)
                st.success("✅ Avaliação salva com sucesso!")

# RODAPÉ
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #6c757d; font-size: 0.9rem;">
        CIP - Central de Inovações e Projetos | Versão 2.0
    </div>
""", unsafe_allow_html=True)