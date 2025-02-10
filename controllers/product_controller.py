from flask import Blueprint, request, render_template, jsonify
from services.products_service import ProductService
from models.products import Products, db

# 💡 Agregar `url_prefix='/products'` para que todas las rutas dentro de este controlador empiecen con `/products`
product_blueprint = Blueprint('products', __name__, url_prefix='/products')

# ✅ Obtener todos los productos
@product_blueprint.route('', methods=['GET'])  # La ruta se vuelve "/products"
def get_products():
    products = Products.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description} for p in products])

# ✅ Crear producto
@product_blueprint.route('', methods=['POST'])  # "/products"
def create_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    product = ProductService.create_product(name, description)
    return jsonify({'message': 'Product created', 'id': product.id})
# ✅ Obtener un producto por su ID
@product_blueprint.route('/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = Products.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    return jsonify({"id": product.id, "name": product.name, "description": product.description})

# ✅ Actualizar un producto existente
@product_blueprint.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    product = Products.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    product.name = name
    product.description = description
    db.session.commit()

    return jsonify({'message': 'Product updated successfully'})

# ✅ Página principal (evita conflicto con "/products")
@product_blueprint.route('/home')
def index():
    return render_template('index.html')
