from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/track', methods=['POST'])
def track():
    phone = request.form.get('phone_number')
    # Abhi ke liye dummy result return kar rahe
    result = f"Tracking info for: {phone}"
    return result

if __name__ == '__main__':
    app.run(debug=True)