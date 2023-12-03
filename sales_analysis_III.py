import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    product_id_n = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')][['product_id']].drop_duplicates()
    product_id_not = sales[(sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31')][['product_id']]
    check = product_id_n['product_id'].isin(product_id_not['product_id'])
    print(check)
    return product_id_n[~check].merge(product,on="product_id")[['product_id','product_name']]
    