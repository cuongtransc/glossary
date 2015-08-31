from app import db

class Term(db.Model):

    id = db.Column(db.String, primary_key=True)
    en_term = db.Column(db.String)
    en_desc = db.Column(db.String)
    vi_term = db.Column(db.String)
    vi_desc = db.Column(db.String)


    def to_dict(self):
        return dict(
            id = self.id,
            en_term = self.en_term,
            en_desc = self.en_desc,
            vi_term = self.vi_term,
            vi_desc = self.vi_desc
        )

    def __repr__(self):
        return '<Term %r>' % (self.id)

