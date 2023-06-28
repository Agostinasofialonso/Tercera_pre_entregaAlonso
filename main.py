# main.py

from my_first_package.modulo1 import Customer

users = {}

def main():
  # Register a few customers
  customer1 = Customer("Agostina Alonso", "agosalonso@gmail.com", "123 Liniers", "261-456-7890")
  customer1.register()
  customer2 = Customer("Sofia Heredia", "sofiheredia9@gmail.com", "456 Vegas", "261-666-7777")
  customer2.register()

  # Display all customers
  customer1.display_all()

  # Try to login with an incorrect password
  customer2.login("sofiaheredia123")

if __name__ == "__main__":
  main()
