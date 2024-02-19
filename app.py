# Importamos las librerías necesarias
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# Creamos una instancia de la clase Flask
app = Flask(__name__)

# Simulamos una base de datos de usuarios
# Las contraseñas se almacenan como hashes por seguridad
users = {
    "user1": generate_password_hash("password1"),
    "user2": generate_password_hash("password2")
}

# Definimos una ruta para el registro de usuarios
@app.route('/register', methods=['POST'])
def register():
    # Obtenemos el nombre de usuario y la contraseña del cuerpo de la solicitud
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Verificamos si el nombre de usuario ya existe
    if username in users:
        # Si el nombre de usuario ya existe, devolvemos un error
        return jsonify({"message": "El usuario ya existe"}), 400
    
    # Si el nombre de usuario no existe, lo agregamos a la base de datos
    users[username] = generate_password_hash(password)
    
    # Devolvemos un mensaje de éxito
    return jsonify({"message": "Usuario registrado exitosamente"}), 201

# Definimos una ruta para el inicio de sesión de usuarios
@app.route('/')
def home():
    return "¡Bienvenido a mi aplicación Flask!"

@app.route('/login', methods=['POST'])
def login():
    # Obtenemos el nombre de usuario y la contraseña del cuerpo de la solicitud
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Verificamos si el nombre de usuario existe y si la contraseña es correcta
    if username in users and check_password_hash(users[username], password):
        # Si el nombre de usuario existe y la contraseña es correcta, devolvemos un mensaje de éxito
        return jsonify({"message": "Autenticación satisfactoria"}), 200
    
    # Si el nombre de usuario no existe o la contraseña es incorrecta, devolvemos un error
    return jsonify({"message": "Error en la autenticación"}), 401

# Ejecutamos la aplicación
if __name__ == '__main__':
    app.run(debug=True)
