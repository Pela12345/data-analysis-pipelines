import pandas as pd
import json
import re
import matplotlib
import seaborn as sns
import numpy as np
import requests
from reportlab.pdfgen import canvas
from matplotlib import pyplot as plt
import sys

import loading
import wrangling 
import analysis
import api
import web_scraping
import visualize
import pdf

# creo un titulo para el nombre de la imagen guardada
heading = "Terrorist-Attacks-in-the-USA"

# doy a elegir como quieren los datos
variable = str(input("Enter by which variable you want to see the data ('Year' or 'Growth Rate'): "))

def read_file(file):
    data = loading.load_data(file)
    return data

def cleaning(data):
    data = wrangling.selecting_columns(data)
    data = wrangling.filling_nulls(data)
    data = wrangling.renaming_columns(data)
    data = wrangling.correct_type(data, 'Year')
    return data

def use_api(api_url):
    data2 = api.get_api(api_url)
    return data2

def use_webscraping(data2, web_link):
    data2_final = web_scraping.get_webscraping(data2, web_link)
    return data2_final

def analysing(data, data2_final):
    data2_final = analysis.binning(data2_final)
    data = analysis.filter_rows(data, 'Country', 'United States')
    data = analysis.create_column(data, 'Casualties', 'Killed', 'Wounded')
    dataX = analysis.count_attacks(data)
    data_merged = analysis.merge_data(dataX, data2_final, 'Year')
    data_merged = analysis.drop_unused(data_merged, 'Killed', 'Wounded')
    return data_merged

def visualising(data_merged, variable, heading):
    gplot = visualize.growth_plot(data_merged, variable, heading)
    return gplot

def generating_pdf():
    pdf.generate_pdf()

# uso el main para correr el codigo, aparte del pdf imprimo los datos en consola con stdout por si lo prefieren ver asi
def main():
    d = read_file("globalterrorismdb_0718dist1.csv")
    d_cleaned = cleaning(d)
    d2 = use_api("https://stats.oecd.org/SDMX-JSON/data/SNA_TABLE1/USA.B1_GE.G/all?startTime=1970&endTime=2017&dimensionAtObservation=allDimensions")
    d3 = use_webscraping(d2,"https://www.macrotrends.net/countries/USA/united-states/gdp-growth-rate")
    d4 = analysing(d_cleaned, d3)
    d5 = visualising(d4, variable, heading)
    sys.stdout.write(str(d5))
    generating_pdf()


if __name__ == "__main__":
    main()
