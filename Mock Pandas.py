#Problem 1
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['id']%2!=0) & (cinema['description'] != 'boring')]
    return df.sort_values(by='rating', ascending=False)
#Problem 2
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    x = my_numbers.drop_duplicates(keep=False)
    print(x.max())
    return pd.DataFrame({'num':x.max()})
    
#Problem 3
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product,on='product_id',how='left')
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df = df[(df['sale_date']>='2019-01-01') & (df['sale_date']<='2019-03-31')]
    #print(df)
    product_sales_counts = df.groupby('product_id')['sale_date'].nunique().reset_index()
    print(product_sales_counts)
  
#Problem 4  
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    users['join_date'] = pd.to_datetime(users['join_date'])
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    
    new = orders[(orders['order_date'].dt.year == 2019) & (orders['buyer_id'].isin(users['user_id']))]
    cnt = new.groupby('buyer_id').size().reset_index(name='orders_in_2019')
    print(cnt)
    result = pd.merge(users,cnt,left_on='user_id', right_on='buyer_id', how='left')
    result = result[['user_id', 'join_date', 'orders_in_2019']]
    result.rename(columns={'user_id':'buyer_id'},inplace=True)
    result = result[['buyer_id', 'join_date', 'orders_in_2019']]
    result['orders_in_2019'].fillna(0, inplace=True)
    return result
