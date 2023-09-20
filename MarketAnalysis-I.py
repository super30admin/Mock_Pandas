import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(users, orders, left_on = 'user_id', right_on = 'buyer_id', how = 'inner')
    df = df[(df['order_date'] >= '2019-01-01') & (df['order_date'] <= '2019-12-31')]
    df = df.groupby(['buyer_id'])['order_id'].size().reset_index(name = 'orders_in_2019')
    df2 = pd.merge(users, df, left_on ='user_id', right_on = 'buyer_id', how = 'left')
    df2['orders_in_2019'] = df2['orders_in_2019'].fillna(0).astype(int)
    return df2[['user_id', 'join_date', 'orders_in_2019']].rename(columns = {'join_date_x':'join_date', 'user_id':'buyer_id'})