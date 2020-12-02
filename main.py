from flask import Flask, render_template, request, redirect
from datetime import timedelta
import os

app = Flask(__name__)

#cookie session 亂數金鑰
app.config['SECRET_KEY'] = os.urandom(24)
#如果設置了 session.permanent 為 True，那麽過期時間是31天
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

db_name = 'taeyeon'

#WTF
class SetForm(FlaskForm):
    
	year = SelectField('Year', choices = [(i,i) for i in range(1950,2021)] , validators = [DataRequired()])
	mon = SelectField('Mon', choices = [(i,i) for i in range(1,13)] , validators = [DataRequired()])
	day = SelectField('Day', choices = [(i,i) for i in range(1,32)] , validators = [DataRequired()])
	submit = SubmitField('Submit')


@app.route('/index')
def index():
    return render_template("index.html")

#最初畫面~登入系統
@app.route('/login')
def login():
    account = request.form['account']
    password = request.form['password']

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT user.id FROM `user` where `account` = {{account}} and `password` = {{password}}"
        cursor.execute(sql)

        row = cursor.fetchone()
        if row == None:
            session['message'] = '登入失敗'
            session.permanent = True
            return redirect('/index')
        else:
        #把user_id 用 session傳送 
            session['message'] = row[0]
            session.permanent = True  
            return redirect('/part')

#sql還沒做好        
@app.route('/part')
def part():
    id = session.get('user_id')

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT project.id, project.name FROM `project`, `member` where member.project_id = project.id and member.user_id = {{id}}"
        cursor.execute(sql)

        from html_list import Part_Click as Part_Click
        html_list = Part_Click()    
        for row in cursor.fetchall():
            html_list.add(row[0], row[1])
    return render_template("part.html", html_list=html_list.get_word())

@app.route('/user' ,methods = ['GET', 'POST'])
def user():
    
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT name, account, id FROM `user`"
        cursor.execute(sql)

        from html_list import User_Click as User_Click
        html_list = User_Click()    
        for row in cursor.fetchall():
            html_list.add(row[0], row[1], row[2])

    return render_template("user.html", html_list=html_list.get_word())
@app.route('/add' ,methods = ['GET', 'POST'])
def add():
    return render_template("add.html")   

@app.route('/update' ,methods = ['GET', 'POST'])
def update():
    id = request.values.get("id")
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "SELECT name, password, id FROM `user` WHERE `id` = id"
        cursor.execute(sql)

        row = cursor.fetchone()
    return render_template("update.html", name=row[0], password=row[1], id=row[2])   

#db
@app.route('/db_add' ,methods = ['GET', 'POST'])
def db_add():
    name = request.form["name"]
    account = request.form["account"]
    password = request.form["password"]
    
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "INSERT INTO `user`(`id`,`name`,`account`,`password`,`type`) VALUES (NULL, name, account, password, '2')"
        cursor.execute(sql)
    return render_template('/user')

@app.route('/db_del' ,methods = ['GET', 'POST'])
def db_del():
    id = request.form["id"]
    
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        sql = "DELETE FROM `user` WHERE `id` = id"
        cursor.execute(sql)
    return render_template('/user')
@app.route('/db_update' ,methods = ['GET', 'POST'])
def db_update():
    name = request.form["name"]
    password = request.form["password"]
    id = request.form["id"]
    sql = "UPDATE `user` SET `name` = name, `password`= password WHERE `id` = id"
    cursor.execute(sql)
    return render_template('/user')
#db_proj
@app.route('/db_proj_add' ,methods = ['GET', 'POST'])
def db_proj_add():
    name = request.form["name"]
    description= request["description"]

    direction_name = request['direction_name']
    direction_description = request['direction_description']
    direction_id = request['direction_id']

    sql = "INSERT INTO `project`(`id`,`name`,`description`) VALUES (NULL, name, description)"
    id = int(cursor.lastrowid)
    sql = "INSERT INTO `member`(`id`,`project_id`,`user_id`,`type`) VALUES (NULL, id,'1','1')"

    foreach ($direction_id as $k=>$aaaa){
        $res= sql_query("INSERT INTO `direction` (`id`,`direction_id`, `name`, `description`) VALUES (NULL,'$id' , '{$direction_name[$k]}', '{$direction_description[$k]}')");
    }

    return render_template('/project')
@app.route('/db_proj_del' ,methods = ['GET', 'POST'])
def db_proj_del():
    return render_template('/user')
@app.route('/db_proj_update' ,methods = ['GET', 'POST'])
def db_proj_update():
    return render_template('/user')
@app.route('/db_proj_add_user' ,methods = ['GET', 'POST'])
def db_proj_add_user():
    return render_template('/user')
#db_opinion
@app.route('/db_opinion' ,methods = ['GET', 'POST'])
def db_opinion():

@app.route('/db_opinion_add' ,methods = ['GET', 'POST'])
def db_opinion_add():


@app.route('/stat' ,methods = ['GET', 'POST'])
def stat():
 
#return render_template(".html",username=request.values.get("Username"))      
#name = request.form['name']