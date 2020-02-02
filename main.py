from flask import Flask, render_template, flash, redirect, request, url_for
from groupForm import CreateGroupForm
from initGroup import initGroup, reset, defaultGroup, triggerSMS

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
    groupName = request.args.get('groupName') if request.args.get('groupName') else "GroupName"
    if form.validate_on_submit():
        flash(f'Account created for {form.groupName.data}!')
        initGroup(form)
        return redirect(url_for('index'))
        #print(form.people.entries)
        #print(form.people.entries[0].username)
    return render_template("group.html", groupName=groupName, form=form)


@app.route("/")
@app.route("/admin/reset")
def resetroute():
    reset()
    return redirect(url_for("admin"))

@app.route("/")
@app.route("/admin/default")
def default():
    defaultGroup()
    return redirect(url_for("admin"))

@app.route("/")
@app.route("/admin/triggerSMS")
def triggerSMSroute():
    triggerSMS()
    return redirect(url_for("admin"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
