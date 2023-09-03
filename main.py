from seed import seed_database
from sqlalchemy.orm import sessionmaker
from models import engine, Restaurant, Customer, Review

if __name__ == "__main__":
    seed_database()


Session = sessionmaker(bind=engine)
session = Session()


def print_separator():
    print("\n" + "=" * 40 + "\n")

# Query all restaurants and print their names and prices
print("All Restaurants:")
restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
    print(f"Name: {restaurant.name}, Price: {restaurant.price}")

print_separator()

# Query all customers and print their full names
print("All Customers:")
customers = session.query(Customer).all()
for customer in customers:
    print(f"Full Name: {customer.full_name()}")

print_separator()

# Query all reviews and print the review text
print("All Reviews:")
reviews = session.query(Review).all()
for review in reviews:
    print(review.full_review())

print_separator()

# Query a specific restaurant's reviews
restaurant_name = "Your Restaurant Name"
restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()

if restaurant:
    print(f"Reviews for {restaurant_name}:")
    reviews = session.query(Review).filter_by(restaurant=restaurant).all()
    for review in reviews:
        print(review.full_review())
else:
    print(f"Restaurant with name '{restaurant_name}' not found.")

print_separator()

# Query a specific customer's reviews
customer_first_name = "John"
customer_last_name = "Doe"
customer = session.query(Customer).filter_by(first_name=customer_first_name, last_name=customer_last_name).first()

if customer:
    print(f"Reviews by {customer_first_name} {customer_last_name}:")
    reviews = session.query(Review).filter_by(customer=customer).all()
    for review in reviews:
        print(review.full_review())
else:
    print(f"Customer '{customer_first_name} {customer_last_name}' not found.")
