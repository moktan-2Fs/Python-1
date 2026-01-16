from flask import Flask, request
app = Flask(__name__)


@app.route("/home")
def home(*args):
    there = request.args.get("where")
    this = request.args.get("distance")
    if "where" in request.args and "distance" in request.args:
        return f"Your home is {there} and it's {this} far...."
    elif "where" in request.args:
        return f"Your home is in {there} and you didn't provide me the distance from Kathmandu to {there}"
    else:
        return "This is a practice Flask app...."


@app.route("/login/<name>/<int:id>")
def login(name, id):
    # if "name" in request.args and "id" in request.args:
    return f"Your name is {name}.\nYour id is {id}."


if __name__ == '__main__':
    app.run(debug=True)
