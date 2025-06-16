from flask import Flask, render_template, request
from modules.truecaller_scraper import search_truecaller
from modules.google_dork_links import generate_google_dorks
from modules.phoneinfoga_runner import run_phoneinfoga  # ✅ NEW

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    phone_number = request.form['phone_number']

    truecaller_result = search_truecaller(phone_number)
    google_dorks = generate_google_dorks(phone_number)
    phoneinfoga_output = run_phoneinfoga(phone_number)  # ✅ NEW

    return render_template('result.html',
                           phone_number=phone_number,
                           truecaller_result=truecaller_result,
                           google_dorks=google_dorks,
                           phoneinfoga_output=phoneinfoga_output)  # ✅ NEW

if __name__ == '__main__':
    app.run(debug=True)