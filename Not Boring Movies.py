import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['id']%2 == 1) & (cinema['description'] != 'boring')]
    df = df.sort_values(by='rating', ascending=False)
    return df