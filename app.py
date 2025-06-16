from flask import Flask, render_template, request
from modules.truecaller_scraper import search_truecaller

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    number = request.form['phone']
    truecaller_result = search_truecaller(number)

    return render_template('result.html', number=number, truecaller=truecaller_result)

if __name__ == '__main__':
    app.run(debug=True)