from flask import Flask , render_template
import pandas as pd
import sqlite3
import pathlib

path = pathlib.Path().cwd()

def create_db(db_name , filename , table_name):
    
    file_path = path/ filename
    
    con = sqlite3.connect('Netflix.db')
    cursor = con.cursor()
    
    Net_data = pd.read_csv('Netflix_dataset.csv') 
    Net_data.to_sql(table_name , con , index = False, if_exists="replace")
    
    result = cursor.execute("SELECT * FROM Net_data").fetchall()
    print(result)

    con.commit()
    con.close()
    

if __name__=="__main__":
    db_name = "Netflix.db"
    filename = "Netflix_dataset.csv"
    table_name = "Net_data"
    create_db(db_name, filename, table_name)