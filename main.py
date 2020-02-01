from flask import Flask, render_template
from groupForm import CreateGroupForm
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

"""
@app.route("/")
def index():
    form = CreateGroupForm()
    return render_template(".html", title="Create Group", form=form)
"""
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="80")