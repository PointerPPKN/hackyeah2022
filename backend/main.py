from flask import Flask, redirect, render_template, request
from app import db
from models import tag
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
    if request.method == 'POST':
        id = request.form['id']
        tag_name = request.form['tag_name']
        type = request.form['type']
        cord_x = request.form['cord_x']
        cord_y = request.form['cord_y']
        localisations = tag(id=id, tag_name=tag_name, type=type, cord_x=cord_x, cord_y=cord_y)
        db.session.add(localisations)
        db.session.commit()
        return redirect('/data')
@app.route('/data')
def ReadDataList():
    ids = id.query.all()
    return render_template('datalist.html',ids = ids)
@app.route('/data/<int:id>')
def ReadOneElement():
    localisation=tag.query.filter_by(id=id).first()
    if localisation:
        return render_template('data.html', localisation = localisation)
    return f"Localisation with id ={id} Doenst exist"
