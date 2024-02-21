#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models
from app import app
from models import Production, db

# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`


# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

# 8.✅ Create a query to delete all existing records from Production  
def clear_database():
    print('clearing database..')
    Production.query.delete()
   
# 9.✅ Create some seeds for production and commit them to the database. 
def create_productions():
    print('creating productions...')
    productions = []

    p1 = Production(
        title = 'Hamilton',
        genre = 'Musical',
        director = 'Lin-Manuel Miranda',
        image = "some image url",
        budget = 101.00,
        description = "some description",
        ongoing = True
    )
    productions.append(p1)

    p2 = Production(
        title = "Hamlet",
        genre = "Drama",
        budget = 102.00,
        image = "some image url",
        director = "Some person",
        description = "some description",
        ongoing = False
    )
    productions.append(p2)

    p3 = Production(
        title = "Romeo and Juliet",
        genre = "Tragedy",
        budget = 103.00,
        image = "some image url",
        director = "Some person",
        description = "some description",
        ongoing = True
    )
    productions.append(p3)

    p4 = Production(
        title = "SomePlay",
        genre = "Drama",
        budget = 104.00,
        image = "some image url",
        director = "Some person",
        description = "some description",
        ongoing = False
    )
    productions.append(p4)

    db.session.add_all(productions)
    print("adding productions to database...")

    db.session.commit()

# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  
    
if __name__ == "__main__":
    with app.app_context():
        clear_database()
        create_productions()
        print('seeding complete')
        