from flask import Flask,request,render_template,flash
from flaskext.mysql import MySQL
from wtforms import Form, validators,TextField,RadioField,SubmitField,BooleanField,HiddenField
import db_config
from flask_basicauth import BasicAuth
import pandas as pd

print 'Attempting to Enter Database'
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = db_config.host
app.config["MYSQL_DATABASE_USER"] = db_config.user
app.config["MYSQL_DATABASE_PASSWORD"] = db_config.password
app.config["MYSQL_DATABASE_DB"] = db_config.db
app.config["MYSQL_DATABASE_PORT"] = db_config.port
mysql=MySQL(app)
conn=mysql.connect()
cur= conn.cursor()
print 'Successfully Connected to Database'


app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'rishi'
basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def start():

	# Querying Database
	query="""\
	    SELECT * from table1;
	    """
	df=pd.read_sql(query,conn)

	# Creating Table HTML
	data = ''
	for index, row in df.iterrows():
		temp = '<tr><td>'+row['Name']+'</td><td>'+row['Phone']+'</td><td>'+row['Sector']+'</td><td>'+row['Chapter']+'</td><td>'+row['Village']+'</td><td>'+row['Name']+'</td><td>'+row['Email']+'</td></tr>'
		data = data + temp
	
	return render_template('index.html', data=data)

if __name__=="__main__":
	app.run(debug=True)
