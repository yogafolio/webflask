from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about-us")
def about_us():
    return render_template("about-us.html")


@app.route("/portofolio")
def portofolio():
    return render_template("portofolio.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")


@app.route("/contact-us")
def contact_us():
    return render_template("contact-us.html")


if __name__ == '__main___':
    app.run(debug=True)
