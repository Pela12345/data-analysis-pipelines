import numpy as np
import pandas as pd



def binning(data2_final):
    mpg_labels = ['Very Low/Negative', 'Low', 'Moderate', 'High']
    bins = pd.qcut(data2_final['Growth Rate'],4, labels=mpg_labels)
    data2_final["Growth Rate"]= bins
    return data2_final

def filter_rows(data, col, country):
    data = data[data[col]==country]
    return data

def create_column(data, new_col, col1, col2):
    data[new_col]=data[col1]+data[col2]
    cols = [new_col, col1, col2]
    data[cols] = data[cols].applymap(np.int64)
    return data

def count_attacks(data):
    count = data['Country'].groupby(data['Year']).agg('count')
    dataX = data.groupby(["Year"]).agg({"Killed": "sum", "Wounded": "sum", "Casualties": "sum"})
    dataX["Attacks"]= count
    dataX = dataX.reset_index()
    return dataX

def merge_data(dataX, data2_final, col0):
    dataX[col0] = dataX[col0].astype('int64')
    data_merged = pd.merge(dataX, data2_final, on=col0)
    return data_merged

def drop_unused(data_merged, col1, col2):
    data_merged.drop([col1, col2], axis=1, inplace=True)
    return data_merged



