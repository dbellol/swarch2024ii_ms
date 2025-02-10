from flask import Flask, render_template
from models.products import db
from controllers.product_controller import product_blueprint

app = Flask(__name__, template_folder='templates')

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123@172.17.0.3:3306/swarch2024ii_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos
db.init_app(app)

# Registrar el blueprint
app.register_blueprint(product_blueprint)

# ✅ Hacer que `index.html` también cargue en `/`
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)

