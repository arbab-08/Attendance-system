from flask import Flask, render_template, request, redirect
import sqlite3
from database import connect

app = Flask(__name__)
connect()

def get_db():
    conn = sqlite3.connect("attendance.db")
    return conn

@app.route("/")
def home():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    cur.execute("SELECT * FROM attendance")
    records = cur.fetchall()

    return render_template("index.html", students=students, records=records)

@app.route("/register", methods=["POST"])
def register():
    roll = request.form["roll"]
    name = request.form["name"]

    conn = get_db()
    cur = conn.cursor()

    cur.execute("INSERT OR IGNORE INTO students VALUES (?,?)", (roll, name))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/attendance", methods=["POST"])
def attendance():
    roll = request.form["roll"]
    status = request.form["status"]

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT name FROM students WHERE roll=?", (roll,))
    data = cur.fetchone()

    if data:
        name = data[0]
        cur.execute("INSERT INTO attendance (roll,name,status) VALUES (?,?,?)",
                    (roll, name, status))

    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)