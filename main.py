from flask import Flask, render_template, request, redirect, url_for, session
import os, sqlite3
from datetime import timedelta

app = Flask(__name__)

#cookie session 亂數金鑰
app.config['SECRET_KEY'] = os.urandom(24)
#如果設置了 session.permanent 為 True，那麽過期時間是31天
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

db_name = 'taeyeon.db'

#最初畫面~登入系統
@app.route('/index', methods = ['GET', 'POST'])
def index():
    meg = ''
    if 'message' in session:
        meg = session.get('message')
    return render_template("index.html", meg=meg)
@app.route('/login', methods = ['GET', 'POST'])
def login():
    account = request.form['account']
    password = request.form['password']

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT id FROM `user` where `account` = '{}' and `password` = '{}'".format(account, password)
        cursor.execute(sql)

        row = cursor.fetchone()
        if row == None:
            session['message'] = '登入失敗'
            session.permanent = True
            return redirect('/index')
        else:
        #把user_id 用 session傳送 
            session['id'] = row[0]
            session.permanent = True  
            return redirect('/part')
#k
@app.route('/part', methods = ['GET', 'POST'])
def part():
    id = session.get('id')

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT project.id, project.name FROM `project`, `member` where member.project_id = project.id and member.user_id = {}".format(id)
        cursor.execute(sql)

        from html_list import Part_list as Part_list
        html_list = Part_list()    
        for row in cursor.fetchall():
            html_list.add(row[0], row[1])
    return render_template("part.html", html_list=html_list)
    
#user
@app.route('/user' ,methods = ['GET', 'POST'])
def user():
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT name, account, id FROM `user`"
        cursor.execute(sql)

        from html_list import User_list as User_list
        html_list = User_list()    
        for row in cursor.fetchall():
            html_list.add(row[0], row[1], row[2])

    return render_template("user.html", html_list=html_list)  
#k
@app.route('/add' ,methods = ['GET', 'POST'])
def add():
    return render_template("add.html")   
#k
@app.route('/update' ,methods = ['GET', 'POST'])
def update():
    id = request.values.get("id")
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT name, password, id FROM `user` WHERE `id` = {}".format(id)
        cursor.execute(sql)

        row = cursor.fetchone()
    return render_template("update.html", name=row[0], password=row[1], id=row[2])   
#db_user
@app.route('/db_add' ,methods = ['GET', 'POST'])
def db_add():
    name = request.form["name"]
    account = request.form["account"]
    password = request.form["password"]
    
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "INSERT INTO `user`(`id`,`name`,`account`,`password`,`type`) VALUES (NULL, '{}', '{}', '{}', '2')".format(name, account, password)
        cursor.execute(sql)
    return redirect('/user')
#k
@app.route('/db_del' ,methods = ['GET', 'POST'])
def db_del():
    id = request.values.get["id"]
    
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "DELETE FROM `user` WHERE `id` = {}".format(id)
        cursor.execute(sql)
    return redirect('/user')
#k
@app.route('/db_update' ,methods = ['GET', 'POST'])
def db_update():
    name = request.form["name"]
    password = request.form["password"]
    id = request.form["id"]
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()   
        sql = "UPDATE `user` SET `name` = '{}', `password`= '{}' WHERE `id` = {}".format(name, password, id)
        cursor.execute(sql)
    return redirect('/user')

#proj
@app.route('/proj' ,methods = ['GET', 'POST'])
def proj():
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT name, id FROM `project`"
        cursor.execute(sql)

        from html_list import Proj_list as Proj_list
        html_list = Proj_list()    
        for row in cursor.fetchall():
            html_list.add(row[0], row[1])
    return render_template('proj.html', html_list=html_list)
#ajax
@app.route('/proj_add' ,methods = ['GET', 'POST'])
def proj_add():
    return render_template("proj_add.html")  
#k
@app.route('/proj_add_user' ,methods = ['GET', 'POST'])
def proj_add_user():
    id = request.values.get("id")

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT id, name FROM `user` WHERE `id` != '1'"
        cursor.execute(sql)

        from html_list import Proj_add_user as Proj_add_user
        from html_list import Proj_add_user1 as Proj_add_user1
        html_list = Proj_add_user()    
        html_list1 = Proj_add_user1()
        for row in cursor.fetchall:
            html_list.add(row[0], row[1])
            html_list1.add(row[0], row[1])
    return render_template("proj_add_user.html", html_list=html_list, html_list1=html_list1, id=id)    
#ajax
@app.route('/proj_update' ,methods = ['GET', 'POST'])
def proj_update():
    id = request.values.get("id")
 
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
    #proj
        sql = "SELECT name, description, id FROM `project` WHERE `id` = {}".format(id)
        cursor.execute(sql)
        row = cursor.fetchone()
    #direction
        sql = "SELECT name, description, id FROM `direction` WHERE `direction_id` = {}".format(id)
        cursor.execute(sql)
        from html_list import Proj_update as Proj_update
        html_list = Proj_update()
        for i in cursor.fetchall:
            html_list.add(i)
    return render_template("proj_update.html", name=row[0], description=row[1], id=row[2], html_list=html_list)   
#db
#k


#db_proj
@app.route('/db_proj_del' ,methods = ['GET', 'POST'])
def db_proj_del():
    id = request.values.get("id")
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "DELETE FROM `project` WHERE `id` = '{}'".format(id)
        cursor.execute(sql)
        sql = "DELETE FROM `direction` WHERE `direction_id`= '{}'".format(id)
        cursor.execute(sql)
    return redirect('/proj')
#ajax
@app.route('/db_proj_add' ,methods = ['GET', 'POST'])
def db_proj_add():
    name = request.form["name"]
    description= request.form["description"]

    direction_name = request.form['direction_name']
    direction_description = request.form['direction_description']
    direction_id = request.form['direction_id']
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "INSERT INTO `project`(`id`,`name`,`description`) VALUES (NULL, {}, {})".format(name, description)
        cursor.execute(sql)
        id = int(cursor.lastrowid)
        sql = "INSERT INTO `member`(`id`,`project_id`,`user_id`,`type`) VALUES (NULL, {}, '1', '1')".format(id)
        cursor.execute(sql)
        for i in direction_id:
            sql = "INSERT INTO `direction` (`id`,`direction_id`, `name`, `description`) \
                VALUES (NULL,'id' , '{}', '{}')".format(direction_name[i], direction_description[i])
            cursor.execute(sql)
    return redirect('/proj')

@app.route('/db_proj_update' ,methods = ['GET', 'POST'])
def db_proj_update():
    name = request.form["name"]
    description = request.form["description"]
    id = request.form["id"]
    direction_name = request.form['direction_name']
    direction_description = request.form['direction_description']
    direction_id = request.form['direction_id']
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "DELETE FROM `direction` WHERE `direction_id`='{}'".format(id)
        cursor.execute(sql)
        sql = "UPDATE `project` SET `name` = '{}',`description`='{}' WHERE `id` = '{}'".format(name, description, id)
        cursor.execute(sql)
        for i in direction_id:
            sql = "INSERT INTO `direction` (`id`,`direction_id`, `name`, `description`) \
                VALUES (NULL,'id' , '{}', '{}')".format(direction_name[i], direction_description[i])
            cursor.execute(sql)
    return redirect('/proj')
@app.route('/db_proj_add_user' ,methods = ['GET', 'POST'])
def db_proj_add_user():
    leader = request.form["leader"]
    member = request.form["member"]
    id = request.form["id"]

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "DELETE FROM `member` WHERE project_id = 'id "
        cursor.execute(sql)
        sql = "INSERT INTO `member`(`id`,`project_id`,`user_id`,`type`) VALUES (NULL, {}, '1', '1')".format(id)
        cursor.execute(sql)
        sql = "INSERT INTO `member`(`id`,`project_id`,`user_id`,`type`) VALUES (NULL, {}, '{}', '1')".format(id, leader)
        cursor.execute(sql)
        for val in member:
            sql = ("INSERT INTO `member`(`id`,`project_id`,`user_id`,`type`) VALUES (NULL, {}, '{}', '2')").format(id, val)
            cursor.execute(sql)
    return redirect('/proj')

#opinion
@app.route('/opinion' ,methods = ['GET', 'POST'])
def opinion():
    with sqlite3.connect(db_name) as conn:
        from html_list import Opinion_list as Opinion_list
        html_list = Opinion_list()

        cursor = conn.cursor()   
        sql = "SELECT user_id FROM `opinion`"
        cursor.execute(sql)
        
        for row in cursor.fetchall:
            sql = "SELECT name FROM `user` WHERE `id` = {}".format(row[0])
            cursor.execute(sql)
            user_name = cursor.fetchone[0]
            html_list.add(row[1], row[2], row[3], row[4], user_name, row[5], row[6])
    return render_template('opinion.html', html_list=html_list)
@app.route('/db_opinion' ,methods = ['GET', 'POST'])
def db_opinion():
    return redirect('/opinion')
@app.route('/db_opinion_add' ,methods = ['GET', 'POST'])
def db_opinion_add():
    return redirect('/opinion')

@app.route('/stat' ,methods = ['GET', 'POST'])
def stat():
    return 0

if __name__ == "__main__":
    app.run(host='localhost', port=10723, debug=True)
#return render_template(".html",username=request.values.get("Username"))      
#name = request.form['name']