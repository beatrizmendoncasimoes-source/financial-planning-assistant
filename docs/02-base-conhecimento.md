# Base de Conhecimento


## Dados Utilizados

| Arquivo | Formato | Para que serve na Bena? |
|---------|---------|---------------------|
| `historico_consultas.csv` | CSV | Registrar temas já discutidos com o usuário e fornecer contexto para atendimentos futuros. |
| `perfil_usuario.json` | JSON | Identificar o perfil profissional, nível de conhecimento e objetivos do usuário para personalizar as explicações. |
| `conceitos_financeiros.json` | JSON | Servir como base de conhecimento sobre FP&A, indicadores financeiros e conceitos de planejamento financeiro. |
| `indicadores_financeiros.csv` | CSV | Disponibilizar dados financeiros simulados para exemplos, análises e interpretação de indicadores. |

---

## Adaptações nos Dados

Os dados originais do projeto eram focados em finanças pessoais e investimentos. Para alinhar o projeto à proposta da Bena Assistant, os arquivos foram adaptados para um contexto de FP&A e finanças corporativas.

As principais alterações incluíram:
- Substituição do perfil de investidor por um perfil profissional de FP&A.
- Troca dos produtos financeiros por conceitos e indicadores financeiros corporativos.
- Substituição das transações pessoais por indicadores financeiros simulados.
- Adaptação do histórico de atendimento para consultas relacionadas a planejamento financeiro, orçamento e análise de desempenho.

---

## Estratégia de Integração

### Como os dados são carregados?

A aplicação carrega os arquivos JSON e CSV para compor o contexto utilizado pelo modelo de linguagem. Dessa forma, a Bena Assistant consegue gerar respostas mais alinhadas ao perfil do usuário e aos conceitos disponíveis em sua base de conhecimento.

```python
import pandas as pd
import json

perfil = json.load(open('./data/perfil_usuario.json'))
indicadores = pd.read_csv('./data/indicadores_financeiros.csv')
historico = pd.read_csv('./data/historico_consultas.csv')
conceitos = json.load(open('./data/conceitos_financeiros.json'))
```

### Exemplo de Contexto Enviado ao LLM
```text
Usuário:
Mariana Oliveira

Cargo:
Analista Financeira Júnior

Área:
FP&A

Nível de conhecimento:
Iniciante

Objetivo:
Desenvolver habilidades em planejamento financeiro e análise de indicadores.

Temas de interesse:
- Budget
- Forecast
- DRE
- EBITDA
- Fluxo de Caixa

Histórico recente:
- Explicação sobre EBITDA
- Processo de Forecast mensal
- Construção de Budget anual

Base de conhecimento disponível:
- Conceitos de Budget
- Conceitos de Forecast
- EBITDA
- Fluxo de Caixa
- Real vs Budget

Pergunta do usuário:
"Qual a diferença entre Budget e Forecast?"
```

Esse contexto fornece ao modelo informações suficientes para gerar respostas mais personalizadas, mantendo o foco em educação financeira corporativa e conceitos de FP&A.

---

### Como os dados são usados no prompt?

Para simplificar o protótipo, os dados da base de conhecimento são incorporados diretamente ao contexto enviado ao modelo de linguagem. Dessa forma, a Bena Assistant consegue responder utilizando informações específicas sobre o perfil do usuário, conceitos financeiros e indicadores disponíveis.

Em uma solução mais robusta, os arquivos seriam consultados dinamicamente por meio de funções de busca e recuperação de contexto (RAG), permitindo atualização contínua da base de conhecimento sem necessidade de alterar os prompts.

```text
PERFIL DO USUÁRIO (data/perfil_usuario.json)

{
  "nome": "Mariana Oliveira",
  "cargo": "Analista Financeira Júnior",
  "area": "FP&A",
  "objetivo_principal": "Desenvolver habilidades em planejamento financeiro e análise de indicadores",
  "nivel_conhecimento": "iniciante",
  "anos_experiencia": 1,
  "temas_interesse": [
    "Budget",
    "Forecast",
    "DRE",
    "EBITDA",
    "Fluxo de Caixa"
  ]
}

INDICADORES FINANCEIROS DISPONÍVEIS (data/indicadores_financeiros.csv)

periodo,indicador,valor
2025-01,Receita,1200000
2025-01,Custos,850000
2025-01,EBITDA,180000
2025-02,Receita,1250000
2025-02,Custos,900000
2025-02,EBITDA,175000
2025-03,Receita,1300000
2025-03,Custos,910000
2025-03,EBITDA,210000

HISTÓRICO DE CONSULTAS (data/historico_consultas.csv)

data,canal,tema,resumo,resolvido
2025-09-15,chat,EBITDA,Usuário solicitou explicação sobre cálculo e interpretação do EBITDA,sim
2025-09-22,chat,Forecast,Usuário pediu orientação sobre processo de Forecast mensal,sim
2025-10-01,chat,Budget,Usuário solicitou explicação sobre construção de orçamento anual,sim

BASE DE CONHECIMENTO (data/conceitos_financeiros.json)

[
  {
    "nome": "Budget",
    "categoria": "Planejamento Financeiro",
    "descricao": "Planejamento financeiro elaborado para um período futuro."
  },
  {
    "nome": "Forecast",
    "categoria": "Planejamento Financeiro",
    "descricao": "Atualização periódica das projeções financeiras."
  },
  {
    "nome": "EBITDA",
    "categoria": "Indicador Financeiro",
    "descricao": "Indicador que mede o resultado operacional antes de juros, impostos, depreciação e amortização."
  }
]
```
---

## Exemplo de Contexto Montado

O exemplo de contexto abaixo sintetiza as informações mais relevantes da base de conhecimento da Bena Assistant. O objetivo é fornecer contexto suficiente para respostas personalizadas sem consumir uma quantidade excessiva de tokens. Em aplicações reais, o nível de detalhamento deve ser ajustado conforme a complexidade da solicitação do usuário.

```text
DADOS DO USUÁRIO:
- Nome: Mariana Oliveira
- Cargo: Analista Financeira Júnior
- Área: FP&A
- Nível de conhecimento: Iniciante
- Objetivo: Desenvolver habilidades em planejamento financeiro e análise de indicadores

TEMAS DE INTERESSE:
- Budget
- Forecast
- DRE
- EBITDA
- Fluxo de Caixa

HISTÓRICO RECENTE:
- Solicitou explicação sobre EBITDA
- Buscou orientação sobre processo de Forecast
- Solicitou explicação sobre construção de Budget

INDICADORES DISPONÍVEIS:
- Receita Jan/2025: R$ 1.200.000
- Custos Jan/2025: R$ 850.000
- EBITDA Jan/2025: R$ 180.000
- Receita Fev/2025: R$ 1.250.000
- EBITDA Fev/2025: R$ 175.000

CONCEITOS DISPONÍVEIS PARA EXPLICAÇÃO:
- Budget
- Forecast
- EBITDA
- Fluxo de Caixa
- Real vs Budget

PERFIL DA ASSISTENTE:
- Especialista em FP&A e finanças corporativas
- Explica conceitos de forma didática
- Auxilia na interpretação de indicadores financeiros
- Sugere hipóteses para análise
- Não substitui análise profissional especializada
```
