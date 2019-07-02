import numpy as np
import pandas as pd



def binning(data2_final):
    # Uso Bins para agrupar los años con respecto a su crecimento del GDP, para ver si eran años de alto crecimiento o bajo
    mpg_labels = ['Very Low/Negative', 'Low', 'Moderate', 'High']
    bins = pd.qcut(data2_final['Growth Rate'],4, labels=mpg_labels)
    data2_final["Growth Rate"]= bins
    return data2_final

def filter_rows(data, col, country):
    # El analisis es de Estados Unidos asi que eligo las filas de ese Pais
    data = data[data[col]==country]
    return data

def create_column(data, new_col, col1, col2):
    # Funcion para unir las columnas y crear una nueva sumandolas
    data[new_col]=data[col1]+data[col2]
    cols = [new_col, col1, col2]
    data[cols] = data[cols].applymap(np.int64)
    return data

def count_attacks(data):
    # Creo una columna contando el numero de ataques, cuento las veces que aparece la palabra pais por año para sacarlo
    count = data['Country'].groupby(data['Year']).agg('count')
    # creo el dataframe agrupado por año sumando los datos de cada año
    dataX = data.groupby(["Year"]).agg({"Killed": "sum", "Wounded": "sum", "Casualties": "sum"})
    dataX["Attacks"]= count
    dataX = dataX.reset_index()
    return dataX

def merge_data(dataX, data2_final, col0):
    # Junto los datos de la api y el web scraping con el df del CSV a traves del año
    dataX[col0] = dataX[col0].astype('int64')
    data_merged = pd.merge(dataX, data2_final, on=col0)
    return data_merged

def drop_unused(data_merged, col1, col2):
    # funcion para tirar las columnas que ya no necesito al haber creado nuevas con las sumas
    data_merged.drop([col1, col2], axis=1, inplace=True)
    return data_merged



