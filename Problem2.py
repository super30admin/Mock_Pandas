'''
1. We drop all the duplicate entries using drop_duplicates function and keeping no entry using keep parameter
2. We require the biggest number so extract it using max function
3. Set the column name as num and create the df. return it.
'''

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame((my_numbers.drop_duplicates(keep=False).max()),columns=['num'])
    