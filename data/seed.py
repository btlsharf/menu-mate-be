from config.database import SessionLocal, engine, Base
from models import Category, MenuItem, User
from config.settings import get_password_hash

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        if db.query(Category).count() == 0:
            categories = [
                Category(name="Appetizers"),
                Category(name="Main Course"),
                Category(name="Desserts"),
                Category(name="Beverages"),
            ]
            db.add_all(categories)
            db.commit()
            print("✓ Categories created")

            menu_items = [
                MenuItem(
                    name="Caesar Salad",
                    description="Fresh romaine lettuce with parmesan and croutons",
                    price=8.99,
                    category_id=1,
                    is_available=True
                ),
                MenuItem(
                    name="Chicken Wings",
                    description="Crispy wings with your choice of sauce",
                    price=12.99,
                    category_id=1,
                    is_available=True
                ),
                MenuItem(
                    name="Grilled Salmon",
                    description="Fresh Atlantic salmon with vegetables",
                    price=24.99,
                    category_id=2,
                    is_available=True
                ),
                MenuItem(
                    name="Beef Burger",
                    description="Juicy beef patty with lettuce, tomato, and cheese",
                    price=15.99,
                    category_id=2,
                    is_available=True
                ),
                MenuItem(
                    name="Margherita Pizza",
                    description="Classic pizza with fresh mozzarella and basil",
                    price=18.99,
                    category_id=2,
                    is_available=True
                ),
                MenuItem(
                    name="Chocolate Cake",
                    description="Rich chocolate layer cake",
                    price=7.99,
                    category_id=3,
                    is_available=True
                ),
                MenuItem(
                    name="Ice Cream",
                    description="Vanilla, chocolate, or strawberry",
                    price=5.99,
                    category_id=3,
                    is_available=True
                ),
                MenuItem(
                    name="Iced Tea",
                    description="Freshly brewed sweet or unsweet",
                    price=2.99,
                    category_id=4,
                    is_available=True
                ),
                MenuItem(
                    name="Coffee",
                    description="Hot or iced coffee",
                    price=3.99,
                    category_id=4,
                    is_available=True
                ),
            ]
            db.add_all(menu_items)
            db.commit()
            print("✓ Menu items created")

        if db.query(User).count() == 0:
            admin_user = User(
                email="admin@menumate.com",
                password_hash=get_password_hash("admin123"),
                role="admin"
            )
            db.add(admin_user)
            db.commit()
            print("✓ Admin user created (email: admin@menumate.com, password: admin123)")

        print("\n✓ Database seeded successfully!")

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Seeding database...")
    init_db()
