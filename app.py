from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, Product
from forms import ProductForm

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        q = request.args.get('q', '').strip()
        page = request.args.get('page', 1, type=int)
        if q:
            products = Product.query.filter(
                (Product.name.ilike(f"%{q}%")) |
                (Product.sku.ilike(f"%{q}%")) |
                (Product.supplier.ilike(f"%{q}%"))
            ).order_by(Product.created_at.desc()).paginate(page=page, per_page=8)
        else:
            products = Product.query.order_by(Product.created_at.desc()).paginate(page=page, per_page=8)
        return render_template('index.html', products=products, q=q)

    @app.route('/product/new', methods=['GET', 'POST'])
    def add_product():
        form = ProductForm()
        if form.validate_on_submit():
            product = Product(
                sku=form.sku.data.strip(),
                name=form.name.data.strip(),
                description=form.description.data.strip(),
                quantity=form.quantity.data,
                price=float(form.price.data),
                supplier=form.supplier.data.strip()
            )
            db.session.add(product)
            db.session.commit()
            flash('Product added successfully', 'success')
            return redirect(url_for('index'))
        return render_template('add_edit.html', form=form, title="Add Product")

    @app.route('/product/<int:product_id>/edit', methods=['GET', 'POST'])
    def edit_product(product_id):
        product = Product.query.get_or_404(product_id)
        form = ProductForm(obj=product)
        if form.validate_on_submit():
            product.sku = form.sku.data.strip()
            product.name = form.name.data.strip()
            product.description = form.description.data.strip()
            product.quantity = form.quantity.data
            product.price = float(form.price.data)
            product.supplier = form.supplier.data.strip()
            db.session.commit()
            flash('Product updated successfully', 'success')
            return redirect(url_for('index'))
        return render_template('add_edit.html', form=form, title="Edit Product")

    @app.route('/product/<int:product_id>/delete', methods=['POST'])
    def delete_product(product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted', 'info')
        return redirect(url_for('index'))

    @app.route('/product/<int:product_id>')
    def view_product(product_id):
        product = Product.query.get_or_404(product_id)
        return render_template('view.html', product=product)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
