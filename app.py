from flask import Flask, render_template, request, url_for, redirect

from the_age_app import the_age_app


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/app_the_age", methods=["GET", "POST"])
def app_the_age():
    if request.method == "POST":
        age_app_name = request.form['age_app_name']
        age_app_age = int(request.form['age_app_age'])
        ansver = the_age_app(age_app_name, age_app_age)

        return render_template('apps/app_the_age/app_the_age.html', age_app_name=age_app_name, age_app_age=age_app_age, ansver=ansver)

    else:
        return render_template('apps/app_the_age/app_the_age.html')


if __name__ == '__main__':
    app.run(debug=True)
