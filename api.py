import requests
import pandas as pd


def get_api(api_url):
    # llamo a la API del OECD
    response = requests.get(api_url)
    results = response.json()
    # obtengo una columna con la tasa de crecimiento del GDP de USA a traves de una list comprehension
    growth_rate = [elem[0] for elem in results['dataSets'][0].get('observations').values()]
    # creo una lista vacia para recoger los años de la api
    year=[]
    for e in results["structure"]["dimensions"]["observation"][3]["values"]:
        year.append(e["id"])
    dict = {
    "Growth Rate": growth_rate,
    "Year": year
    }
    # Junto las dos variables obtenidas en un dataframe
    data2 = pd.DataFrame(dict)
    return data2

