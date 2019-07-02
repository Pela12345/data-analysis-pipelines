import requests 
from bs4 import BeautifulSoup
import api

def get_webscraping(data2, web_link):
    res = requests.get(web_link)
    soup = BeautifulSoup(res.text, features="html.parser")
    wanted = soup.select('div.col-xs-6 tbody tr')
    value1=wanted[47].text[6:10]
    year1=wanted[47].text[1:5]
    dict1={
        "Year":year1,
        "Growth Rate":float(value1)
    
    }
    data2_final = data2.append(dict1, ignore_index=True)
    data2_final=data2_final.sort_values(by=['Year'])
    data2_final["Year"] = data2_final["Year"].astype('int64')
    return data2_final

   