import datetime
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.sql.expression import join
from models import Competition, setup_db, Workout, User
from sqlalchemy.orm import load_only, joinedload
from datetime import date
import math


def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

app = Flask(__name__)
setup_db(app)


def getUserDailyActivities(user):
    dailyActivities = { 'move': {'cals': 0, 'percentage': 0},
                        'excercise': {'cals': 0, 'percentage': 0},
                        'stand': {'cals': 0, 'percentage': 0}
                    }
    todayActivities = Workout.query.filter(
        Workout.created_at==date.today(), Workout.user_id==user.id).all()
    for activity in todayActivities:
        dailyActivities['move']['cals'] += int(activity.totalCal)
        dailyActivities['excercise']['cals'] += get_sec(activity.totalTime)//60
        dailyActivities['stand']['cals'] += 1
    
    dailyActivities['move']['percentage'] = min(math.floor(
        dailyActivities['move']['cals']/user.moveGoal*100), 100)
    dailyActivities['excercise']['percentage'] = min(math.floor(
        dailyActivities['excercise']['cals']/user.excersiceGoal*100), 100)
    dailyActivities['stand']['percentage'] = min(math.floor(
        dailyActivities['stand']['cals']/user.standGoal*100), 100)
    return dailyActivities

@app.route('/')
def index():
    return redirect(url_for('getWorkouts', workout_id=Workout.query.filter(Workout.user_id==User.query.first().id).first().id))
    

@app.route('/<int:workout_id>')
def getWorkouts(workout_id):
    workout = Workout.query.get(workout_id)
    workoutsHistory = Workout.query.filter(
        Workout.user_id == User.query.first().id).order_by(Workout.created_at.desc()).all()
    user = User.query.first()
    competitions = Competition.query.filter(Competition.competitior_first_id == User.query.first().id).options(
        joinedload(Competition.competitior_first), joinedload(Competition.competitior_second)).all()
    
    formatted_workouts = [w.format() for w in workoutsHistory]

    
    formatted_competitions = []
    for competition in competitions:
        c={
            "competitior_first_name": competition.competitior_first.name,
            "competitior_second_name": competition.competitior_second.name,
            "competitior_first_score": competition.competitior_first_score,
            "competitior_second_score": competition.competitior_second_score,
            "target": competition.target,
            "end_date": competition.end_date
        }
        formatted_competitions.append(c)
    dailyActivities = getUserDailyActivities(user)
    return render_template('home.html', competitions=formatted_competitions, workouts=formatted_workouts, dailyActivities=dailyActivities, workout=workout, user=user)


@app.route('/start-workout', methods=['GET'])
def addActivity():
    return render_template('add-activity.html', workouts=[
        {
            'type': 'Walking',
            'img': 'static/icons/walking.png'
        },
        {
            'type': 'Running',
            'img': 'static/icons/running.png'
        },
        {
            'type': 'Dance',
            'img': 'static/icons/dance.png'
        },
        {
            'type': 'Yoga',
            'img': 'static/icons/walking.png'
        },
        {
            'type': 'Cycling',
            'img': 'static/icons/cycling.png'
        },
        {
            'type': 'Swim',
            'img': 'static/icons/swim.png'
        },
        {
            'type': 'Cooldown',
            'img': 'static/icons/cooldown.png'
        },
        {
            'type': 'HIIT',
            'img': 'static/icons/hiit.png'
        }
    ])




@app.route('/start-workout', methods=['POST'])
def addActivityPost():
    data = request.form
    workout = Workout(type=data['type'],
                        activeCal=data['activeCal'],
                        totalCal=data['totalCal'],
                        totalTime=data['totalTime'],
                        heart=data['heart'],
                        icon='static/icons/'+data['type'].lower()+'.png',
                        user_id=User.query.first().id,
                        created_at=date.today())
    workout.insert()

    competitions = Competition.query.filter(Competition.competitior_first_id==User.query.first().id).options(
        joinedload(Competition.competitior_first), joinedload(Competition.competitior_second)).all()

    for competition in competitions:
        competition.competitior_first_score += int(workout.totalCal)
        competition.update()

    return redirect(url_for('index'))


# Default port:
if __name__ == '__main__':
    app.run(debug=True)
