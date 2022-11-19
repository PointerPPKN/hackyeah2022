import json
from flask import Flask, redirect, render_template, request
from app import db
from models import tag


@app.route('/data/create' , methods = ['POST'])
def create():
    if request.method == 'POST':
        tag_name = request.form['tag_name']
        type = request.form['type']
        cord_x = request.form['cord_x']
        cord_y = request.form['cord_y']
        localisations = tag(tag_name=tag_name, type=type, cord_x=cord_x, cord_y=cord_y)
        db.session.add(localisations)
        db.session.commit()
        return '', 204


@app.route('/data')
def ReadDataList():
    tags = tag.query.all()
    #sparsuj tags w jsona i zwróc jako json
    return json.dumps(tags, indent=4), 200


@app.route('/data/<int:id>')
def ReadOneElement():
    localisation=tag.query.filter_by(id=id).first()
    if localisation:
        #zwróc localisation jako json
        return json.dumps(localisation, indent=4), 200
    return f"Localisation with id ={id} Doenst exist", 404
