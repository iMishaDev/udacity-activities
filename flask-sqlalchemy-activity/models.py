from flask_migrate import Migrate
import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Sequence
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
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, type, icon, totalTime, totalCal, activeCal, heart, created_at, user_id):
        self.type = type
        self.icon = icon
        self.totalTime = totalTime
        self.totalCal = totalCal
        self.activeCal = activeCal
        self.heart = heart
        self.user_id = user_id
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


# class Friendship(db.Model):
#     __tablename__ = 'friend'
#     fk_user_from = db.Column(
#         db.Integer, db.ForeignKey('user.id'), primary_key=True)
#     fk_user_to = db.Column(
#         db.Integer, db.ForeignKey('user.id'), primary_key=True)
#     extra_field = db.Column(db.Integer)



class Competition(db.Model):
    __tablename__ = 'competitions'

    id = Column(Integer, Sequence('competition_id_seq'), primary_key=True)
    competitior_first_id = Column(Integer, ForeignKey('users.id'), primary_key=True, nullable=False)
    competitior_second_id = Column(Integer, ForeignKey('users.id'), primary_key=True, nullable=False)
    competitior_first_score = Column(Integer)
    competitior_second_score = Column(Integer)
    target = Column(Integer)
    end_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, competitior_first_id, competitior_second_id, competitior_first_score, competitior_second_score, target, end_date):
        self.competitior_first_id = competitior_first_id
        self.competitior_second_id = competitior_second_id
        self.competitior_first_score = competitior_first_score
        self.competitior_second_score = competitior_second_score
        self.end_date = end_date
        self.target = target

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
            'competitior_first': self.competitior_first_id,
            'competitior_second': self.competitior_second_id,
            'competitior_first_score': self.competitior_first_score,
            'competitior_second_score': self.competitior_second_score,
            'end_date': self.end_date,
            'target': self.target,
        }


'''
User

'''

# class User (db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     user_to = db.relationship(
#         'Friendship', backref='to', primaryjoin=id == Friendship.fk_user_to)
#     user_from = db.relationship(
#         'Friendship', backref='from', primaryjoin=id == Friendship.fk_user_from)

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
    workouts = relationship("Workout",  backref='user', lazy=False)
    ompetitior_first = relationship(
        'Competition', backref='competitior_first', primaryjoin=id == Competition.competitior_first_id)
    ompetitior_second = relationship(
        'Competition', backref='competitior_second', primaryjoin=id == Competition.competitior_second_id)
    # competitions = relationship('Competition', backref='user', lazy=False)

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
