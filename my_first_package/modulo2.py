import random
import string

# Define a class to represent a customer
class Customer:

  # The constructor for the Customer class
  def __init__(self, name, email, address, phone):
    self.name = name
    self.email = email
    self.address = address
    self.phone = phone

  # A method to validate the password
  def is_valid_password(self, password):
    # The password must be at least 8 characters long
    if len(password) < 8:
      return False

    # The password must contain at least one uppercase letter
    if not any(c.isupper() for c in password):
      return False

    # The password must contain at least one lowercase letter
    if not any(c.islower() for c in password):
      return False

    # The password must contain at least one digit
    if not any(c.isdigit() for c in password):
      return False

    # The password must contain at least one special character
    if not any(c in string.punctuation for c in password):
      return False

    return True

  # A method to register a customer
  def register(self):
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username already exists in the database
    if username in users:
      print("Username already exists.")
      return

    # Validate the password
    if not self.is_valid_password(password):
      print("Invalid password.")
      return

    # Add the user to the database
    users[username] = password

    # Write the users to a file
    with open("users.txt", "a") as f:
      f.write(username + ":" + password + "\n")

    # Print a success message
    print("User registered successfully.")

  # A method to display all customers
  def display_all(self):
    # Read the users from a file
    with open("users.txt", "r") as f:
      users = {}
      for line in f:
        username, password = line.split(":")
        users[username] = password

    # Print a list of all users
    for username, password in users.items():
      print(username, password)

  # A method to login a customer
  def login(self):
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match
    if username in users and users[username] == password:
      print("Login successful.")
    else:
      print("Login failed.")

# Create a dictionary to store users
users = {}

# Register a few customers
customer1 = Customer("Agostina Alonso", "agosalonso@gmail.com", "123 Liniers", "261-456-7890")
customer1.register()
customer2 = Customer("Sofia Heredia", "sofiheredia9@gmail.com", "456 Vegas", "261-666-7777")
customer2.register()

# Display all customers
customer1.display_all()

# Login a customer
customer1.login()

# Try to login with an incorrect password
customer2.login()