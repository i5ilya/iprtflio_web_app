from operator import methodcaller
from flask import Flask, render_template, request, url_for, redirect

from the_age_app import the_age_app
from ideal_weght import ideal_weght

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


@app.route("/app_ideal_weght", methods=["GET", "POST"])
def app_ideal_weght():
    if request.method == "POST":
        jsonData = request.get_json()
        #print(jsonData)
        user_height = jsonData['user_height']
        user_hand = jsonData['user_hand']
        user_age = jsonData['user_age']
        user_sex = jsonData['user_sex']
        
        return {
            'response' : ideal_weght(user_height, user_sex, user_hand, user_age)
        }
    else:
        return render_template('apps/app_ideal_weght/app_ideal_weght.html')




@app.route("/app_test", methods=["GET", "POST"])
def app_test():
    if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        pythonsay = jsonData['name'] *2
        some_my_text = 'I am some text answer'

        return {
            'response' : some_my_text,
            'answer' : pythonsay
        }
        
    else:
        user = {'firstname': 'Harry', 'lastname': 'Potter'}
        return render_template("apps/app_test/test.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)
