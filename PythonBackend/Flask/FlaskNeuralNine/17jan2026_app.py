from flask import Flask,request, make_response

app = Flask(__name__) 

@app.route("/login", methods= ["GET","POST","DELETE"])
def login():
  response = make_response("hello\nWorld\nThis is Sagar Moktan from Nepal.....")
  response.status_code = 234
  response.headers['content-type'] = "text-plain"
  if "False" in request.args:
    return "Sorry brotheer..",404
  if "True" in request.args:
    return response

if __name__ == "__main__":
  app.run(debug= True,port= 7777)

