# Project 3:Pizza

Web Programming with Python and JavaScript

The project is a pizza ordering site for a fictional restaurant Cheesilicious. Users can register, login and logout of the site. Once logged in, they can choose from the wide range of items in the menu, customise them by adding toppings, choose the size and add it to their cart. Multiple items can be added to the cart which are saved even if the user logs out. The user can then proceed to checkout and place their order after reviewing it. Also, an item can be deleted from the cart before it is checked out. They can then view the status of their order and all past orders. Site administrators can use django admin to add and delete items to the menu. Also, a page is provided where they can view all orders and mark the status of orders as complete.

Personal Touch: Allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders. Also, allowing users to delete items placed in the cart before their order is placed.

Files included:
In templates folder:
base.html-Contains basic layout for all html pages
index.html-Show the menu of categories available, each linked to detailed menu
signup.html-Allows user to register
login.html-Allows registered user to login using login form
list.html-Provide detailed menu
checkout.html-Provide view of items in the cart and option to place order
see_order_status.html-Allow users to see theirs placed orders and their statuses
curr_orders.html-Page only accessible by site admins. Shows all placed orders and allows to mark an order as complete
contact.html-Basic info of the shop
faq.html-Basic info regarding pizzas and what constitutes a special pizza
home.html-Basic info of the shop

In static folder:
base.css - Contains the styling for all pages
Images folder contains all the images used.

views.py contains all function definitions for urls
orders/urls.py-Contains urls of all pages made
models.py-Models for managing the databases
admin.py-For registering the models