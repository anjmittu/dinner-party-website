from flask import Flask, render_template, flash, redirect
from groupForm import CreateGroupForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b3cb272ad35cbeb8f11b88974fd34ba0'

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/")
@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/")
@app.route("/createGroup", methods=['GET', 'POST'])
def createGroup():
    form = CreateGroupForm()
    groupName = "GroupName"
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template("group.html", groupName=groupName, form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
