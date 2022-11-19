from app import db

class tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50))
    type = db.Column(db.Integer, nullable=False)
    cord_x = db.Column(db.Float, nullable=False)
    cord_y = db.Column(db.Float, nullable=False)



    def __repr__(self):
        return f'<tag> {self.tagname}'
        


