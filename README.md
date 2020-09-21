# Guitar Store— CS50x Final Project

This project is my final project submisson for Harvard CS50x. It was a group project, built by Nathan Kawaller, Natalie Sterling and Michael Kramer. It is an online store (a guitar store in this case), and the main purposes of the project were to practice our CRUD skills, practice database design, and get comfortable using the Django Rest Framework.

## URL

```
https://github.com/nkawaller/store_app
https://github.com/nmsterling/store_app (fork)
```

## Project Specifications

### Features

* Landing page/login/logout
  * When the user arrives at your site and they’re not logged in, they should arrive at a landing page.  The page should have a header with a login link.
  * Once they’re logged in, they should be redirected to a product page
  * If they’re logged in, there should be a link to logout.  You should also include a link in the header for them to go to their user profile (see below).
* Search
  * Give users the ability to search for a product by name.  When they search, they are brought to a new page that lists all the products that met the search term.
* Product list/Reviews
  * There should a list of products. List page might include a short description, a thumbnail image, and a price.
  * Give users the ability to add a product review and have it displayed on the page along with their username.
* Cart
  * Products can be added to a cart with a quantity.  The quantity of a product added to the cart can be no more than is currently in stock.  Note that the stock quantity only goes down upon purchase, not when customers add a product to their cart.  For this reason, they need to be notified if they try to checkout and there are no longer enough quantity of a product.
  * User can update the quantity of a product in their cart as well as remove from their cart.
  * Customers can checkout.  Checkout includes a confirmation screen with the products they will be ordering and the address it will be shipped to (see user profile).  Once they confirm, an order history should be created and the cart’s contents should be cleared.
* User types
  * There should be two types of users, a regular user and a preferred customer.  A preferred customer gets 10% off their orders.  Users can select to be preferred user in their user profile.  If a user is preferred, the products they see should indicate the list price as well as their preferred price.
* Products
   * List a name, description, price, and picture of the product
* User Profile
  * Order history
  * Shipping address
  * Preferred status or not
* Tests
  * All features should have at least one unit test
* Front-End filtering/ordering
  * On your product list page/search results page give the user the ability to search through the products on the page and order by name and price.

### Workflow

* Kanban Board (Trello)
  * Create a ticket for each feature
  * For each ticket, work on a new branch
  * Once completed, create a pull request
  * Have the request reviewed by a team member
  * If all the tests pass, merge branch into master

## Built With

* Django
* Django Rest Framework
* Vue
* Python
* JavaScript
* HTML
* CSS
* Bootstrap
* Material Design for Bootstrap
