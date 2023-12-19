# app.py
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display_table():
    # Read the CSV file
    data = pd.read_csv('report2.csv')

    # Convert DataFrame to HTML table
    table_html = data.to_html(classes='table table-striped', index=False)

    return render_template('index.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
