from flask import Flask, redirect, request
from flask_sqlalchemy import SQLAlchemy
import json
from generate_data import generate_data



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////workspaces/hackyeah2022/backend/quiz.db'
db = SQLAlchemy(app)


class Tag(db.Model):
    id = db.Column(db.Integer, db.Identity(start=0, cycle=True), primary_key=True)
    tag_type = db.Column(db.String(100), nullable=False)
    cord_x = db.Column(db.Float, nullable=False)
    cord_y = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<tag> {self.tagname}'


@app.route('/data/create' , methods = ['POST'])
def create():
    tag_name = request.form['tag_name']
    type = request.form['type']
    cord_x = request.form['cord_x']
    cord_y = request.form['cord_y']
    localisations = Tag(tag_name=tag_name, type=type, cord_x=cord_x, cord_y=cord_y)
    db.session.add(localisations)
    db.session.commit()
    return '', 204


@app.route('/data' , methods = ['GET'] )
def read_data_list():
    tags = Tag.query.all()
    return json.dumps(tags, indent=4), 200


@app.route('/data/<int:id>' , methods = ['GET'])
def read_one_element():
    localisation = Tag.query.filter_by(id=id).first()
    if localisation:
        return json.dumps(localisation, indent=4), 200
    return f"Localisation with id ={id} Does not exist", 404

@app.route('/data/<int:id>/update',methods = ['POST'])
def update(id):
    localisations = Tag.query.filter_by(id=id).first()
    if localisations:
        db.session.delete(localisations)
        db.session.commit()

        tag_name = request.form['tag_name']
        type = request.form['type']
        cord_x = request.form['cord_x']
        cord_y = request.form['cord_y']
        localisations = Tag(tag_name=tag_name, type=type, cord_x=cord_x, cord_y=cord_y)

        db.session.add(localisations)
        db.session.commit()
        return '', 204
    return f"localisation with id = {id} Does not exist", 404


@app.route('/data/<int:id>/delete', methods=['POST'])
def delete(id):
    localisations = Tag.query.filter_by(id=id).first()
    if request.method == 'POST':
        if localisations:
            db.session.delete(localisations)
            db.session.commit()
            return '', 204
        return 'Could not remove', 404


generate_data = generate_data(1000)

for data in generate_data:
    with app.app_context():
        new_tag = Tag(tag_type=data.tag_type, cord_x=data.cord_x, cord_y=data.cord_y)
        db.session.add(new_tag)
        db.session.commit()

