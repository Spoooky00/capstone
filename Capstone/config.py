from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'clinic'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = "test"
mysql.init_app(app)
