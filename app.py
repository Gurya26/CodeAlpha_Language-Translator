from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    original_text = ""
    selected_lang = "hi"

    if request.method == "POST":
        original_text = request.form["text"]
        selected_lang = request.form["language"]

        translated_text = GoogleTranslator(
            source='auto',
            target=selected_lang
        ).translate(original_text)

    return render_template(
        "index.html",
        translated_text=translated_text,
        original_text=original_text,
        selected_lang=selected_lang
    )

if __name__ == "__main__":
    app.run(debug=True)