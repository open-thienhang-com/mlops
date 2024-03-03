 
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
@app.route('/hello')
def hello():
   # Render the page
   return "Hello Python!"

class BaseService:
    def __init__(self):
        app.run('localhost', 8080)
 
 
