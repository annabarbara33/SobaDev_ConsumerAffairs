
import data
from data import *
from flask import Flask, request, render_template, jsonify,redirect
import categories
from categories import *
import insert_db
from insert_db import insert_data
from insert_db import select

app = Flask(__name__)

#ls = ["FHA LOAN LENDERS","MOTORCYCLE INSURANCE","BACKGROUND CHECK COMPANIES","AUTO LOANS"]

ls = []
row  = select()
if len(row) != 0:
    for i in row:
        ls.extend(list(i))


@app.route("/")
def index():
    x = trail()
    return render_template("home.html",found = x)


@app.route("/search/<string:box>")
def process(box):
    query = request.args.get('query')
    if box == 'names':
        suggestions = [{'value': 'Travel Insurance','data': 'Travel Insurance'}, {'value': 'FHA LOAN LENDERS','data': 'FHA LOAN LENDERS'},{'value': 'SECURED CREDIT CARDS','data': 'SECURED CREDIT CARDS'},{'value': 'BACKGROUND CHECK COMPANIES','data': 'BACKGROUND CHECK COMPANIES'} ]
    return jsonify({"suggestions":suggestions})

@app.route("/result" , methods=['GET', 'POST'])
def result():
    print("helloworld")
    select = request.form.get('comp_select')
    dict= {'Travel Insurance': 'https://www.consumeraffairs.com/insurance/travel-insurance/', 'FHA LOAN LENDERS':"https://www.consumeraffairs.com/finance/fha-loans/","SECURED CREDIT CARDS":"https://www.consumeraffairs.com/finance/credit-cards/secured/","BACKGROUND CHECK COMPANIES":"https://www.consumeraffairs.com/online/background-check/"}
    insert_data(select)
    #ls.append(select)
    #print(ls)
    return redirect(dict[select])




if __name__=='__main__':
    app.run(debug=True)




'''
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

# @app.route('/', methods=['GET'])
# def my_form_post():
#     print("hello world")
#     if request.method == "GET":
#         text = request.form['text']
#         processed_text = text.upper()
#         print(processed_text)


@app.route("/search/<string:box>")
def process(box):
    query = request.args.get('query')
    if box == 'names':
        # do some stuff to open your names text file
        # do some other stuff to filter
        # put suggestions in this format...
        suggestions = [{'value': 'Travel','data': 'Travel'}, {'value': 'Shopping','data': 'Shopping'},{'value': 'Insurance','data': 'Insurance'},{'value': 'Finance','data': 'Finance'} ]
    #if box == 'songs':
        # do some stuff to open your songs text file
        # do some other stuff to filter
        # put suggestions in this format...
        #suggestions = [{'value': 'song1','data': '123'}, {'value': 'song2','data': '234'}]
    return jsonify({"suggestions":suggestions})


@app.route("/test" , methods=['GET', 'POST'])
def test():
    data = []
    error = None
    select = request.form.get('text')
    print("Anna")



    #processed_text = text.upper()
    #print(processed_text)






if __name__ == "__main__":
    app.run(debug=True)
'''


#/Users/chanukya/Documents/GitHub/SobaDev_ConsumerAffairs/ConsumerAffairs/Project1/Backend/myapp.py
#/Users/chanukya/Documents/GitHub/SobaDev_ConsumerAffairs/ConsumerAffairs/Project1/Front-End/static
