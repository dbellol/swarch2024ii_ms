from models.products import Products, db
class ProductRepository:
    @staticmethod
    def create_product(name, description):
        product = Products(name=name, description=description)
        db.session.add(product)
        db.session.commit()
        return product
    @staticmethod
    def update_product(product_id, name, description):
        product = Products.query.get(product_id)
        if not product:
            return None
        product.name = name
        product.description = description
        db.session.commit()
        return product