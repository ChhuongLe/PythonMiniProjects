MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Description:
  # Make a coffee maker program that will ask the user what kind of hot drink they want (espresso, latte, cappuccino)
  # Other functions that can be added are a report function and an off function to exit the program
  # If a coffee drink is selected, first ask how much money they have in coins
  # Then determine if there are enough resources to produce the required coffee
    # If enough money and resources are available, then make the coffee
    # Otherwise output an error message

# TODO: implement a method that asks the user to insert their payment value in coins
# Should return a boolean to show that the process is valid or not
def processPayment(drink):
  total = 0

  numPennies = float(input('How many pennies?: '))
  numNickels = float(input('How many nickels?: '))
  numDimes = float(input('How many dimes?: '))
  numQuarters = float(input('How many quarters?: '))

  total = 0.01*numPennies + 0.05*numNickels + 0.10*numDimes + 0.25*numQuarters

  if drink['cost'] < total:
    print ('You input: $' + str(total))
    total = total - drink['cost']
    print('Your change is: $'+ str(total))
    return True
  elif drink['cost'] == total:
    print('You input: $' + str(total))
    return True
  # Base case, returns false if process fails
  print('Need more money, head to the nearest coin machine')
  return False

# TODO: implement a method that checks the resources available
def checkResources(orderIngredients):
  # Base case, return false if there is not enough ingredients
  return False

# TODO: implement a method that will make the coffee
def makeCoffee():
  return 'Still implementing'

# Initialize a boolean flag that will keep the program running
isOn = True

# While this boolean is still true, run the program
while(isOn):
  # Ask the user what kind of hot drink they want
  selection = input('What drink would you like today? (espresso/latte/cappuccino): ')
  selection = selection.lower()
  # Determine the selection
  # If they input off, the jump out of the loop
  if (selection == 'off'):
    isOn = False
    print('Coffee machine turning off')
  # If the user wants a report of the remaining resources
  elif (selection == 'report'):
    # Print the current resources
    print(resources)
  # If the user selects a drink, check if the drink is present
  elif selection in MENU.keys():
    # if it is, ask the user to input the amount in coins they are going to pay
    if processPayment(MENU[selection]):
      # if the processPayment method returns true, check if there are enough resources present
      if checkResources(selection['ingredients']):
        # if checkResources returns true, then make the coffee
        makeCoffee()
  else:
    print('Drink not found')