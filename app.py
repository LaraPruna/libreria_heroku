from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)
with open("books.json") as fichero:
		libros=json.load(fichero)

@app.route('/')
def indice():
	return render_template("indice.html",libros=libros)

@app.route('/libro/<isbn>')
def detalle_libro(isbn):
	for libro in libros:
		if isbn==libro.get("isbn"):
			try:
				titulo=libro.get("title")
				portada=libro.get("thumbnailUrl")
				numpag=libro.get("pageCount")
				if libro.get("longDescription")==None:
					descripcion="Este libro tiene una descripción disponible."
				else:
					descripcion=libro.get("longDescription")
				autores=libro.get("authors")
				cat=libro.get("categories")
				status=libro.get("status")
			except:
				abort(404)
	return render_template("detalle_libro.html",titulo=titulo,portada=portada,numpag=numpag,descripcion=descripcion,autores=autores,cat=cat,status=status)

@app.route('/categoria/<categoria>')
def categorias(categoria):
	titulos=[]
	isbn=[]
	for libro in libros:
		for cat in libro.get("categories"):
			if cat == categoria:
				categoria=cat
				titulos.append(libro.get("title"))
				isbn.append(libro.get("isbn"))
	return render_template("categoria.html",titulos=titulos,isbn=isbn,categoria=categoria)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=True)