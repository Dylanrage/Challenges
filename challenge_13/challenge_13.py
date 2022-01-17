import xlrd   # library to manage excel spreadsheets
import json   # library to manage JSON classes and functions
import pandas as pd   #pip install pandas openpyxl

#je datafile inladen via onderstaande code
with open('./groups_struc.json') as json_file:
    data = json.load(json_file)
#maken van een dataframe om de data op te slaan 
df = pd.DataFrame(data)
#uiteindelijk de data uit het dataframe opslaan in de vorm van een excel file
df.to_excel('./webex_groups.xlsx')

wb = xlrd.open_workbook("webex_groups.xlsx")
sheet = wb.sheet_by_index(0)  # read data from the first tab

member_dict["group"]        = sheet.cell_value(1, 0) 
member_dict["person_name"]  = sheet.cell_value(1, 1)
member_dict["email"]        = sheet.cell_value(1, 2)

def find_all_persons_and_groups(xlf):
    wb = xlrd.open_workbook(xlf)
    sheet = wb.sheet_by_index(0)
    number_rows = sheet.nrows
    member_list = []
    for r in range(number_rows):
        if r > 0: ### first row contains column names
            member_dict["group"]        = sheet.cell_value(r, 0) 
            member_dict["person_name"]  = sheet.cell_value(r, 1)
            member_dict["email"]        = sheet.cell_value(r, 2)
            member_list.append(member_dict.copy())     
    return member_list