from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Numeric(precision=10, scale=2)) 
    # Precision is the number of digits in a number. 
    # Scale is the number of digits to the right of the decimal point in a number.
    # E.g.  123.45 has a precision of 5 and a scale of 2.  

    def __repr__(self):
        return f"<Plant {self.name} , {self.price}>"
