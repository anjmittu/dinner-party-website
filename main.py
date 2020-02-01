from flask import Flask, render_template
from groupForm import CreateGroupForm
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/")
@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/")
@app.route("/createGroup")
def createGroup():
    groupName = "GroupName"
    return render_template("group.html", groupName=groupName)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
