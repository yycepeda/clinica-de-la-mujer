from flask import Flask
from flask import render_template as render

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render('login.html')

@app.route('/registro', methods=['GET','POST'])
def registro():
    return render('registro.html')

@app.route('/politica-privacidad', methods=['GET'])
def politica_privacidad():
    return render('politica_privacidad.html')

@app.route('/nosotros', methods=['GET'])
def nosotros():
    return render('nosotros.html')

@app.route('/contacto', methods=['GET'])
def contacto():
    return render('contacto.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render('dashboard.html')

@app.route('/medico', methods=['GET'])
def medico():
    return render('medicos.html')

@app.route('/historia-clinica', methods=['GET'])
def historia():
    return render('historia-clinica.html')

@app.route('/listado-citas', methods=['GET'])
def listado_citas():    
    return render('listado-citas.html')

@app.route('/listado-citas/<cita>', methods=['GET'])
def detalle_citas(cita):    
    return render('detalle-cita.html')

@app.route('/form-cita', methods=['GET', 'POST'])
def formCitas():
    return render('form-cita.html')

@app.route('/paciente', methods=['GET'])
def paciente():
    return render('pacientes.html')

@app.route('/paciente/<user>', methods=['GET'])
def userPaciente(user):
    return render('layout-paciente.html', user = user, nacimiento = '1/10/1800', eps = 'SURA', correo='example@uninorte.com.co', cel= 3160000000, dir= 'cali' , ciudad='Cali, Valle')


if __name__ == '__main__': 
    app.run(debug=True, port=8000)