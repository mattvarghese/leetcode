from database import SessionLocal, engine
from models import Base, User, UserItem

def reset_and_seed():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    session = SessionLocal()
    
    barbie = User(username="barbie", password="password123")
    ken = User(username="ken", password="password123")
    session.add_all([barbie, ken])
    session.flush()

    items = [
        UserItem(user_id=barbie.user_id, item_name="Dream House", quantity=1),
        UserItem(user_id=barbie.user_id, item_name="Microphone", quantity=1),
        UserItem(user_id=ken.user_id, item_name="Rollerblades", quantity=2)
    ]
    session.add_all(items)
    session.commit()
    session.close()
    print("Database Seeded!")

if __name__ == "__main__":
    reset_and_seed()
