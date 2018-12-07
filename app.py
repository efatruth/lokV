#livinus felix bassey
#LokaverkefnI
#20.11.2018
from bottle import run, route, template, request, response, redirect, static_file
import datetime, pymysql

connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0301865919',
                             password='mypassword',
                             db='0301865919_lokaverkefni',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:

        # Create a new record
        sql = "INSERT INTO `notandur` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('daniel@yahoo.com', '2468'))

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `notandur` WHERE `email`=%s"
        cursor.execute(sql, ('john@yahoo.com',))
        result = cursor.fetchone()

        # view record
        print(result)
finally:
    connection.close()

# ath. þessi kóði kemur ekki í veg fyrir margskráningu (sami notandi aftur og aftur skráður.)

expire_date = datetime.datetime.now()
expire_date = expire_date + datetime.timedelta(days=90)

conn_cur = connection.cursor()

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./storedfiles')

@route('/')
def index():
    if request.get_cookie("name", secret="logged-in"):
        redirect('/todo')
    else:
        return template('mainpage.tpl')

@route('/login')
def login():
    if request.get_cookie("name", secret="logged-in"):
        redirect('/todo')
    else:
        return template("login.tpl", message=" ")

@route('/login', method="POST")
def login_post():
    conn_cur.execute('SELECT Username, Password FROM notandur')
    users = conn_cur.fetchall()

    user_list = []
    for i, x in users:
        user_list.append([i, x])

    signinUser = request.forms.get('username')
    signinPass = request.forms.get('pass')

    global user
    user = signinUser.strip("'")
    signIn = list((signinUser, signinPass))

    for notandanafn, lykilord in user_list:
        if signIn[0] == notandanafn and signIn[1] == lykilord:
            response.set_cookie("name", user, secret="logged-in", expires=expire_date)
            redirect('/todo')
            break
    return template('login.tpl', message="Innskráning hefur ekki staðist")


@route('/signup')
def signup():
    if request.get_cookie("name", secret="logged-in"):
        redirect('/todo')
    else:
        return template("signup.tpl", message=" ")

@route('/signup', method="POST")
def signup_post():
    conn_cur.execute('SELECT * FROM notandur')
    users = conn_cur.fetchall()

    user_list = []
    for i in users:
        user_list.append([i])

    signupUser = request.forms.get('username')
    displayUser = request.forms.get('displayname')
    signUpPass = request.forms.get('pass')
    confirmpass = request.forms.get('confirmpass')
    signUp = list((signupUser, signUpPass))

    complete = True
    for notendanafn in user_list:
        if signUp[0] == notendanafn[0][0]:
            complete = False
        elif signUpPass != confirmpass:
            complete = False

    if complete == True:
        conn_cur.execute('INSERT INTO notandur VALUES(%s, %s, %s)', (signupUser, displayUser, signUpPass))
        connection.commit()
        conn_cur.execute('CREATE TABLE IF NOT EXISTS ' + str(signupUser) +
                        ' (Name VARCHAR(50) NOT NULL, ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT);')
        connection.commit()
        return template('signup.tpl', message="Nýskráning hefur staðist")
    elif complete == False:
        return template('signup.tpl', message="Nýskráning hefur ekki staðist")

@route('/todo')
def todo():
    if request.get_cookie("name", secret="logged-in"):
        user = request.get_cookie("name", secret="logged-in")
        user_database = request.get_cookie("name", user, secret="logged-in")
        all_data = conn_cur.execute('SELECT * FROM ' + user_database)
        everything = conn_cur.fetchall()
        conn_cur.execute("SELECT Disp_Name FROM Users WHERE Username = '" + user + "'")
        display_name = conn_cur.fetchall()
        dblist = []
        for i in everything:
            dblist.append(i)
        display_name = display_name[0][0]
        row_1 = dblist
        return template('todo.tpl', data_1=row_1, display_name=display_name)
    else:
        redirect('/')

@route('/delete', method="POST")
def deletetodo():
    user = request.get_cookie("name", secret="logged-in")
    deleterow = request.forms.get('deltodo')
    conn_cur.execute('DELETE FROM ' + user + ' WHERE ID = %s', deleterow)
    connection.commit()
    redirect('/todo')

@route('/add', method="POST")
def updatetodo():
    user = request.get_cookie("name", secret="logged-in")
    chore = request.forms.get('adding')
    conn_cur.execute("INSERT INTO " + user + "(Name) VALUES ('" + chore + "');")
    connection.commit()
    redirect('/todo')

@route('/signout')
def logout():
    user = request.get_cookie("name", secret="logged-in")
    response.set_cookie("name", user, secret="logged-in", max_age=0)
    redirect('/')

run(host='localhost', port=8080, reloader=True, debug=True)
