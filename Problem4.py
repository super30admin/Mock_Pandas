'''
Method 1: 
1. We first group by the users on buyer_id in filtered (ordered in year 2019) orders table to get the number of purchases made.
2. Join users table on user_id and this result on buyer id to get the number of orderes made by each user. Fill with 0s if they didnt make a purchase.
Method 2:
1. Get the buyers filtered using between function, use groups to get the values as a dictionary.
2. Create the result df with the values from this dictionary.
'''

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df = orders[orders['order_date'].apply(lambda x: x.year==2019)].groupby(['buyer_id'])['order_id'].size()
    df = users.merge(df,how='left',left_on='user_id',right_on='buyer_id').fillna(0).rename(columns={'user_id':'buyer_id','order_id':'orders_in_2019'})
    return df[['buyer_id','join_date','orders_in_2019']]
    

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    buy_group = dict(orders[orders['order_date'].between(
        '2019-01-01', '2019-12-31')].groupby('buyer_id').groups)
    return pd.DataFrame({
        'buyer_id': users.user_id,
        'join_date': users.join_date,
        'orders_in_2019': [len(buy_group.get(user, [])) for user in users.user_id ]
    })