import os
from sqlalchemy import (
    create_engine, Column, Integer, String, 
    Boolean, ForeignKey, func, text
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import OperationalError

# 1. SETUP & CONNECTION 
# Matches your docker-compose.yaml: user, password, and practice_db
DATABASE_URL = "postgresql://user:password@localhost:5432/practice_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 2. MODELS (Aligned with your SQL notes)
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False) # Added per your notes
    active = Column(Boolean, default=True)
    
    items = relationship("UserItem", back_populates="owner", cascade="all, delete-orphan")

class UserItem(Base):
    __tablename__ = "user_items"
    item_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    done = Column(Boolean, default=False) # Matches your SQL notes
    
    owner = relationship("User", back_populates="items")

# 3. CORE LOGIC
def seed_data(session):
    """Inserts initial data if the tables are empty."""
    if session.query(User).count() == 0:
        print("--- Seeding Initial Data (Barbie & Ken) ---")
        barbie = User(username="barbie", password="password123")
        ken = User(username="ken", password="password123")
        session.add_all([barbie, ken])
        session.flush() # Gets IDs without committing

        items = [
            UserItem(user_id=barbie.user_id, item_name="Dream House", quantity=1),
            UserItem(user_id=barbie.user_id, item_name="Pink Convertible", quantity=1, done=True),
            UserItem(user_id=ken.user_id, item_name="Rollerblades", quantity=2),
            UserItem(user_id=ken.user_id, item_name="Mojo Dojo House Kit", quantity=12)
        ]
        session.add_all(items)
        session.commit()

def run_interview_drills(session):
    """Drills for Jeff's interview: State Reconstruction & Atomic Deletion."""
    
    # Drill 1: State Reconstruction (Window Function)
    # Finding the 'Latest' item ID per user as a proxy for state
    print("\n--- Drill 1: Reconstructing State (Latest Item ID) ---")
    window_query = text("""
        SELECT username, item_name
        FROM (
            SELECT u.username, i.item_name,
                   ROW_NUMBER() OVER(PARTITION BY u.user_id ORDER BY i.item_id DESC) as rn
            FROM users u
            JOIN user_items i ON u.user_id = i.user_id
        ) t WHERE rn = 1
    """)
    results = session.execute(window_query)
    for row in results:
        print(f"User: {row.username} | Current Item: {row.item_name}")

    # Drill 2: Atomic Deactivation (ACID Principles)
    print("\n--- Drill 2: Atomic Deactivation of Ken ---")
    try:
        ken = session.query(User).filter(User.username == 'ken').first()
        if ken and ken.active:
            ken.active = False
            # Logical Exclusion: Delete items belonging to the inactive user
            session.query(UserItem).filter(UserItem.user_id == ken.user_id).delete()
            session.commit()
            print("Ken deactivated and items deleted atomically.")
        else:
            print("Ken already inactive or not found.")
    except Exception as e:
        session.rollback()
        print(f"Transaction failed: {e}")

# 4. EXECUTION
if __name__ == "__main__":
    try:
        # Create tables (only if they don't exist)
        Base.metadata.create_all(engine)
        
        db_session = SessionLocal()
        
        seed_data(db_session)
        run_interview_drills(db_session)
        
        db_session.close()
        print("\nPractice session complete.")
        
    except OperationalError:
        print("!! Connection Error !!")
        print("Ensure your docker container is up: 'docker compose up -d'")
        print("If password fails, wipe ./postgres_data and restart docker.")

