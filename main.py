from flask import Flask, render_template, request, redirect, url_for
from db import getTaskList, addTask
app = Flask(__name__)

#tasklist = [["Walk Dog", True],["Wash Dishes", False],["Take out trash", True]]
tasklist=getTaskList()
@app.route("/")
def home():
    tasklist = getTaskList()
    return render_template("tasklist.html", TaskList=tasklist)

@app.route("/add", methods=['POST'])
def add():
    taskname = request.form['TaskName']
    duedate = request.form['DueDate']
    addTask(taskname,duedate)
    return redirect(url_for('home'))

app.run()