from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    s = float(request.form["s"])
    k = float(request.form["k"])
    r = float(request.form["r"])
    t = float(request.form["t"])
    v = float(request.form["v"])

    # perform calculation using Binomial Tree method
    # replace this with your own calculation
    price = s * k * r * t * v

    return "The estimated price of the American-style option is {price}"

if __name__ == "__main__":
    app.run(debug=True)
