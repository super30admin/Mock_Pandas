import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(my_numbers['num'].value_counts())
    df = df[df['count'] == 1].sort_values(by = ['num'], ascending= False)
    df = df.reset_index()
    if df.empty:
        return pd.DataFrame([None],columns = ['num'])
    return pd.DataFrame(df['num'].head(1))

    