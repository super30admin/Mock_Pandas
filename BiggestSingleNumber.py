import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.groupby('num').size().reset_index(name = 'cnt')
    df = df[df['cnt'] == 1]
    if len(df) < 1:
        return pd.DataFrame({'num': [None]})
    df = df.sort_values(by = 'num', ascending = False)
    return pd.DataFrame({'num': df['num']}).head(1)