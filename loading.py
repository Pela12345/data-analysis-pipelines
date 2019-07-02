import pandas as pd
import json

def load_data(file):
    data = pd.read_csv(file, encoding='ISO-8859-1')
    return data
