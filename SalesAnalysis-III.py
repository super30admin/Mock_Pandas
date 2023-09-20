import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales1 = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')]
    sales2 = sales[~((sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31'))]
    sales3 = sales1.merge(sales2, left_on='product_id', right_on='product_id', how='left')
    sales4 = sales3[sales3['price_y'].isna()]
    df = sales4.merge(product, left_on='product_id', right_on='product_id', how='inner')
    return df[['product_id', 'product_name']].drop_duplicates()
