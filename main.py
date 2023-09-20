from flask import Flask, render_template

app = Flask(__name__)

taskList = [["Walk Dog", True],["Wash Dishes", False],["Take out trash", True]]
@app.route("/")
def home():
    return render_template("tasklist.html", TaskList=taskList)


app.run()