from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def hello_world():
    return render_template("index.html")

# Dynamically generate pages 
@app.route("/<string:page_name>")
def html_page(page_name=None):
    return render_template(page_name)

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

# @app.route("/works.html")
# def work():
#     return render_template("works.html")

# @app.route("/thankyou.html")
# def thankyou(data=None):
#     return render_template("thankyou.html", name=data)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database1:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankyou.html") #thankyou(data)
    else:
        return "Something went wrong, Try again!"