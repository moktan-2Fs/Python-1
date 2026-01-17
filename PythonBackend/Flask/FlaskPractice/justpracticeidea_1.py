from flask import Flask,request 
app = Flask(__name__)
@app.route("/name")
def ret_data():
    data = {"Fname": "Sagar ",
            "Lname": 'Moktan',
            "age": 22,
            "Academics": 'Undergraduate'}
    if "Sagar" in request.args and "moktan@123" in request.args:
        return data
    else:
        return f"404 Error!!!!! \nPlease enter your password too in the URL......"
if __name__ == '__main__':
    app.run(debug=True)
