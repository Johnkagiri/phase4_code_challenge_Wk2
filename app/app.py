from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound    
from flask_cors import CORS
from models import db, Restaurant, Pizza, RestaurantPizza
import os

file_path = os.path.abspath(os.getcwd())+"\app.db"
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class Home(Resource):

    def get(self):

        response_dict = {
            "index": "Welcome to the restaurants",
        }

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response
          

api.add_resource(Home, '/')

class Restaurant_res(Resource):
    def get(self):
        restaurant_dict=[n.to_dict() for n in Restaurant.query.all()]
        response = make_response(
            jsonify(restaurant_dict),200
        )
        return response
api.add_resource(Restaurant_res,'/restaurant')    

class RestaurantByid(Resource):
    def get(self, id):
        restaurant_dict=Restaurant.query.filter_by(id=id).first().to_dict()
        response = make_response(
            jsonify(restaurant_dict),200
        )
        return response
api.add_resource(RestaurantByid, '/restaurant/<int:id>')   

class Pizza_res(Resource):
    def get(self):
        pizza_dict=[n.to_dict() for n in Pizza.query.all()]
        response = make_response(
            jsonify(pizza_dict),200
        )
        return response
api.add_resource(Pizza_res,'/pizza') 

class PizzaByid(Resource):
    def get(self, id):
        pizza_dict=Pizza.query.filter_by(id=id).first().to_dict()
        response = make_response(
            jsonify(pizza_dict),200
        )
        return response
api.add_resource(PizzaByid, '/pizza/<int:id>')

class RestaurantPizzares(Resource):
    def post(self):
        data = request.get_json()        
        newrec= RestaurantPizza(
            price=data.get('price'),
            restaurant_id=data.get('restaurant_id'),
            pizza_id=data.get('pizza_id')
        )
        db.session.add(newrec)
        db.session.commit() 
        return make_response(
            jsonify(
                {'price': newrec.price, 'restaurant_id': newrec.restaurant_id, 'pizza_id': newrec.pizza_id }))

api.add_resource(RestaurantPizzares, '/restaurantpizza')