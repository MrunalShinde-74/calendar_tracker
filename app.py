from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)
calendar_data = {}

@app.route('/')
def index():
    today = datetime.date.today()
    return render_template('index.html', today=today, calendar_data=calendar_data)

@app.route('/add', methods=['POST'])
def add():
    date = request.form['date']
    note = request.form['note']
    calendar_data[date] = note
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
