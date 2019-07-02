import pandas as pd
import json

# Cargo el dataset descargado de kaggle (el dataset fue reducido para que cupiera el tamaño en github

def load_data(file):
    data = pd.read_csv(file, encoding='ISO-8859-1')
    return data
