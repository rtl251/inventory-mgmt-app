# Inventory Management App
A command-line Python application which allows the user to manage an inventory of products. Performs all product "CRUD" operations (i.e. "List", "Show", "Create", "Update", and "Destroy").

Uses a CSV file datastore.

Installation
First, "fork" this upstream repository under your own control.

Then download your forked version of this repository using the GitHub.com online interface or the Git command-line interface. If you are using command-line Git, you can download it by "cloning" it:

git clone https://github.com/YOUR_USERNAME/inventory-mgmt-app-py.git
After downloading your forked repository, navigate into its root directory:

cd path/to/inventory-mgmt-app-py/
NOTE: all commands in this document assume you are running them from this root directory.

#Setup
Before you run this application for the first time (or anytime you want to reset the database), reset the database by populating it with the default products:

For Homebrew-installed Python 3.x on Mac OS:
python3 products_app/reset.py

All others:
python products_app/reset.py

#Usage
Run the application:

For Homebrew-installed Python 3.x on Mac OS:
python3 products_app/app.py

All others:
python products_app/app.py

# License
Please pay attention to the license terms, located here: https://github.com/prof-rossetti/inventory-mgmt-app-py/blob/master/LICENSE.md
