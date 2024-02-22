from flask import Flask, jsonify, redirect

app = Flask(__name__)

# Endpoint para compartir en Facebook
@app.route('/api/compartir', methods=['POST'])
def compartir_en_facebook():
    # Aquí maneja la lógica para generar el enlace de compartir en Facebook
    enlace_compartir = '...'  # Genera el enlace adecuado aquí
    return jsonify({'enlace': enlace_compartir})

# Endpoint para seguir en Facebook
@app.route('/api/seguir', methods=['GET'])
def seguir_en_facebook():
    # Aquí redirige al usuario a la página de Facebook para realizar el seguimiento
    return redirect('https://www.facebook.com/profile.php?id=61556754897854&is_tour_completed=true')

if __name__ == '__main__':
    app.run(debug=True)
