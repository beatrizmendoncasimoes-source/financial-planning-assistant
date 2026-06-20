# Passo a Passo de Execução

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull qwen2.5:3b

# 3. Testar se funciona
ollama run qwen2.5:3b "Olá!"
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run .\src\app.py
```

## Evidência de Execução

<img width="598" height="579" alt="evidencia_execucao" src="https://github.com/user-attachments/assets/b83c6e20-c666-4f74-9d97-c83ccfadb072" />

