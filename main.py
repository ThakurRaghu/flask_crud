from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route('/api/users')
def get_users():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from student_t3")
    rows = cur.fetchall()
    users = []
    for row in rows:
        user = {}
        user['id'] = row[0]
        user['uname'] = row[1]
        user['email'] = row[2]
        user['contact'] = row[3]
        user['age'] = row[4]
        users.append(user)
    return jsonify(users)



@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from student_t3")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


@app.route("/add_user", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        uname = request.form['uname']
        email = request.form['email']
        contact = request.form['contact']
        age = request.form['age']
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("insert into student_t3(UNAME, EMAIL, CONTACT, AGE) values (?,?,?,?)", (uname,email,contact, age))
        con.commit()
        flash('User Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_user.html")


@app.route("/edit_user/<string:uid>", methods=['POST', 'GET'])
def edit_user(uid):
    if request.method == 'POST':
        uname = request.form['uname']
        email = request.form['email']
        contact = request.form['contact']
        age = request.form['age']
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("update student_t3 set UNAME=?, EMAIL=?,CONTACT=?, AGE=? where UID=?", (uname, email, contact, age, uid))
        con.commit()
        flash('User Updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from student_t3 where UID=?", (uid,))
    data = cur.fetchone()
    return render_template("edit_user.html", datas=data)


@app.route("/delete_user/<string:uid>", methods=['GET'])
def delete_user(uid):
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("delete from student_t3 where UID=?", (uid,))
    con.commit()
    flash('User Deleted', 'warning')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)