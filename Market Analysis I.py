import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = orders['order_date'].dt.year
    orders = orders[orders['order_date']==2019]
    df = orders.groupby('buyer_id').size().reset_index(name = 'orders_in_2019')
    df = users.merge(df, left_on = 'user_id', right_on = 'buyer_id', how = 'left')
    df['orders_in_2019'] = df['orders_in_2019'].fillna(0).astype(int)
    df = df[['user_id','join_date','orders_in_2019']]
    return df.rename(columns = {'user_id': 'buyer_id'})