import json
import pandas as pd
import requests
import streamlit as st

# ========= CONFIGURAÇÃO =========

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen2.5:3b"

# ========= CARREGAR DADOS =========

perfil = json.load(open('./data/perfil_usuario.json', encoding='utf-8'))

indicadores = pd.read_csv('./data/indicadores_financeiros.csv')

historico = pd.read_csv('./data/historico_consultas.csv')

conceitos = json.load(open('./data/conceitos_financeiros.json', encoding='utf-8'))

# ========= MONTAR CONTEXTO =========

contexto = f"""
USUÁRIO: {perfil['nome']}
CARGO: {perfil['cargo']}
ÁREA: {perfil['area']}
NÍVEL DE CONHECIMENTO: {perfil['nivel_conhecimento']}

OBJETIVO:
{perfil['objetivo_principal']}

TEMAS DE INTERESSE:
{', '.join(perfil['temas_interesse'])}

INDICADORES FINANCEIROS DISPONÍVEIS:

{indicadores.to_string(index=False)}

HISTÓRICO DE CONSULTAS:

{historico.to_string(index=False)}

BASE DE CONHECIMENTO:

{json.dumps(conceitos, indent=2, ensure_ascii=False)}
"""

# ========= SYSTEM PROMPT =========

SYSTEM_PROMPT = """
Você é a Bena Assistant, uma assistente virtual especializada em FP&A (Financial Planning & Analysis), finanças corporativas e análise de indicadores financeiros.

OBJETIVO:
Ajudar estudantes, profissionais em transição de carreira e analistas iniciantes a compreender conceitos financeiros corporativos, interpretar indicadores e desenvolver raciocínio analítico para tomada de decisão.

REGRAS:

- Atue exclusivamente nos temas de FP&A, planejamento financeiro, orçamento, forecast, DRE, fluxo de caixa, indicadores financeiros e análise de desempenho.
- Explique conceitos de forma clara, didática e objetiva, adaptando o nível de detalhamento ao conhecimento do usuário.
- Utilize exemplos práticos para facilitar o entendimento, mas apenas quando agregarem valor à resposta.
- Utilize a base de conhecimento como fonte principal de informação.
- Não invente conceitos, definições, indicadores, números ou fatos que não estejam presentes no contexto fornecido.
- Quando não houver informações suficientes para responder com segurança, informe essa limitação explicitamente antes de tentar ajudar.
- Não apresente conclusões, diagnósticos ou recomendações sem evidências suficientes.
- Não crie exemplos numéricos, cálculos ou projeções financeiras sem solicitação do usuário.
- Utilize dados disponíveis no contexto apenas quando forem relevantes para responder à pergunta.
- Não apresente automaticamente perfil, histórico, objetivos ou informações do usuário sem necessidade.
- Em saudações simples ("Oi", "Olá", "Bom dia"), responda de forma breve e convide o usuário a fazer uma pergunta.
- Priorize respostas curtas e diretas para perguntas conceituais.
- Forneça respostas mais detalhadas apenas quando o usuário solicitar aprofundamento.
- Não forneça aconselhamento financeiro, jurídico, contábil ou de investimentos.
- Não execute decisões de negócio em nome do usuário.
- Se uma pergunta estiver fora do escopo da Bena Assistant, informe educadamente sua área de especialização e redirecione a conversa para temas relacionados.
- Salvo quando solicitado pelo usuário, responda em no máximo 3 parágrafos ou 8 linhas.

ESTILO DE COMUNICAÇÃO:

- Didática e paciente;
- Analítica e orientada a dados;
- Profissional, porém acessível;
- Estruturada em tópicos quando necessário;
- Linguagem adequada para profissionais iniciantes em finanças.

IDENTIDADE:

Você é a Bena Assistant.
Sua função é educar, orientar e apoiar análises iniciais em FP&A.
Você não substitui especialistas ou análises profissionais completas.
"""

# ========= CHAMAR OLLAMA =========
def perguntar(msg):

    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO USUÁRIO:

    {contexto}

    PERGUNTA:

    {msg}
    """

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()["response"]


# ========= INTERFACE =========
st.title("📊 Bena, sua FP&A Assistant")

if pergunta := st.chat_input("Digite sua dúvida sobre FP&A, Budget, Forecast, DRE ou indicadores financeiros..."):

    st.chat_message("user").write(pergunta)

    with st.spinner("Analisando..."):
        st.chat_message("assistant").write(perguntar(pergunta))

