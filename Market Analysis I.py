import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df_2019_orders = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')]
    df = df_2019_orders[['buyer_id', 'order_date']]
    df = df.groupby('buyer_id').size().reset_index(name='orders_in_2019')
    intrim = df.merge(users, how='right', left_on='buyer_id', right_on='user_id')
    res_df =  intrim[['user_id', 'join_date', 'orders_in_2019']]
    res_df = res_df.rename(columns={'user_id':'buyer_id'})
    res_df['orders_in_2019'] =  res_df['orders_in_2019'].fillna(0)
    return res_df