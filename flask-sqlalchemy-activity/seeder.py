from flask import Flask
from models import User, Workout
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy()
app.config.from_object('config')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.app = app
db.init_app(app)


user = User(name="Jane Doe",
            dob="1958-6-29",
            blod="O+",
            health="80",
            water="normal",
            moveGoal=700,
            excersiceGoal=70,
            standGoal=12)




user2 = User(name="John Doe",
            dob="1958-6-29",
            blod="O+",
            health="80",
            water="normal",
            moveGoal=700,
            excersiceGoal=70,
            standGoal=12)



user3 = User(name="John Doe Junior",
            dob="1958-6-29",
            blod="O+",
            health="80",
            water="normal",
            moveGoal=700,
            excersiceGoal=70,
            standGoal=12)

db.session.add(user)
db.session.add(user2)
db.session.add(user3)
db.session.commit()



workout1 = Workout(type="Running",
                icon="static/icons/running.png",
                totalTime="01:12:01",
                totalCal=400,
                activeCal=450,
                heart=160,
                created_at="2021-06-18",
                
                )


db.session.add(workout1)
db.session.commit()

workout1 = Workout(type="Dance",
                icon="static/icons/dance.png",
                totalTime="00:15:01",
                totalCal=120,
                activeCal=130,
                heart=140,
                created_at="2021-06-18",
                
                )

db.session.add(workout1)
db.session.commit()

workout1 = Workout(type="Cycling",
                icon="static/icons/cycling.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-06-18",
                
                )

db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="Running",
                icon="static/icons/running.png",
                totalTime="01:12:01",
                totalCal=400,
                activeCal=450,
                heart=160,
                created_at="2021-05-18",
                
                )

db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="Dance",
                icon="static/icons/dance.png",
                totalTime="00:15:01",
                totalCal=120,
                activeCal=130,
                heart=140,
                created_at="2021-05-18",
                
                )

db.session.add(workout1)
db.session.commit()

workout1 = Workout(type="Cycling",
                icon="static/icons/cycling.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-05-18",
                
                )
db.session.add(workout1)
db.session.commit()

workout1 = Workout(type="Cycling",
                icon="static/icons/cycling.png",
                totalTime="01:00:01",
                totalCal=750,
                activeCal=800,
                heart=180,
                created_at="2021-04-18",
                
                )

db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="Cycling",
                icon="static/icons/cycling.png",
                totalTime="02:12:01",
                totalCal=1200,
                activeCal=1250,
                heart=180,
                created_at="2021-04-18",
                
                )

db.session.add(workout1)
db.session.commit()

workout1 = Workout(type="Cycling",
                icon="static/icons/cycling.png",
                totalTime="03:12:01",
                totalCal=2900,
                activeCal=3000,
                heart=180,
                created_at="2021-04-18",
                
                )

db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="swim",
                icon="static/icons/swim.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-03-18",
                
                )

db.session.add(workout1)
db.session.commit()

workout1 = Workout(type="walking",
                icon="static/icons/walking.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-03-18",
                
                )

db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="hiit",
                icon="static/icons/hiit.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-03-18",
                
                )

db.session.add(workout1)
db.session.commit()

workout1 = Workout(type="running",
                icon="static/icons/running.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-03-18",
                
                )

db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="swim",
                icon="static/icons/swim.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-01-18",
                
                )

db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="dance",
                icon="static/icons/dance.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-01-18",
                
                )

db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="running",
                icon="static/icons/running.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-01-18",
                
                )

db.session.add(workout1)
db.session.commit()

workout1 = Workout(type="walking",
                icon="static/icons/walking.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-02-18",
                
                )
db.session.add(workout1)
db.session.commit()


workout1 = Workout(type="dance",
                icon="static/icons/dance.png",
                totalTime="01:12:01",
                totalCal=800,
                activeCal=850,
                heart=180,
                created_at="2021-05-18",
                
                )

db.session.add(workout1)
db.session.commit()
