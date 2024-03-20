 
from flask import Flask, render_template, request
import sys, os
from packages.gsheet import GSheet

template_folder = os.path.join(os.path.dirname(__file__), "templates")
app = Flask(__name__, template_folder=template_folder)
 
import pandas

@app.route('/')
def home():
  print("Get request string")
  return render_template("index.html")


@app.route('/', methods = ['POST'])
def home_post():
  dim1 = request.form['first_dim']
  dim2 = request.form['second_dim']
  dim3 = request.form['third_dim']
  volume = float(dim1) * float(dim2) * float(dim3)
  print("Get post request")
  return render_template("index.html", output=volume, dim_1=dim1, dim_2=dim2, dim_3=dim3)

class BaseService:
    def __init__(self):
        app.run('localhost', 8080)
        import pandas

        url_sheet1 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"
        url_sheet2 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2014"
        data1 = pandas.read_csv(url_sheet1)
        data2 = pandas.read_csv(url_sheet2)

        print(data1)
        print(data2)
 
 
