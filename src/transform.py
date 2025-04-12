def transform_data(df):
    df['total_venda'] = df['quantidade'] * df['preco_unitario']
    df.columns = [col.lower() for col in df.columns]
    return df