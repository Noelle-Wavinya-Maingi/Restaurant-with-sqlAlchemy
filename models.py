from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Create a declarative base
Base = declarative_base()

# Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurant.db')  
Session = sessionmaker(bind=engine)
session = Session()

# Define the Review model
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

    # Define relationships with Customer and Restaurant
    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, star_rating={self.star_rating})>"

    # Define a method to get the full review text
    def full_review(self):
        restaurant_name = self.restaurant.name if self.restaurant else "Unknown Restaurant"
        customer_name = self.customer.full_name() if self.customer else "Unknown Customer"
        return f"Review for {restaurant_name} by {customer_name}: {self.star_rating} stars"
    
    # Object relationship methods
    def customer_name(self):
        return self.customer.full_name()

    def restaurant_name(self):
        return self.restaurant.name

# Define the Customer model
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define relationship with Review
    reviews = relationship("Review", back_populates="customer")

    def __repr__(self):
        return f"<Customer(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')>"

    # Define a method to get the full name of the customer
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Object relationship methods
    def customer_reviews(self):
        return self.reviews

    def reviewed_restaurants(self):
        return session.query(Restaurant).distinct().join(Review).filter(Review.customer == self).all()
    
    def favorite_restaurant(self):
        max_rating = 0
        favorite = None
        for review in self.reviews:
            if review.star_rating > max_rating:
                max_rating = review.star_rating
                favorite = review.restaurant
        return favorite

    def add_review(self, restaurant, rating):
        review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(review)
        session.commit()
        return review

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

# Define the Restaurant model
class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define relationship with Review
    reviews = relationship("Review", back_populates="restaurant")

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name='{self.name}', price={self.price})>"

    # Object relationship methods
    def restaurant_reviews(self):
        return self.reviews

    def reviewing_customers(self):
        return session.query(Customer).distinct().join(Review).filter(Review.restaurant == self).all()
    
    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars" for review in self.reviews]

# Create the tables in the database
Base.metadata.create_all(engine)
