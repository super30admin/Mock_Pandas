# Sales Analysis III

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
   df1=sales[(sales['sale_date']>='2019-01-01')& (sales['sale_date']<='2019-03-31')]
   df2=sales[(sales['sale_date']<'2019-01-01')|(sales['sale_date']>'2019-03-31')]
   product=product[product['product_id'].isin(df1['product_id'])&(~product['product_id'].isin(df2['product_id']))]
   return product[['product_id','product_name']]


# Market Analysis I

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df=orders.query('order_date.dt.year==2019').merge(users, left_on='buyer_id',right_on='user_id',how='right')

    result=df.groupby(['user_id','join_date']).item_id.count()

    return result.reset_index().rename(columns={'user_id':'buyer_id','item_id':'orders_in_2019'})
    