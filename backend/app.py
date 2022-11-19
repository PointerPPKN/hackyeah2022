from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////workspaces/hackyeah2022/backend/quiz.db'
db = SQLAlchemy(app)


class tag(db.Model):
    id = db.Column(db.Integer, db.Identity(start=0, cycle=True), primary_key=True)
    tag_name = db.Column(db.String(50))
    tag_type = db.Column(db.Integer, nullable=False)
    cord_x = db.Column(db.Float, nullable=False)
    cord_y = db.Column(db.Float, nullable=False)



    def __repr__(self):
        return f'<tag> {self.tagname}'

app.app_context().push()
