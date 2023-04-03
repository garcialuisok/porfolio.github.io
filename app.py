from flask import Flask, render_template

app = Flask(__name__)

#retorna la pagina principal 
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home.html')
def home():
	return render_template('home.html')

@app.route('/porfolio.html')
def porfolio():
	 return render_template('porfolio.html')

@app.route('/service.html')
def service():
	 return render_template('service.html')

@app.route('/contact.html')
def contact():
	 return render_template('contact.html')

# refresca los cambios que se realizan
if __name__ == '__main__':
	app.run(debug=True)  