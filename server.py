from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template("./index.html")

@app.route("/<string:package_name>")
def html_page():
    return render_template("package_name")

def get_data(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['name']
        message = data['message']
        file = database.write(f'{email},{subject},{message}')


def get_csv(data):
    with open('database2.csv', mode='a') as database2:
        email = data['email']
        subject = data['name']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',  quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        get_csv(data)
        return 'thankyou!'
    else:
        return 'something_went_wrong'