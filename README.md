# Group 13 - Python Project: Python Media Catalog

## Project Description:

This project focuses on storing Netflix data in a database and serving that data via a website. By executing the `Netflix_App.py` script, users can access the website to explore and interact with the Netflix dataset.

## Usage Guidelines:

1. Execute `Netflix_App.py` to obtain the website link.
2. Open the provided link to access the index page of the website.

## Code Samples:

### `Netflix_App.py`

```python
from flask import Flask, render_template
import sqlite3
import pathlib

netflix_html = Flask(__name__)

base_path = pathlib.Path().cwd()
db_name = "Netflix.db"
File_path = base_path / db_name

@netflix_html.route("/")
def index():
    return render_template("index.html")

@netflix_html.route("/about")
def about():
    return render_template("about.html")

@netflix_html.route("/data")
def data():
    con = sqlite3.connect(File_path)
    cursor = con.cursor()
    Net_data = cursor.execute("SELECT * FROM Net_data").fetchall()
    con.close()
    return render_template("data_table_fillin.html", Net_data=Net_data)

if __name__ == "__main__":
    netflix_html.run(debug=True)
```

## File Structure:

```
Main Folder: New-Python-Project
    - Netflix.db - Database file
    - Netflix_App.py
    - Netflix_dataset.csv
    - Netflix_file.ipynb
    - README.md
    - templates (subfolder)
        - index.html - HTML file for the index page
        - about.html - HTML file for the About page
        - data_table_fillin.html - HTML file for the Netflix data
```

## Contributors:

- Semini Sehara Amarasinghe
- Ramandeep Kaur Mehra
- Shivam Sharma
