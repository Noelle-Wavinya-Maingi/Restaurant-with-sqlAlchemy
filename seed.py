from sqlalchemy.orm import sessionmaker
from models import engine, Customer, Restaurant, Review
import random
from faker import Faker

# Create a Faker instance to generate fake data
fake = Faker()

Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    # Create restaurants and customers
    for _ in range(10):  # You can adjust the number of records as needed
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(100, 4000)
        )
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(restaurant)
        session.add(customer)
        session.commit()  # Commit after adding each restaurant and customer

    # Create reviews for customers
    for _ in range(30):  # You can adjust the number of reviews as needed
        customer = random.choice(session.query(Customer).all())
        restaurant = random.choice(session.query(Restaurant).all())
        rating = random.randint(1, 5)
        review = Review(
            customer=customer,
            restaurant=restaurant,
            star_rating=rating
        )
        session.add(review)
        session.commit()  # Commit after adding each review

if __name__ == "__main__":
    seed_database()
