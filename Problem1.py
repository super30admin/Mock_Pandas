'''
1. We find the cinemas that have an odd id
2. Cinemas that have boring in description in description column
3. Sort the result on ratings column in descending order
'''

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema['id']%2!=0) &  ~(cinema['description'].str.contains('boring'))].sort_values('rating',ascending=False)
    