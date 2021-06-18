from flask_migrate import Migrate
import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
import timeago
db = SQLAlchemy()
now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config.from_object('config')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    Migrate(app, db)
    db.init_app(app)
    db.create_all()


'''
Workout

'''


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    icon = Column(String)
    totalTime = Column(String)
    totalCal = Column(String)
    activeCal = Column(Integer)
    heart = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, type, icon, totalTime, totalCal, activeCal, heart, created_at):
        self.type = type
        self.icon = icon
        self.totalTime = totalTime
        self.totalCal = totalCal
        self.activeCal = activeCal
        self.heart = heart
        self.created_at = created_at

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'type': self.type,
            'icon': self.icon,
            'totalTime': self.totalTime,
            'totalCal': self.totalCal,
            'activeCal': self.activeCal,
            'heart': self.heart,
            'created_at': timeago.format(self.created_at, now)
        }








'''
User

'''


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(DateTime, default=datetime.datetime.utcnow)
    blod = Column(String)
    health = Column(String)
    water = Column(String)
    moveGoal = Column(Integer)
    excersiceGoal = Column(Integer)
    standGoal = Column(Integer)


    def __init__(self, name, dob, blod, health, water, moveGoal, excersiceGoal, standGoal):
        self.name = name
        self.dob = dob
        self.blod = blod
        self.health = health
        self.water = water
        self.moveGoal = moveGoal
        self.excersiceGoal = excersiceGoal
        self.standGoal = standGoal


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'blod': self.blod,
            'health': self.health,
            'water': self.water,
            'moveGoal': self.moveGoal,
            'excersiceGoal': self.excersiceGoal,
            'standGoal': self.standGoal,
        }
