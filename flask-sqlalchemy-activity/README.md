

## Udacity Activity Week#2 <img src="https://user-images.githubusercontent.com/12359091/122653726-44b0ef80-d14f-11eb-8849-1cd70624aae5.png" width="20">

this project is built as activity in for the Full Stack Nanodegree. Students are required to complete the requirments to build the backend of this app using flask & SQLAlchemy. the focus of this activity is to give students more practicing of the SQLAlchemy ORM Qeury API. 


### about the acitivty 
this is an Applee Fitness+ App Clone. user can review his activity details (daily activity, workout history)  and start a new workout. he also can review his competitions with other users. calculating the calories is fake also the heart beats. it's just an illustration of how Fitness could look like through the web. 


## setup 
1. make sure you have python to run the app. 
2. install the dependencies required by running `pip3 install -r requirements.txt` 
3. create a postgres database for the app by doing the following: 
    - `sudo -u postgres -i` 
    - `createdb udacity-sqlalchemy-activity;`
    - `exit`
4. make sure you have the same name or else you need to update the `config.py` file with your database name. 
5. start migrating the models you have in `models.py` by doing the following: 
    - `pip3 install flask_migrate`
    - `flask db init`
    - `flask db migrate`
    - `flask db upgrade`
    now you have the database with the tables created, now we need to add data to it.
6. run the `seeder.py` file to fill the database with the dummy data that has been created in the seeder. 
    to run it you just need to do `pythoon3 seeder.py`

Now you have the database filled with data and ready to execute the app by running the following : 
    - `export FLASK_APP=app`
    - `export DEBUG_MODE=True`
    - `flask run`

now you can test the app and navigate through it to have an idea of how it works!! 


### review 
let's start with showing the project strucure : 
.
```
+-- static
|   +-- icons 
|   +-- style.css
+-- templates
|   +-- add-activity.html
|   +-- home.html
|   +-- main.html
+-- config.py
+-- models.py
+-- requirements.py
+-- seeder.py
+-- README.md
```
let's go through the models and check what we have so far. starting with the `user` model:  

```

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

``` 

as you can see, user has basic data, what we want to look at is the `moveGoal, excersiceGoal and standGoal`. each user should have these data so we will be able to calculate his activity. we also have the inserting, updating and deleting functions already setup. format is helpful we want to return the object, we don't need to explicitly format it, we can use format unless we need to filter some data before returning the response. 


now let's go and check the `workout` model : 

```
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

```


what we are intrested to have for each workout is the icon representing the workout, which is already there in the static folder. all we need to do is the path of the icon. the totla time spent doing the workout which is already been calculated by the frontend, your job is just to store it and show it along with the totalCal, the activeCal and the heart beats which are calculated randomly. 




### Note : altough we have users, there's no need to create a login/registraion system. it's a lightweight project but you have to stick to one user through the application and apply all the requiremnts on it

## requirments 
- [ ] user and workout models are not related, you need to add a one to many relationship between them and run the migration again to update it with  the new structure, don't forget to reflect this change on the seeder file. 
- [ ] the user can create a new workout, the frontend is ready to send the requiest and all you have to do is doing the actual creation in the database. 
- [ ] the user should be able to review the following in the home page : 
    - his workouts history
    - one workout details through the `workout viewer`. ( meaning that it's alway gonna be a workout to review, if the user didn't pick one.. you return the first one in the database by default)
    - his competitions ( not included in this version but you can check it out in the solution branch after you finish the one)
    - his personal data
    - his daily activity showing today's activity ( how much the user moved, exercised and stand ) along with the percentage of achivement based on the user daily goal. the frontend is expecting this structure : 

    ```
    dailyActivity = {
        'move': {'cals', 0, 'percentage': 0},
        'excercise': {'cals', 0, 'percentage': 0}
        'stand': {'cals', 0, 'percentage': 0}
    }
    ```

    so as you see it's a huge endpoint! but you can do it! use the Query API to fetch all those and return them in the home page. 
    
    
    
    this is how our app gonna look like if we apply our changes + the competition feature which is exist in the `solution` branch! 
    ### the home page : 
    ![Screen Shot 2021-06-19 at 2 24 21 PM](https://user-images.githubusercontent.com/12359091/122653273-488f4280-d14c-11eb-8849-e3be9e2e78df.png)
    
    
    
    ### starting a workout page
    ![Screen Shot 2021-06-19 at 2 03 47 PM](https://user-images.githubusercontent.com/12359091/122653271-46c57f00-d14c-11eb-850f-d40758b4ab5f.png)
