#Question 1  :
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[~(cinema['id'] % 2 == 0) & ~(cinema['description'] == "boring") ]
    return cinema.sort_values(by = 'rating' , ascending = False)

#Question 2 :
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    
   x = my_numbers['num'].drop_duplicates(keep=False)

   return pd.DataFrame({ 'num' :[max(x, default = None )]}) 

#Question3 : 
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales = sales.groupby('product_id')['sale_date'].agg(['min','max']).reset_index()
    sales = sales[(sales['min'] >= '2019-01-01') & (sales['max'] <= '2019-04-30') ]
    product = product.merge(sales , how = 'inner' , on = 'product_id')
    return product[['product_id' , 'product_name']]

#Question4 :
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')]
    df = orders.groupby('buyer_id').size().reset_index(name = 'orders_in_2019')
    users = users.merge(df,left_on = 'user_id', right_on = 'buyer_id' , how = 'left')
    users['orders_in_2019'] = users['orders_in_2019'].fillna(0)

    return users[['user_id','join_date','orders_in_2019']].rename(columns = {'user_id' : 'buyer_id'})