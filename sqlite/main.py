from sqlalchemy import text
from database import SessionLocal
from models import User, UserItem

def get_latest_state():
    session = SessionLocal()
    # State Reconstruction using Window Function
    query = text("""
        SELECT username, item_name
        FROM (
            SELECT u.username, i.item_name,
                   ROW_NUMBER() OVER(PARTITION BY u.user_id ORDER BY i.item_id DESC) as rn
            FROM users u
            JOIN user_items i ON u.user_id = i.user_id
        ) t WHERE rn = 1
    """)
    results = session.execute(query)
    for row in results:
        print(f"Current State -> User: {row.username} | Item: {row.item_name}")
    session.close()

def filter_complex_logic():
    session = SessionLocal()
    # Demonstrating 'Boolean Logic' and 'Logical Exclusions'
    # Find active users with items that are NOT done OR quantity > 10
    results = session.query(UserItem).join(User).filter(
        User.active == True,
        (UserItem.done == False) | (UserItem.quantity > 10)
    ).all()
    
    for item in results:
        print(f"Filtered -> {item.owner.username} has {item.item_name}")
    session.close()

if __name__ == "__main__":
    get_latest_state()
    filter_complex_logic()
