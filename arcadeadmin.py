import os
import os.path as op
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin.actions import action

from EmulationStation import GameList
from properties import *


# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = secret_key

# Create in-memory database
app.config['DATABASE_FILE'] = db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


def update_xml(list):
    GameList.write(list,gamelist_xml)





# Create models
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


def update_db():
#Updates playcount and last played modified by emulation station
    for game in GameList.read(gamelist_xml):
        arcade = db.session.query(Arcade).filter_by(id=game.name)
        arcade.playcount = int(game.playcount)
        arcade.lastplayed = game.lastplayed

    db.session.commit()
    return


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'




# Customized User model admin
class UserAdmin(sqla.ModelView):
    column_searchable_list = ('name',)
    column_list = ('id','name', 'players','genre','developer','rating','date','favorite')
    column_filters = ('name', 'players','genre','developer','rating','date','favorite')
    column_display_pk = True


    @action('favorite', 'Favorite', 'Are you sure you want to favorite the selected games?')
    def favorite(self, ids):
        selected = Arcade.query.filter(Arcade.id.in_(ids))
        for game in selected:
            if game.favorite == False:
                game.favorite = True

        query = Arcade.query.filter(Arcade.favorite == True)
        list = []
        for game in query:
            go = GameList.game_object()
            go.id = game.id
            go.name = game.name
            go.genre = game.genre
            go.players = str(game.players)
            go.developer = game.developer
            go.rating = str(game.rating / 10)
            go.playcount = str(game.playcount)
            go.lastplayed = game.lastplayed
            go.desc = game.desc
            list.append(go)
            print game.name
        db.session.commit()
        update_xml(list)

    @action('unfavorite', 'Unfavorite', 'Are you sure you want to unfavorite the selected games?')
    def unfavorite(self, ids):
        selected = Arcade.query.filter(Arcade.id.in_(ids))
        for game in selected:
            if game.favorite == True:
                game.favorite = False

        query = Arcade.query.filter(Arcade.favorite == True)
        list = []
        for game in query:
            go = GameList.game_object()
            go.id = game.id
            go.name = game.name
            go.genre = game.genre
            go.players = str(game.players)
            go.developer = game.developer
            go.rating = str(game.rating / 10)
            go.playcount = str(game.playcount)
            go.lastplayed = game.lastplayed
            go.desc = game.desc
            list.append(go)
            print game.name
        db.session.commit()
        update_xml(list)


# Create admin
admin = admin.Admin(app, name='Arcade Admin', template_mode='bootstrap3')



# Add views
admin.add_view(UserAdmin(Arcade, db.session))






def build_db():
    """
    Populate a small db with some example entries.
    """


    db.drop_all()
    db.create_all()



    for game in GameList.read(samlple_gamelist):
        arcade = Arcade()
        arcade.id = game.id
        arcade.name = game.name
        if game.rating != "" and game.rating != None:
            arcade.rating = format(float(game.rating) * 10,'.2f')
        else:
            arcade.rating = 0
        if game.releasedate != None:
            arcade.date = int(game.releasedate)
        else:
            arcade.date = 0
        arcade.developer = game.developer
        arcade.genre = game.genre
        arcade.players = game.players
        arcade.favorite = game.favorite
        arcade.desc = game.desc
        db.session.add(arcade)



    db.session.commit()
    return

if __name__ == '__main__':
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = op.realpath(os.path.dirname(__file__))
    database_path = op.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_db()

    # Start app
    app.run(debug=True)