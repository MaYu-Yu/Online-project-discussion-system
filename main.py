from flask import Flask, render_template, request, redirect

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
        sql = "SELECT * FROM `user` where `account` = '$account' and `password` = '$password'"
        cursor.execute(sql)

        row = cursor.fetchone()
        if row == None:
            session['message'] = '登入失敗'
            return redirect('/index')
    #把user.id 用 session傳送 
        session['message'] = row[0]
        return redirect('/part')

#sql還沒做好        
@app.route('/part')
def part():
    id = session.get('id')

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
    #what is it member.project_id = project.id ???help~~
        sql = "SELECT * FROM `project`, `member` where member.project_id = project.id and member.user_id = {{id}}"
        cursor.execute(sql)

        project_id = [] 
        name = []
        for row in cursor.fetchall():
#原程式
    foreach ($res as $result) {
        
        ?>
        <div onClick="location.href='discuss.php?id=<?=$result['project_id']?>'">
            <?=$result['name']?>
        </div>
        <?php

    return render_template("part.html")
@app.route('/user' ,methods = ['GET', 'POST'])
def user():
    return render_template("user.html")
@app.route('/add' ,methods = ['GET', 'POST'])
def add():
    return render_template("add.html")   

#db
@app.route('/db_add' ,methods = ['GET', 'POST'])
def db_add():
    return redirect(url_for('user.html'))

@app.route('/db_del' ,methods = ['GET', 'POST'])
def db_del():

@app.route('/db_update' ,methods = ['GET', 'POST'])
def db_update():

#db_proj
@app.route('/db_proj_add' ,methods = ['GET', 'POST'])
def db_proj_add():

@app.route('/db_proj_del' ,methods = ['GET', 'POST'])
def db_proj_del():

@app.route('/db_proj_update' ,methods = ['GET', 'POST'])
def db_proj_update():

@app.route('/db_proj_add_user' ,methods = ['GET', 'POST'])
def db_proj_add_user():

#db_opinion
@app.route('/db_opinion' ,methods = ['GET', 'POST'])
def db_opinion():

@app.route('/db_opinion_add' ,methods = ['GET', 'POST'])
def db_opinion_add():


@app.route('/stat' ,methods = ['GET', 'POST'])
def stat():
 
#return render_template(".html",username=request.values.get("Username"))      
#name = request.form['name']