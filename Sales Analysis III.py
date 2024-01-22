import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df1 = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date']<= '2019-03-31')]
    df2 = sales[~((sales['sale_date'] >= '2019-01-01') & (sales['sale_date']<= '2019-03-31'))]
    df3 = df1.merge(df2, left_on = 'product_id', right_on = 'product_id', how = 'left')
    df4 = df3[df3['price_y'].isna()]
    df = df4.merge(product, left_on = 'product_id', right_on = 'product_id', how = 'inner')
    return df[['product_id', 'product_name']].drop_duplicates()
    