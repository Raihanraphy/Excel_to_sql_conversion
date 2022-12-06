import os
import PySimpleGUI as sg
import pandas as pd 
from sqlalchemy import create_engine

sqlEngine = create_engine(f'mysql+pymysql://root:@localhost/DBname', pool_recycle=3600)

dbConnection    = sqlEngine.connect()
print("connected")
#!cur=mydb.cursor()
working_directory = os.getcwd()
layout = [  
            [sg.Text("Choose an xlsx file:")],
            [sg.InputText(key="-FILE_PATH-"), 
            sg.FileBrowse(initial_folder=working_directory, file_types=[("xlsx file", "*.xlsx")])],
            [sg.Button('Submit'), sg.Exit()]
        ]

window = sg.Window("Excel Reader", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Submit":
        csv_address = values["-FILE_PATH-"]
        df=pd.read_excel(csv_address)
        df.to_sql('Table_name', dbConnection, index=False)
window.close()