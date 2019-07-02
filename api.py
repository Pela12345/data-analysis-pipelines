import requests
import pandas as pd

def get_api(api_url):  
    response = requests.get(api_url)
    results = response.json()
    growth_rate = [elem[0] for elem in results['dataSets'][0].get('observations').values()]
    year=[]
    for e in results["structure"]["dimensions"]["observation"][3]["values"]:
        year.append(e["id"])
    dict = {
    "Growth Rate": growth_rate,
    "Year": year
    }
    data2 = pd.DataFrame(dict)
    return data2

