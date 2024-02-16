# Author: Sachi and Gunveen
# Date: 16 February, 2024
# Description: School website developed with Python, Flask, HTML, CSS, and JavaScript, featuring SQLite3 backend for a seamless user experience.

from flask import Flask, render_template
from flask import Flask, render_template, send_file
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/notices')
def notices():
    return render_template('notices.html')

@app.route('/englishnotice')
def englishnotices():
    return render_template('englishnotice.html')

@app.route('/gujnotice')
def gujnotice():
    return render_template('gujnotice.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/englishfaculty')
def englishfaculty():
    return render_template('englishfaculty.html')

@app.route('/gujratifaculty')
def gujratifaculty():
    return render_template('gujratifaculty.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/event-details')
def eventdetails():
    return render_template('event-details.html')

@app.route('/campus')
def campus():
    return render_template('campus.html')

@app.route('/admission')
def admission():
    return render_template('admission.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download_timetable')
def download_timetable():
    try:
        conn = sqlite3.connect('database1.db')  # Replace 'database1.db' with your actual SQLite database filename
        cursor = conn.cursor()
        
        # Debugging: Print the list of tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables in the database:", tables)
        
        cursor.execute("SELECT * FROM timetable1")
        data = cursor.fetchall()
        
        # Create timetable1.csv file
        with open('timetable1.csv', 'w') as f:
            for row in data:
                f.write(','.join(map(str, row)) + '\n')
        
        conn.close()
        
        return send_file('timetable1.csv', as_attachment=True)
    
    except Exception as e:
        return str(e)

@app.route('/download_article')
def download_article():
    try:
        conn = sqlite3.connect('database1.db')  # Replace 'database1.db' with your actual SQLite database filename
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM events")
        data = cursor.fetchall()
        
        # Create events1.docx file
        with open('events1.docx', 'wb') as f:
            for row in data:
                f.write(row[0])  # Assuming the blob data is in the first column
                
        conn.close()
        
        return send_file('events1.docx', as_attachment=True)
    
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
