from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pineapple123@localhost:15432/Example'
db = SQLAlchemy(app)
db.init_app(app)

if __name__ =='__main__':
	app.run()