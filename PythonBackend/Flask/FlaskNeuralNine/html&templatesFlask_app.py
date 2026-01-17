from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
  ran_value = "My name is Sagar Moktan......"
  ran_result = 45 + 555
  return render_template('index.html', mval= ran_value, mre= ran_result)

if __name__ == "__main__":
  app.run(host= '0.0.0.0',port= 777, debug= True)
