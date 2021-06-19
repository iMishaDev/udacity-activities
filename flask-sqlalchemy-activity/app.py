import datetime
from flask import Flask, render_template, request, redirect, url_for
from models import  setup_db, Workout, User
from sqlalchemy.orm import load_only, joinedload
from datetime import date
import math

# helpful instructions
# You can use the with_entities() method to restrict which columns you'd like to return in the result.
# You can use  options( joinedload(Entity.Column))
# filter == | filter_by(col=)
# searching Entity.ilike('%'+textToSearch+'%'))



app = Flask(__name__)
setup_db(app)

# this is a helper function, you are going to 
# need it when you want to calculate the the 
# total time spent working out during the day,
# since the `totalTiem` is stored as a string.    
def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# here's the entry point which should redirect the user to getWorkouts endpoint,
# as we mentioned in the rREADME we always have to return at leaset one workout fot the viewer
@app.route('/')
def index():
    return redirect(url_for('getWorkouts', workout_id=Workout.query.first().id))


@app.route('/<workout_id>')
def getWorkouts(workout_id):
    # fetch user's workouts history
    # one workout details by the help of workout_id 
    # user's personal data
    # his daily activity showing today's activity ( how much the user moved, exercised and stand ) along with the percentage of achivement based on the user daily goal.
    return render_template('home.html', 
                        workouts=[],
                        dailyActivities={'move': {'cals': 0, 'percentage': 0},
                                        'excercise': {'cals': 0, 'percentage': 0},
                                        'stand': {'cals': 0, 'percentage': 0}
                                        },
                        workout={},
                        user={})


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
    return redirect(url_for('index'))



# Default port:
if __name__ == '__main__':
    app.run(debug=True)
