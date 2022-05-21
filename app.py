from flask import Flask, render_template, request
from redis import Redis
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='templates')


redis = Redis(host="redis", db=0, socket_timeout=5, charset="utf-8", decode_responses=True)

#code for connection
app.config['MYSQL_USER'] = 'myuser'
app.config['MYSQL_PASSWORD'] = 'mypassword'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():

    cur = mysql.connection.cursor()
    cur.execute(''' CREATE TABLE players(identifier varchar(255), name varchar(255) UNIQUE, amountofgold int(11)) ''')
    mysql.connection.commit()
    cur.close()
    return 'Player Table create !'

@app.route('/Createplayer', methods=['POST', 'GET'])
def Createplayer():

    if request.method == 'POST':
        userDetails = request.form
        identifier = userDetails['identifier']
        name = userDetails['name']
        amountofgold = userDetails['amountofgold']
        redis.rpush("amountofgold", {'amountofgold':amountofgold})
        redis.rpush("identifier", {'identifier':identifier})
        #redis.set("identifier", identifier)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO players(identifier,name) VALUES(%s, %s)",(identifier,name))
        mysql.connection.commit()
        cur.close()
        return 'Great ! You Have Successfully Registered The Player!'
    return render_template('index.html')

@app.route('/Getplayer')
def Getplayer():

     cur = mysql.connection.cursor()
     resultValue = cur.execute("SELECT * FROM players")
     if resultValue > 0:
        playerDetails = cur.fetchall()
        cur.close()
        #getgold=redis.lrange( "amountofgold", 0, -1 )
        getgold=redis.lrange('amountofgold', 0, -1)
        print(getgold)
        return render_template('player.html',playerDetails=playerDetails,getgold=getgold)