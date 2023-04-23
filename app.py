import os
#import psycopg2
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


# configurações para o Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY_DEV')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USERNAME')}:\
{os.getenv('DB_PASSWORD')}@localhost:5432/productsapi"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Product - Modelo
class Product(db.Model):
   """Classe usada para o ORM """
   
   __tablename__ = 'products'

   # define os atributos da Classe que serão as colunas na Tabela
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String())
   description = db.Column(db.String())

   def __init__(self, name, description):
      self.name = name
      self.description = description

   def serialize(self):
      return {
         'id': self.id,
         'name': self.name,
         'description': self.description
      }

# rota para todos os produtos
@app.route('/api/products', methods=['GET'])
def get_products():
   # select em todos os registros da tabela Product
   products = Product.query.all()

   return jsonify([product.serialize() for product in products])

# rota para um produto específico, usando como chave o ID
@app.route('/api/product/<int:id>', methods=['GET'])
def get_product(id):
   # select na tabela Produto filtrando pelo atributo 'id'
   product = Product.query.filter_by(id=id).first()

   if product:
      return jsonify(product.serialize())
   else:
      return jsonify({'error': 'Product not found'})

# rota para criar um novo produto
@app.route('/api/products', methods=['POST'])
def create_product():
   # abre o corpo da requisicao
   data = request.get_json()
   # cria o objeto
   new_product = Product(name=data['name'], description=data['description'])
   # envia para o banco
   db.session.add(new_product)
   db.session.commit()

   return jsonify(['OK', new_product.serialize()])

# rota para atualizar um produto existente
@app.route('/api/product/<int:id>', methods=['PUT'])
def update_product(id):
   # busca o produto pelo id
   product = Product.query.filter_by(id=id).first()
   if product:
      # se existe o produto pesquisado, abre a requisicao
      data = request.get_json()

      # procura pelo atributo 'name' na requisicao, se nao houver
      # mantem o atributo atual
      product.name = data.get('name', product.name)
      product.description = data.get('description', product.description)

      # atualiza o objeto no banco
      db.session.commit()

      return jsonify(['OK', product.serialize()])
   else:
      return jsonify({'error': 'Product not found'})

# rota para deletart um produto pelo ID
@app.route('/api/product/<int:id>', methods=['DELETE'])
def delete_product(id):
   product = Product.query.filter_by(id=id).first()
   if product:
      db.session.delete(product)
      db.session.commit()
      return 'OK', 204
   else:
      return jsonify({'error': 'Product not found'})

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
