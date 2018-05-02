from app import DB

class Users(DB.Model):
    """Simple database model to track event attendees."""
    
    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50))
    email = DB.Column(DB.String(30))
    password = DB.Column(DB.String(30))
    address = DB.Column(DB.String(120))
    fv_animal = DB.Column(DB.String(20))

    def __init__(self, name=None, email=None, password=None, address=None, fv_animal=None):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.fv_animal = fv_animal