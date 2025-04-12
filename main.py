from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def main():
    df = extract_data('data/raw/vendas.csv')
    df_tratado = transform_data(df)
    load_data(df_tratado, 'data/processed/relatorio_vendas.csv')

if __name__ == "__main__":
    main()