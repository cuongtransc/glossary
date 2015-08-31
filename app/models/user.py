from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    username = db.Column(db.String)
    
    firstname = db.Column(db.String)
    
    lastname = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            username = self.username,
            firstname = self.firstname,
            lastname = self.lastname,
            id = self.id
        )

    def __repr__(self):
        return '<User %r>' % (self.id)
