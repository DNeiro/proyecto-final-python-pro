# Importar
from flask import Flask, render_template, request


app = Flask(__name__)


def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef

# La primera página


@app.route('/')
def index():
    return render_template('index.html')
# Segunda página


@app.route('/mouse')
def Mouse():
    return render_template(
                            'Mouse.html')

# La tercera página


@app.route('/teclado')
def teclado():
    return render_template(
                            'teclado.html'
                           )

# Cálculo


@app.route('/monitor')
def monitor():
    return render_template('monitor.html',
                           )
# El formulario


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    # Declarar variables para la recogida de datos
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    # Puedes guardar tus datos o enviarlos por correo electrónico
    return render_template('form_result.html', 
                           # Coloque aquí las variables
                           name=name, email = email,
                           address = address, date = date
                           )


app.run(debug=True)
