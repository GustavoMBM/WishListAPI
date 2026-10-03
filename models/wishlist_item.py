from factory import db

class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = True)
    link = db.Column(db.Text, nullable = True)
    purchased = db.Column(db.Boolean, default = False)
 
    purchased = db.Column(db.Boolean, default=False, server_default="0", nullable=False)

    def __init__(self, name, description=None, link=None, purchased=False, sort_order=None):
        self.name = name
        self.description = description
        self.link = link
        self.purchased = purchased
        self.sort_order = sort_order