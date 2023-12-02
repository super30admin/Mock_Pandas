import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    grp_df = my_numbers.groupby('num').size().reset_index(name='count')
    df = grp_df[grp_df['count'] == 1]
    res = df['num'].max()
    return pd.DataFrame({'num':[res]})
    
