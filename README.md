# ETL Pipeline em Python - Loja de Vendas

Este projeto simula um processo ETL usando Python puro. O objetivo é coletar dados brutos de vendas de uma loja, realizar tratamento e transformação dos dados, e gerar um relatório final pronto para análise.

## Estrutura

- `extract.py`: Leitura dos dados
- `transform.py`: Limpeza e criação de nova coluna
- `load.py`: Gera arquivo final
- `main.py`: Orquestra o pipeline

## Como rodar

1. Instale as dependências:
pip install pandas

markdown
Copy
Edit

2. Rode o projeto:
python main.py

markdown
Copy
Edit

## Resultado
Arquivo `relatorio_vendas.csv` na pasta `data/processed/`