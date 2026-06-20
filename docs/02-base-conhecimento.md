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

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados originais do projeto eram focados em finanças pessoais e investimentos. Para alinhar o projeto à proposta da Bena Assistant, os arquivos foram adaptados para um contexto de FP&A e finanças corporativas.

As principais alterações incluíram:
- Substituição do perfil de investidor por um perfil profissional de FP&A.
- Troca dos produtos financeiros por conceitos e indicadores financeiros corporativos.
- Substituição das transações pessoais por indicadores financeiros simulados.
- Adaptação do histórico de atendimento para consultas relacionadas a planejamento financeiro, orçamento e análise de desempenho.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

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
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, agarntindo que o Agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informaçoes sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
DADOS DO CLIENTE E PERFIL (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

HISTORICO DE ATENDIMENTO DO CLIENTE (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS DISPONIVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "Dividend Yield (DY) costuma ficar entre 6% a 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto montado abaixo, se baiseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informações relevantes disponíveis em seu contexto.

```
DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: R$ 15.000)

RESUMO DE GASTOS:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

PRODUTOS DISPONÍVEIS PARA EXPLICAR:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Imobiliário - FII (risco médio)
- Fundo de Ações (risco alto)
```
