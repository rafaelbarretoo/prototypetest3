import streamlit as st
import pandas as pd
import os
from PIL import Image

# Configuração da página com layout mais amplo
st.set_page_config(
    page_title="IA para elaboração de questões em processos públicos", 
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
        <h1 style='margin:0;'>Projeto - Utilização de IA para o desenvolvimento de questões em processos públicos</h1> 
        <p style='margin:0; font-size:1.1rem;'>SUNOA -Administração Pública
Processos Seletivos Públicos - Nacional
 - Jeremias Silva</p>
    </div>
""", unsafe_allow_html=True)

# SEÇÃO DE INFORMAÇÕES DO PROJETO

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    with st.expander("🧱 **Problema Identificado**", expanded=False):
        st.markdown("""
            Compra de questões inéditas para processos seletivos públicos de todo Brasil: 
- Alto custo (entre "50,00 até 80,00 por questão).
- Prazo longo para elaboração das questões (20 dias úteis, mais 5 dias úteis para respostas a eventuais recursos de candidatos, sem custo adicional). 
- Receita inferior ou igual aos custos com o processo público em alguns casos);
- Morosidade nas formalizações contratuais, entrega de provas, preenchimento das vagas e geração de receita.
- Descontentamento dos órgãos com os prazos do CIEE;
- Previsão de não terceirização de serviços nos contratos dos órgãos com o CIEE (Banca Externa é uma terceirização; risco conhecido e assumido pelo nosso jurídico);
- Questões se tornam obsoletas e passam a ser de conhecimento dos estudantes, podendo gerar reclamações sobre o tema e colocar o processo em risco (anular o processo e gerar reclamações formais no Reclame aqui, canais do CIEE, Ministério Público e perda de credibilidade do CIEE com os órgãos públicos e estudantes). """)

with col2:
    with st.expander("💡 **Solução Proposta**", expanded=False):
        st.markdown("""
           Usar Inteligência Artificial para elaborar as questões de provas para processos seletivos públicos. Há diversas ferramentas candidatas a atender nossas necessidades e gerar os resultados pretendidos. Nenhum dado organizacional ou pessoal, sensível ou não, será necessário para alimentar a IA e obter os resultados do escopo do projeto.
Detalhamento: https://docs.google.com/presentation/d/1supb16_eyYdR5iGM_WkfAW_SUF8s_zI-rw3WpP6Ph-8/edit
        """)

with col3: 
    with st.expander("🗺️ **Roadmap do Projeto**", expanded=False):
        st.markdown("""
            **Início do Projeto: Agosto/2025**
            - Etapa 1:
                Fase atual de planejamento, alinhamentos com Tecnologia (SI e Suporte) e Jurídico (Jurídico e Privacidade) (em curso) e pesquisa de ferramentas de mercado; fluxos esperados já desenhados
            - Etapa 2:
                   Testes e aprofundamento das avaliações de pelo menos 3 ferramentas
            - Etapa 3:
                    Validação e aprovação da(s) ferramenta(s) viável(is) junto ao Jurídico (Jurídico e Privacidade) e Tecnologia (SI e Suporte) 
            - Etapa 4:
                    Testes internos em ambiente PP de homologação para confirmação das premissas e resultados com envolvimento de Tecnologia e Jurídico 
            - Etapa 5:
                    Projeto Piloto em cenário real para órgão com menor exigência nas questões e cursos de ensino médio/técnico; para confirmação das premissas e resultados com envolvimento de Tecnologia e Jurídico
            - Etapa 6:
                    Análise dos resultados do Piloto envolvendo percentual de questões que receberam recursos, pesquisa de satisfação, checagem da redução de custos e prazos; comparação de antes e depois do uso da I.A. 
            - Etapa 7:
                    Validação e aprovação final da ferramenta escolhida junto ao Jurídico (Jurídico e Privacidade) e Tecnologia (SI e Suporte) 
            - Etapa 8:
                    Implementação gradual (~ 6 meses) para novos processos seletivos públicos até o atingimento da meta para encerramento do projeto (> "60%" dos processos seletivos públicos sendo realizados com questões geradas por I.A. e ">60+ %" dos contratos de prestação de serviço cumprindo o requisito de não terceirização de serviços)     
            - Etapa 9:
                    Monitoramento e melhoria contínua (custos, recursos interpelados, prazos, cargas de trabalho, prazos para preenchimento de vagas, satisfação do cliente)
            - Etapa 10:  
                     Registro de lições aprendidas, consolidação do fluxo e encerramento do projeto 
            - Término do Projeto: Março/2026
        """)

           
     
    
col4, col5, col6, col7 = st.columns([1, 1, 1, 1])

with col4:
    with st.expander("💰 **Recursos Financeiros Previstos**", expanded=False):
        st.markdown("""
**IA = 0% (Atual, médias dos últimos 3 anos)**
Elaboração das questões (anual): 81.000,00
Trabalho colaboradores (anual): 87.600,00
Recursos (anual; valor incluso): 0,00
- **Total anual: 168.600,00**

**IA = 100% (Projeção)**
Elaboração das questões (anual): 480,00
Trabalho colaboradores (anual): 87.600,00
Recursos (anual; ~130 por ano): 6.500,00 (50 x 130)
- **Total anual:94.580,00**
- **Redução esperada por ano:  74.020,00 (43,9%)**

**IA = 60% (Projeção)**
Elaboração das questões (anual): 32.880,00 (60% IA + 40% "banca")
Trabalho colaboradores (anual): 87.600,00
Recursos (anual; ~130 por ano): 6.240,00 ( 80 x 130 x 60%)
- **Total anual: 126.720,00**
- **Redução esperada por ano: 41.880,00 (24,8%)**

**Premissas:** 
- dedicação dos colaboradores (OPEX) análogo em todos os cenários (simplificação conservadora), com maior produtividade utilizando IA
- Assinatura da plataforma Chat GPT=  479,99 por ano =  1,32 por dia;
- OPEX (trabalho de 1 assistente operando a I.A., e 1 analista validando resultados) = 240,00 por dia 
- fornecedor nos atenderia apenas para respostas aos recursos de candidatos, com o mesmo custo e prazo por recurso (5 dias úteis).
previsão de orçamento para compra de questões pode ser intercambiado para implementação do projeto
""")
        
with col5:
    with st.expander("🎯 **Resultados Esperados**", expanded=False):
        st.markdown("""
        -  Financeiro: Redução de custos (entre 25 e 44%, conforme projeções), antecipação de receita, dispensa de terceirização
        -  Produtividade: Produção de um maior número de questões em menor tempo, redução de prazos de atendimento (de 20 para 5 dias úteis para geração das questões de um processo), agilidade no preenchimento de vagas
        -   Marca: aumento de reputação, aumento da satifação do cliente, foco em atividades mais estratégicas como relacionamento com os clientes
        -  Processual / Tecnológico: Eliminação de etapas, automação, nova tecnologia aplicada (IA), manutenção do nosso banco de questões não inéditas.
 """)

with col6:
    with st.expander("🤝 **Áreas Envolvidas**", expanded=False):
        st.markdown("""
            - SUNOA: Supervisão de Operações e Atendimento da Adm. Pública 
            - SUPEX: Gerência de Tecnologia
            - SUPEX: Supervisão de Cloud Computing e Suporte de TI 
            - SUPEX: Supervisão de Segurança da Informação 
            - SUPEX: Gerência Jurídica e Compliance e DPO 
            - SUPEX: Supervisão Jurídica e de Compliance
        """)


with col7:
    st.link_button("📝 Acessar Forms do Projeto", "https://docs.google.com/spreadsheets/d/1KZbUqlQf3B_QAEH_1IoH1n-B-6nk6v3eFwO6w_5bzOM/edit?gid=1103467164#gid=1103467164",
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
            arquivo = "avaliacoes01.xlsx"

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