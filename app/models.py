from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurant'

    serialize_rules = ('-restaurantPizza.hero',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurantPizza = db.relationship('RestaurantPizza', backref='restaurant')

    def __repr__(self):
        return f'<Restaurant {self.name} for {self.address}>'

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantPizza'

    serialize_rules = ('-restaurant.resraurantPizza', '-pizza.restaurantPizza',)
    
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))

class Pizza(db.Model, SerializerMixin):
    __tablename__='pizza'
    serialize_rules = ('-resturantPizza.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    restaurantPizza = db.relationship('RestaurantPizza', backref='pizza')        

    def __repr__(self):
        return f'<Pizza {self.name} ingredients: {self.ingredients} '