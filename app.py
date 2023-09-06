from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import dbase as dbase  

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    recetas = db['receta']
    recetarecivida = recetas.find()
    return render_template('index.html', recetas = recetarecivida)

@app.route('/recetas/<string:receta>')
def ingredientes(receta):
    ingrediente = db['receta']
    ingredientesrecividos = ingrediente.find({'name': receta})
    return render_template('receta.html', ingrediente = ingredientesrecividos)

