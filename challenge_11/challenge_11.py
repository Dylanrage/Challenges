#pip install pandas openpyxl
#importeren van de modules
import json
import pandas as pd
#je datafile inladen via onderstaande code
with open('./import.json') as json_file:
    data = json.load(json_file)
#maken van een dataframe om de data op te slaan 
df = pd.DataFrame(data)
#uiteindelijk de data uit het dataframe opslaan in de vorm van een excel file
df.to_excel('./export.xlsx')