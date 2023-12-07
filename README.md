# New-Python-Project

Dataset- Netflix Movies and TV Shows. 

Netflix is one of the most popular media and video streaming platforms. They have over 8000 movies or tv shows available on their platform, as of mid-2021, they have over 200M Subscribers globally. This tabular dataset consists of listings of all the movies and tv shows available on Netflix, along with details such as - cast, directors, ratings, release year, duration, etc.

ID (JustWatch): Unique identifiers for precision.
Title: Names of your favorite shows and movies.
Release Year: Journey through time with release year details.
Age Certification: Tailored viewing experiences for all audiences.
Runtime: Episode and movie length for binge-watching planning.
IMDb Score & Votes: Audience opinions revealed.
IMDb (Internet Movie Database): A renowned online database showcasing ratings, reviews, and information about movies, TV shows, and more.
TMDB Popularity & Score: Additional insights for informed choices.
TMDB (The Movie Database): A community-driven database offering information on movies and TV shows, enhancing your understanding of content appeal.

# netflix.py:
(python file) in which imports flask, pandas, sqlite3, pathlib.
path = pathlib.Path().cwd()    --- 
                      This code uses the pathlib module to obtain the current working directory (cwd) and assigns it to the 
                      variable path.

def create_db(db_name , filename , table_name)  --- 
                                      This function creates a database named db_name using the SQLite library, with a 
                                      specified filename for storage. It also establishes a table named table_name within 
                                      the database. 

con = sqlite3.connect('Netflix.db')
    cursor = con.cursor()   ---  
               This code establishes a connection to an SQLite database file named 'Netflix.db' using the sqlite3 module.
               It creates a cursor object (cursor) associated with the connection, which is used to execute SQL queries and 
               fetch results.

result = cursor.execute("SELECT * FROM Net_data").fetchall() ---
       This code executes a SQL query to select all rows and columns from the 'Net_data' table using the cursor's execute 
       method. The fetchall method retrieves all the results from the executed query and stores them in the variable result.

if __name__=="__main__":
    db_name = "Netflix.db"
    filename = "Netflix_dataset.csv"
    table_name = "Net_data"
     create_db(db_name, filename, table_name)   --- 
                      1. It initializes variables for the SQLite database name (db_name), CSV filename (filename), and table 
                         name (table_name).
                      2. It calls the create_db function with these parameters to create a database, using the specified 
                         filename and table name for handling Netflix dataset information.


# Netflix_html.py:

render_template -- ender_template is a function in web development frameworks like Flask that renders and returns an HTML 
                    template

netflix_html = Flask(__name__) ---
              This code initializes a Flask web application named netflix_html.
              The __name__ argument is used to determine the root path for the application.

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
    return render_template("data_table_fillin.html", Net_data = Net_data) ---

                    In this Flask application, three routes are defined: the index route is associated with the root path 
                    ("/") and renders the "index.html" template when accessed. The about route is linked to the "/about" 
                    path and renders the "about.html" template. The data route, associated with "/data," establishes a 
                    connection to an SQLite database located at File_path. Finally, the "data_table_fillin.html" template is 
                    rendered, passing the fetched Net_data as a parameter, and the resulting HTML content is sent as a 
                    response when the "/data" route is accessed.


if __name__=="__main__":
    netflix_html.run(debug = True) ---
                      This conditional statement checks if the Python script is being run directly, not imported as a 
                      module. If true, it launches the Flask web application named netflix_html in debug mode, allowing for 
                      real-time code updates and detailed error messages during development.
