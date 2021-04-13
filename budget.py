# Budget App
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

def init():
  print("These are the categories available:")
  print("1. Food")
  print("2. Clothing")
  print("3. Housing")
  chooseCategory = int(input("Select a category: \n"))
  if (chooseCategory == 1):
    foodBudget = Budget(chooseCategory - 1)
    foodBudget.operations()
  elif (chooseCategory == 2):
    clothingBudget = Budget(chooseCategory - 1)
    clothingBudget.operations()
  elif (chooseCategory == 3):
    housingBudget = Budget(chooseCategory - 1)
    housingBudget.operations()
  else:
    print("You selected the wrong option, try again")
    init()
    
  return chooseCategory

class Budget:
  """
  This is a Budget class
  """
  balance = [0, 0 , 0]
  
  def __init__(self, category):
      self.category = category
    
  def deposit(self):
    depositAmount = int(input("How much will you like to deposit? \n"))
    Budget.balance[self.category] += depositAmount
  
  def withdrawal(self):
    withdrawAmount = int(input("How much will you like to withdraw? \n"))
    Budget.balance[self.category] -= withdrawAmount
  
  def transfer(self):
    if (self.category == 0):
      print("\nThese are the categories available:")
      print("2. Clothing")
      print("3. Housing")
      transferCategory = int(input("\nWhich category will you like to transfer to? \n"))
      if (transferCategory == 2 or transferCategory == 3):
        transferAmount = int(input("How much will you like to transfer? \n"))
        Budget.balance[self.category] -= transferAmount
        Budget.balance[transferCategory - 1] += transferAmount
         
    elif (self.category == 1):
      print("\nThese are the categories available:")
      print("1. Food")
      print("3. Housing")
      transferCategory = int(input("\nWhich category will you like to transfer to? \n"))
      if (transferCategory == 1 or transferCategory == 3):
        transferAmount = int(input("How much will you like to transfer? \n"))
        Budget.balance[self.category] -= transferAmount
        Budget.balance[transferCategory - 1] += transferAmount
        
    elif (self.category == 2):
      print("\nThese are the categories available:")
      print("1. Food")
      print("2. Clothing")
      transferCategory = int(input("\nWhich category will you like to transfer to? \n"))
      if (transferCategory == 1 or transferCategory == 2):
        transferAmount = int(input("How much will you like to transfer? \n"))
        Budget.balance[self.category] -= transferAmount
        Budget.balance[transferCategory - 1] += transferAmount
  
  def budgetBalance(self):
    print(f"Your remaining balance is: {Budget.balance[self.category]}")
    
  def operations(self):
    self.deposit()
    self.withdrawal()
    self.transfer()
    self.budgetBalance()
    
init()