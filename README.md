# Phase 3 Week 3 Code Challenge (Restaurant with SQLAlchemy)

[![License](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## Project Description
### Object Relations Code Challenge - Restaurants
For this assignment, we'll be working with a restaurant review domain.

We have three models: `Restaurant`, `Review`, and `Customer`.

 

For our purposes, a `Restaurant` has many `Review`s, a `Customer` has many

`Review`s, and a `Review` belongs to a `Restaurant` and to a `Customer`.

`Restaurant` - `Customer` is a many to many relationship.

 

### Topics
- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- Lists and List Methods

### Project Deliverables
You need to have migrations and models for the initial `Restaurant` and `Customer` models, and seed data for some `Restaurant`s and `Customer`s.

The schema currently looks like this: 

__restaurant's table__
| Column   | Type     |
| -------- | :------: |
| name     | String   |
| price    | Integer  |

__customer's table__
| Column      | Type     |
| --------    | :------: |
| first_name  | String   |
| last_name   | String   |



You will need to create the migration for the `reviews` table using the attributes specified in the deliverables below.
Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

#### Customer
- `Customer __init__()`
  - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
- `Customer given_name()`
  - returns the customer's given name
  - should be able to change after the customer is created
- `Customer family_name()`
  - returns the customer's family name
  - should be able to change after the customer is created
- `Customer full_name()`
  - returns the full name of the customer, with the given name and the family name concatenated, Western style.
- `Customer all()`
  - returns **all** of the customer instances

#### Restaurant
- `Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string
- `Restaurant name()`
  - returns the restaurant's name
  - should not be able to change after the restaurant is created

#### Review
- `Review __init__()`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review rating()`
  - returns the rating for a restaurant.
- `Review all()`
  - returns all of the reviews

### Object Relationship Methods

#### Review
- `Review customer()`
  - should return the `Customer` instance for this review
- `Review restaurant()`
  - should return the `Restaurant` instance for this review

#### Restaurant
- `Restaurant reviews()`
  - returns a collection of all the reviews for the `Restaurant`
- `Restaurant customers()`
  - returns a collection of all the customers who reviewed the `Restaurant`

#### Customer
- `Customer reviews()`
  - should return a collection of all the reviews that the `Customer` has left
- `Customer restaurants()`
  - should return a collection of all the restaurants that the `Customer` has reviewed

Check that these methods work before proceeding. For example, you should be able to call `session.query(Customer).first().restaurants` and see a list of the restaurants for the first customer in the database based on your seed data; and `session.query(Review).first().customer` should return the customer for the first review in the database.

### Aggregate and Association Methods

#### Customer
- `Customer full_name()`
  - returns the full name of the customer, with the first name and the last name concatenated, Western style.
- `Customer favorite_restaurant()`
  - returns the restaurant instance that has the highest star rating from this customer
- `Customer add_review(restaurant, rating)`
  - given a `restaurant` (an instance of the `Restaurant` class) and a rating
  - creates a new review for the restaurant with the given `restaurant_id`
- `Customer delete_reviews(restaurant)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and
  - removes **all** their reviews for this restaurant
  - you will have to delete rows from the `reviews` table to get this to work!

### Project Setup
Ensure that you have Python3 installed on your machine to run the solutions

1. Clone this repository to your local machine.
```sh
git@github.com:Noelle-Wavinya-Maingi/Restaurant-with-sqlAlchemy.git
```

2. Open a terminal or command prompt.

3. Navigate to the directory containing the repository.

4. Run this on your terminal:
     ```sh 
     python3 main.py 
     ```

6. The solution will execute and display the results on the terminal.

#### Review
- `Review full_review()`
  - should return a string formatted as follows:
Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

#### Restaurant
- `Restaurant fanciest(), this method should be a class method`
  - returns _one_ restaurant instance for the restaurant that has the highest price
- `Restaurant all_reviews()`
  - should return a list of strings with all the reviews for this restaurant
  - formatted as follows:
  [

 __"Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",__

 __"Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",__

]

### Author
The author of the code challenge solution is [Noelle Maingi.](https://github.com/Noelle-Wavinya-Maingi)
