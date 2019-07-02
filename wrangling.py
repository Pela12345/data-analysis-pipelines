

# Me quedo solo con las columnas que necesito del dataset, aquellas que afectan al numero de victimas, localizacion y fecha
def selecting_columns(data):
    final_columns = ["iyear", "country_txt", "provstate", "nkill", "nwound"]
    for col in data.columns:
        if col not in final_columns:
            data=data.drop(col, axis=1)
    return data

# relleno los nulls con un 0 en el caso de variables numericas y con un unknown si no se sabe la ciudad
def filling_nulls(data):
    data[['nkill', 'nwound']] = data[['nkill', 'nwound']].fillna(0)
    data['provstate'] = data['provstate'].fillna("Uncertain")
    return data

# Cambio los nombres para que se entiendan mas facilmente
def renaming_columns(data):
    data = data.rename(columns={
                            'iyear':'Year',
                            'country_txt':'Country',
                            'provstate':'State',
                            'nkill':'Killed', 
                            'nwound':'Wounded'
                            })
    return data

# Corrijo los datos que son del tipo incorrecto, especialmente objetos y floats a integers
def correct_type(data, col):
    data[col] = data[col].astype('int64')
    return data



