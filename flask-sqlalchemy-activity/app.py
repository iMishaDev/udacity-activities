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
    

# helpful instructions 
# You can use the with_entities() method to restrict which columns you'd like to return in the result.
# You can use  options( joinedload(Entity.Column))
# filter == | filter_by(col=)
# searching Entity.ilike('%'+textToSearch+'%'))



    
def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


@app.route('/<workout_id>')
def getWorkouts(workout_id):
    

    return render_template('home.html',  workouts=[], percentages=[], today=[], workout={}, user={})


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
