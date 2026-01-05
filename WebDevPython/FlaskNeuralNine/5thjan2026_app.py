from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return '<h1 style="background-color: red;">hello moktan</h1>'

@app.route("/endpoint")
# /endpoint is used to invoke this function in the website 
# its like going to a different webpage after enterign /endpoint in the url
def hello():
  return "Hello Sagor Tomang!!!!"

@app.route("/greet/<name>")
def greet(name):
  return f"hello {name}"

@app.route("/add/<int:num1>/<int:num2>") #declarign the type of numbers
def add(num1,num2): 
  return f"The sum of {num1} & {num2} is: {num1+num2}"


if __name__ == '__main__':
  app.run(host= "0.0.0.0",debug= True)