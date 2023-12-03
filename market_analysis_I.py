import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')][['order_id','buyer_id']]
    orders =  orders.groupby('buyer_id').count().reset_index()
    df = users.merge(orders,how='left',left_on = "user_id",right_on="buyer_id")[['user_id','join_date','order_id']]
    df = df.rename(columns = {'user_id':'buyer_id','order_id':'orders_in_2019'})
    return df.fillna(0)
