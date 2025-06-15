from flask import Flask, render_template, request
from modules.truecaller_scraper import search_truecaller
from modules.phoneinfoga_runner import run_phoneinfoga
from modules.google_dork_links import google_dork_links
from modules.hunter_checker import search_hunter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        company_domain = request.form.get('company_domain')

        result['truecaller'] = search_truecaller(phone_number)
        result['phoneinfoga'] = run_phoneinfoga(phone_number)
        result['google_dorks'] = google_dork_links(phone_number)
        
        if company_domain:
            result['hunter'] = search_hunter(company_domain)
        else:
            result['hunter'] = "No domain provided for Hunter.io"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)