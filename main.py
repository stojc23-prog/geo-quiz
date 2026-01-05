# Dictionary with country:capital pairs
from flask import Flask, render_template,request
import random

app = Flask(__name__)

country_capital = {

    "Slovenia": "Ljubljana",
    "Austria": "Vienna",
    "Croatia": "Zagreb",
    "Italy": "Rome",
    "Hungary": "Budapest",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Ireland": "Dublin",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg City",
    "Malta": "Valletta",
    "Netherlands": "Amsterdam",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Slovakia": "Bratislava",
    "Spain": "Madrid",
    "Sweden": "Stockholm"
}

@app.route("/", methods=["GET","POST"])
def index():
    result = None


# Samo če uporabnik pošlje odgovor se sproži ta blok in ga sprejme.
    if request.method == "POST":
        user_answer = request.form.get("answer")
        correct_answer = request.form.get("correct_answer")

        if user_answer.strip().lower() == correct_answer.lower():
            result = "Correct!"
        else:
            result = f"Wrong, correct answer was {correct_answer}!"

    country = random.choice(list(country_capital.keys()))
    capital = country_capital[country]

    question = f"What is the capital city of {country}?"

    return render_template("index.html", question=question, correct_answer=capital, result=result)

if __name__ == "__main__":
    app.run()
