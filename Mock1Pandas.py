# Notboring movies
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df=cinema[(cinema['id']%2!=0) & (cinema['description']!='boring')]
    return df.sort_values('rating',ascending=False)

#Biggest Single Number

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
     return my_numbers.drop_duplicates(keep=False).max().to_frame('num')