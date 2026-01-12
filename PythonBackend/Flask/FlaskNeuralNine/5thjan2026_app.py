from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
  return '<h1 style="background-color: red;">hello moktan</h1>'

@app.route("/home",methods=['POST','GET','PUT']) # methods specify what the route does 
# /endpoint is used to invoke this function in the website 
# its like going to a different webpage after enterign /endpoint in the url
def hello():
  if request.method == "GET":
    return "You made a GET request......"
  elif request.method == "POST":
    return "You made a POST request....."
  elif request.method == "PUT":
    return "You made a PUT request....."
  else:
    return "Jackass!!! You will never see this message....."

@app.route("/greet/<name>")
def greet(name):
  return f"hello {name}"

@app.route("/add/<int:num1>/<int:num2>") #declarign the type of numbers
def add(num1,num2): 
  return f"The sum of {num1} & {num2} is: {num1+num2}"

@app.route("/params")
def handle_parms():
  if "greeting" in request.args.keys() and "name" in request.args.keys():
    greeting = request.args.get("greeting")
    name = request.args.get("name")
    return f"{greeting}, Welcome {name} to our webpage or api..."
  else: 
    return "Some parameters are missing..."

if __name__ == '__main__':
  app.run(host= "0.0.0.0",port= 5555,debug= True)