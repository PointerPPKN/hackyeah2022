from app import db

class tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<tag> {self.tagname}'
        


