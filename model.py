import arcadeadmin

class Arcade(db.Model):
    __tablename__ = 'arcade'
    id = db.Column(db.String, primary_key=True)
    name = rating = db.Column(db.String(30))
    genre = db.Column(db.String(30))
    date = db.Column(db.Integer)
    developer = db.Column(db.String(30))
    players = db.Column(db.Integer)
    rating = db.Column(db.Float)
    favorite = db.Column(db.Boolean)
    playcount = db.Column(db.Integer)
    lastplayed =  db.Column(db.String)
    desc = db.Column(db.String(10000000))


    # Required for administrative interface. For python 3 please use __str__ instead.
    def __unicode__(self):
        return self.id