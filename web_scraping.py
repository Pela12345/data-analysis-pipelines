import requests 
from bs4 import BeautifulSoup
import api


def get_webscraping(data2, web_link):
    # llamo a la web de la que quiero informacion
    res = requests.get(web_link)
    soup = BeautifulSoup(res.text, features="html.parser")
    # selecciono las fechas que me faltan (año 1970) que no estaban accesibles en la API
    wanted = soup.select('div.col-xs-6 tbody tr')
    value1=wanted[47].text[6:10]
    year1=wanted[47].text[1:5]
    dict1={
        "Year":year1,
        "Growth Rate":float(value1)
    
    }
    # Uno el dato sacado del webscrapping al data frame que cree con la API, los junto en un nuevo dataframe
    data2_final = data2.append(dict1, ignore_index=True)
    data2_final=data2_final.sort_values(by=['Year'])
    data2_final["Year"] = data2_final["Year"].astype('int64')
    return data2_final

   