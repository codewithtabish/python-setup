from models import db  # Import db from models package

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
    
    # \x24326224313024763772592f4a7459723263753644724b4e305562372e64453178704a734956423472714e4435766d506b5a4f6d692e7470674e5153
