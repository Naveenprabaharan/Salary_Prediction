from flask import Flask, render_template, request
import model as m

app = Flask(__name__)

@app.route("/" , methods = ["POST"])
def hello():
    if request.method == "POST":
        hrs = request.form['expyr']
        salary_pred = m.salaryPrediction(hrs)
        mk = salary_pred
        

    return render_template("index.html", my_sal = mk)
    


@app.route("/") 
def submit():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)


"""
@app.route("/sub", methods = ["POST"])
def submit():
    # HTML -> .py
    if request.method == "POST":
        name = request.form['username']

    # .py -> HTML
    return render_template("sub.html", n = name)
"""
