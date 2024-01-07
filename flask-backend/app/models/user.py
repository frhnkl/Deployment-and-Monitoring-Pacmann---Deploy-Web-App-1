from app.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    role = db.Column(db.String(80), nullable=False)
    
    def has_role(self, role_name):
        return self.role == role_name
    
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override `get_id`") from None

    def serialize(self): 
        return {
            "user_id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }