from flask import Flask, render_template, request, redirect, url_for 

app = Flask(__name__)


species_list = [
    {'name': 'Elephant', 'habitat':'Africa'},
    {'name': 'Lion', 'habitat':'Africa'},
    {'name': 'Girafe', 'habitat':'Africa'},
    {'name': 'Tiger', 'habitat':'Asia'},
    {'name': 'Bat', 'habitat':'Africa'},
    {'name': 'Penguin', 'habitat':'Antartica'},
    {'name': 'Seal', 'habitat':'Antartica'},
    {'name': 'Eagle', 'habitat':'America'},
    {'name': 'Falcon', 'habitat':'Asia'},
    {'name': 'Ostrich', 'habitat':'Africa'}

]

@app.route("/")
def index():
    return render_template("index.html", species_list = species_list)

@app.route("/add", methods = ['POST','GET'])
def add_species():
    if request.method == 'POST':
        species_name = request.form['species_name']
        habitat = request.form['habitat']
        species_list.append({'name':species_name, 'habitat':habitat})
        return redirect(url_for('index'))
    return render_template("add_species.html")

if __name__ == "__main__":
    app.run(debug=True)
