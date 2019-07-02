# Wrangling of CSV 

def selecting_columns(data):
    final_columns = ["iyear", "country_txt", "provstate", "nkill", "nwound"]
    for col in data.columns:
        if col not in final_columns:
            data=data.drop(col, axis=1)
    return data

def filling_nulls(data):
    data[['nkill', 'nwound']] = data[['nkill', 'nwound']].fillna(0)
    data['provstate'] = data['provstate'].fillna("Uncertain")
    return data

def renaming_columns(data):
    data = data.rename(columns={
                            'iyear':'Year',
                            'country_txt':'Country',
                            'provstate':'State',
                            'nkill':'Killed', 
                            'nwound':'Wounded'
                            })
    return data

def correct_type(data, col):
    data[col] = data[col].astype('int64')
    return data



