from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="comp373.cianci.io",
        user="schwegler",
        password="half-practical-contrast",
        database="comp373"
    )

@app.route('/')
def index():
    # Connect to the database
    conn = get_db_connection()
    
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
    # Query to get the names of all tables in the database
    cursor.execute("SHOW TABLES")
    
    # Fetch all the table names
    tables = cursor.fetchall()
    
    # Close the cursor and the connection
    cursor.close()
    conn.close()
    
    # Format the table names into a string to display on the webpage
    table_names = "<br>".join([table[0] for table in tables])
    
    # Return the names of the tables as the response
    return f"<h1>Tables in Database:</h1><p>{table_names}</p>"

if __name__ == '__main__':
    app.run(debug=True)
