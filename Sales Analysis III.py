import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    first_quarter = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')]
    other_quarters = sales[(sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31')]
    ids = first_quarter[~first_quarter['product_id'].isin(other_quarters['product_id'])]['product_id']
    return product[product['product_id'].isin(ids)][['product_id', 'product_name']]