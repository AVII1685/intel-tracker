from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Phone Number Intelligence Tracker is Live!"

if __name__ == '__main__':
    app.run(debug=True)