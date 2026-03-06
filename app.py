from flask import Flask, render_template, request
from src.summarizer_model import summarize_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/summarize', methods=['POST'])
def summarize():

    text = request.form['text']

    summary = summarize_text(text)

    return render_template(
        "index.html",
        original=text,
        summary=summary
    )

if __name__ == "__main__":
    app.run(debug=True)