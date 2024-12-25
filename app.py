from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    title = "My Home Page"
    heading = "My first Heading"
    return render_template("home.html", x=title, y=heading)

@app.route("/about")
def about():
    items = ["apple", "banana", "cherry"]
    return render_template("about.html", items=items)

@app.route("/products")
def products():
    my_dict = {
        "Name": "Alice",
        "Age": 30,
        "Country": "USA",
        "Occupation": "Enginner"
    }
    return render_template("products.html", my_dict=my_dict)

@app.route("/contact")
def contact():
    return render_template("add.html")


@app.route("/submit")
def submit():
    x = request.args.get("x")
    y = request.args.get("y")
    result = int(x) + int(y)
    return f"Sum is {result}"



app.run(debug=True)