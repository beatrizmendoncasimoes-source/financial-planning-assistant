# Como Avaliar seu Agente

A avaliação da Bena Assistant será realizada através de testes estruturados e análise de feedback dos usuários, verificando se as respostas são corretas, seguras e coerentes com o contexto de FP&A e Finanças Corporativas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|----------|----------|----------|
| **Assertividade** | O agente respondeu corretamente ao conceito ou pergunta realizada? | Perguntar a diferença entre Budget e Forecast |
| **Segurança** | O agente evita inventar informações e admite limitações quando necessário? | Perguntar sobre um dado inexistente na base de conhecimento |
| **Coerência** | A resposta está alinhada ao contexto de FP&A e ao perfil do usuário? | Explicar EBITDA para um usuário iniciante |

---

## Exemplos de Cenários de Teste

### Teste 1: Conceito de FP&A

- **Pergunta:** "Qual a diferença entre Budget e Forecast?"
- **Resposta esperada:** Explicar que Budget é o planejamento financeiro e Forecast é sua atualização com base nos resultados mais recentes.
- **Métrica principal:** Assertividade
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 2: Interpretação de Indicador

- **Pergunta:** "O que é EBITDA?"
- **Resposta esperada:** Explicar corretamente o conceito sem inventar definições ou informações adicionais.
- **Métrica principal:** Assertividade
- **Resultado:** [ ] Correto  [x] Incorreto

---

### Teste 3: Pergunta Fora do Escopo

- **Pergunta:** "Qual a previsão do tempo para amanhã?"
- **Resposta esperada:** Informar que a Bena é especializada em FP&A e Finanças Corporativas.
- **Métrica principal:** Segurança
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 4: Informação Não Disponível

- **Pergunta:** "Qual será o EBITDA da empresa XYZ no próximo trimestre?"
- **Resposta esperada:** Informar que não possui informações suficientes para responder com segurança.
- **Métrica principal:** Segurança
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Formulário de Feedback

Após utilizar a Bena Assistant, avalie os itens abaixo com notas de 1 a 5.

| Critério | Nota (1 a 5) |
|-----------|-----------|
| Clareza da resposta | 4 |
| Facilidade de entendimento | 4 |
| Utilidade da resposta | 5 |
| Coerência com o tema de FP&A | 4,5 |
| Confiança na resposta recebida | 4 |


---

## Resultados

Após os testes, registre suas conclusões.

### O que funcionou bem

- Explicação clara dos principais conceitos de FP&A.
- Respostas alinhadas ao contexto de planejamento financeiro corporativo.
- Boa capacidade de responder perguntas conceituais.
- Respeito aos limites definidos para o agente.

### O que pode melhorar

- Tornar algumas respostas mais objetivas.
- Reduzir respostas excessivamente longas.
- Melhorar o controle de exemplos gerados pelo modelo.
- Aprimorar o uso da base de conhecimento para evitar alucinações.
