from project import db, app
import re

# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        self.name = self.validate_customer_name(name)
        self.city = self.validate_customer_city(city)
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"
    
    def validate_customer_name(self, name):
        if re.fullmatch(r'[a-zA-Z0-9\s\-,:\'"]{2,20}', name) is None:
            raise ValueError('Incorrect customer name')
        return name
    
    def validate_customer_city(self, city):
        if re.fullmatch(r'[a-zA-Z0-9\s\-,:\'"]{2,20}', city) is None:
            raise ValueError('Incorrect customer city')
        return city


with app.app_context():
    db.create_all()
