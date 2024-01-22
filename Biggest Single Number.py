import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    singleOccurance = my_numbers.groupby('num')['num'].transform(len)==1
    df = my_numbers[singleOccurance].sort_values(by = 'num', ascending = False)
    if len(df)==0:
        return pd.DataFrame([np.NaN], columns =['num'])
    return pd.DataFrame([df.iloc[0]])

    # dictionary = {}
    # for i in range(len(my_numbers)):
    #     number = my_numbers.iloc[i]['num']
    #     if number not in dictionary:
    #         dictionary[number]=1
    #     else:
    #         dictionary[number] += 1
    # result = []
    # for key, value in dictionary.items():
    #     if value == 1:
    #         result.append(key)
    # result.sort(reverse=True)
    
    # if len(result)==0:
    #     return pd.DataFrame([np.NaN], columns = ['num'])
    # else:
    #     return pd.DateFrame([result[0]],columns = ['num'])