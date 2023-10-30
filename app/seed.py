from random import choice as rc
from sqlalchemy.orm import sessionmaker
from faker import Faker
from flask import session
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurant=[]
    for i in range(50):
        rest= Restaurant(name=fake.company(), address= fake.address())
        restaurant.append(rest)

    db.session.add_all(restaurant) 
    db.session.commit()  

    pizza = []
    for i in range(50):
        pizzaname = fake.word() + ' ' + fake.word()
        ingredients = ', '.join(fake.word() for _ in range(4))  # Convert list to comma-separated string
        piz = Pizza(name=pizzaname, ingredients=ingredients)
        pizza.append(piz)

    db.session.add_all(pizza)
    db.session.commit()

