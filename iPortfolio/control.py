from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/Hacienda_de_Dorado')
def hacienda_de_Dorado():
    return render_template('Casa_Juan_details.html')

@app.route('/Villa_Torens_Luquillo')
def Villa_Torrens_Luquillo():
    return render_template('Casa_Campo_details.html')

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)