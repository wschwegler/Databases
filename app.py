from flask import Flask, request, render_template, redirect, url_for
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
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("index.html", tables=[table[0] for table in tables])

@app.route('/insert', methods=['POST'])
def insert():
    sql_query = request.form['sql_query']
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        conn.commit()
        message = "Query executed successfully!"
    except Exception as e:
        message = f"Error: {e}"
    finally:
        cursor.close()
        conn.close()
    
    return redirect(url_for('index', message=message))

if __name__ == '__main__':
    app.run(debug=True)