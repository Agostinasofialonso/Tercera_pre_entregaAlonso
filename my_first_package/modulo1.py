import hashlib

import string

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
    global users
    users = {}
    if username in users:
      print("Username already exists.")
      return

    # Validate the password
    if not self.is_valid_password(password):
      print("Invalid password.")
      return

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Add the user to the database
    users[username] = hashed_password

    # Write the users to a file
    with open("users.txt", "a") as f:
      f.write(username + ":" + hashed_password + "\n")

    # Print a success message
    print("User registered successfully.")

  # A method to display all customers
  def display_all(self):
    # Read the users from a file
    with open("users.txt", "r") as f:
      users = {}
      for line in f:
        username, hashed_password = line.split(":")
        users[username] = hashed_password

    # Print a list of all users
    for username, hashed_password in users.items():
      print(username, hashed_password)

  # A method to login a customer
  def login(self, username):
    # Get the password from the user
    password = input("Enter your password: ")

    # Check if the username and password match
    try:
      if username in users and hashlib.sha256(password.encode()).hexdigest() == users[username]:
        print("Login successful.")
      else:
        raise ValueError("Invalid username or password.")
    except ValueError:
      print("Login failed.")






