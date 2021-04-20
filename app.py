from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)
with open("books.json") as fichero:
		libros=json.load(fichero)

@app.route('/')
def indice():
	isbn=[]
	titulos=[]
	for libro in libros:
		isbn.append(libro.get("isbn"))
		titulos.append(libro.get("title"))
	return render_template("indice.html",isbn=isbn,titulos=titulos)

@app.route('/libro/<isbn>')
def detalle_libro(isbn):
	for libro in libros:
		if isbn==libro.get("isbn"):
			try:
				titulo=libro.get("title")
				portada=libro.get("thumbnailUrl")
				numpag=libro.get("pageCount")
				descripcion=libro.get("longDescription")
				autores=libro.get("authors")
				cat=libro.get("categories")
				status=libro.get("status")
			except:
				abort(404)
	return render_template("detalle_libro.html",titulo=titulo,portada=portada,numpag=numpag,descripcion=descripcion,autores=autores,cat=cat,status=status)

@app.route('/categoria/<categoria>')
def categorias(categoria):
	categorias=[]
	for libro in libros:
		if libro.get("categories") not in categorias:
			categorias.append(libro.get("categories"))
	return render_template("categoria.html",categorias=categorias)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=True)