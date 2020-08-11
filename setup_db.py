from app import app, db
from app.models import Task

db.drop_all() #drops all the tables
db.create_all() #looks at internal structure of database and creates it for us

tasks = [
    'Eat some food',
    'Listen to some music',
    'Read a book',
]

for task in tasks:
    new_task = Task(name=task, description='')
    db.session.add(new_task)
db.session.commit()
