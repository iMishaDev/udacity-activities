import datetime
from flask import Flask, render_template, request, redirect, url_for
from models import  setup_db, Workout, User
from sqlalchemy.orm import load_only, joinedload
from datetime import date
import math


app = Flask(__name__)
setup_db(app)

@app.route('/')
def index():
    return redirect(url_for('getWorkouts', workout_id=Workout.query.first().id))
    

# You can use the with_entities() method to restrict which columns you'd like to return in the result.
#   states = Venue.query.with_entities(
#       Venue.city, Venue.state).distinct().all()
#   query = Venue.query.options(
#       load_only('name', 'id'), joinedload(Venue.shows))
#   data = []
#   for state in states: 
#     venues = query.filter(Venue.city==state.city, Venue.state==state.state).all()
#     formattedVenues = []

#     for venue in venues:
#       formattedVenues.append({
#         'name': venue.name,
#         'id': venue.id,
#         'num_upcoming_shows': len(venue.shows)
#       })
#     data.append({
#       'city': state.city,
#       'state': state.state,
#       'venues': formattedVenues
#     })
#  questions =  Venue.query.filter(Venue.name.ilike('%'+textToSearch+'%')).all()

# past_shows = Show.query.filter(
#     Show.venue_id == venue.id,  Show.start_time < todays_datetime).all()
# upcoming_shows = Show.query.filter(
#     Show.venue_id == venue.id,  Show.start_time > todays_datetime).all()


    
def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


@app.route('/<workout_id>')
def getWorkouts(workout_id):
    workout = Workout.query.get(workout_id)
    workoutsHistory = Workout.query.order_by(Workout.created_at.desc()).all()
    user = User.query.first()
    formatted_workouts = [w.format() for w in workoutsHistory]



    todayActivities = Workout.query.filter(
        Workout.created_at==date.today()).all()
    todayActivitiesData = {'move': 0, 'excercise': 0, 'stand': 0}
    for activity in todayActivities:
        todayActivitiesData['move'] += int(activity.totalCal)
        todayActivitiesData['excercise'] += get_sec(activity.totalTime)//60
        todayActivitiesData['stand'] += 1
    
    percentages = {'move': 0, 'excercise': 0, 'stand': 0}
    percentages['move'] = min(math.floor(
        todayActivitiesData['move']/user.moveGoal*100), 100)
    percentages['excercise'] = min(math.floor(
        todayActivitiesData['excercise']/user.excersiceGoal*100), 100)
    percentages['stand'] = min(math.floor(
        todayActivitiesData['stand']/user.standGoal*100) ,100)

    return render_template('home.html',  workouts=formatted_workouts, percentages=percentages, today=todayActivitiesData, workout=workout, user=user)


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
    print(data)
    workout = Workout(type=data['type'],
                        activeCal=data['activeCal'],
                        totalCal=data['totalCal'],
                        totalTime=data['totalTime'],
                        heart=data['heart'],
                        icon='static/icons/'+data['type'].lower()+'.png',
                        created_at=datetime.datetime.now())
    workout.insert()
    return redirect(url_for('index'))


# @app.route('/history', methods=['POST'])
# def addActivity():
#     data = Workout.query.group



# Default port:
if __name__ == '__main__':
    app.run(debug=True)
