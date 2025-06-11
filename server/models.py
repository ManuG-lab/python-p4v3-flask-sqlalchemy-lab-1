from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'
    
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)


    @property
    def serialize(self):
        return {
            "id": self.id,
            "location": self.location,
            "magnitude": self.magnitude,
            "year": self.year
        }

    serialize_rules = ('-id',)  # Exclude id from serialization
    def __repr__(self):
        return f"<Earthquake {self.magnitude} at {self.location} on {self.year}>"
