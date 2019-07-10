from flask import Flask, render_template

app=Flask("__name__")

@app.route('/')
def home():
    #return "HomePage here"
    return render_template("homepage.html")

@app.route('/about/')
def about():
    #return "AboutPage here"
    return render_template("aboutpage.html")

if __name__ == "__main__":
    app.run(debug=True)
