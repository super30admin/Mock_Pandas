'''
1. We first get the records that do not fall under Q1
2. We get the records that fall under Q1
3. We need the ids that only in Q1 that means existing in Q1 but not in rest.
'''

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df1 = sales[(sales['sale_date']>'2019-03-31') | (sales['sale_date']<'2019-01-01')]
    df2 = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')]
    res = product[(~product['product_id'].isin(df1['product_id'])) &(product['product_id'].isin(df2['product_id'])) ][['product_id','product_name']]
    return res 

    