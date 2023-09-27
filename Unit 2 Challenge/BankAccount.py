class BankAccoount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
   self.__account_number=account_number
   self.__account_holder_name=account_holder_name
   self.__account_balance=initial_balance
  def deposit(self,amount):
   if amount>0:
    self.__account_balance +=amount
    print("Deposited₹{}. New balance:₹{}".format(amount,self.__account_balance))
   else:
    print("Invaild Deposit amount")
  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance-=amount
      print("Withdrew ₹{}.New balance ₹{}".format(amount,self.__account_balance))
    else:
      print("Invaild Withdrew amount")
  def display_balance(self):
    print("Account Balance for {} (Account #{}:₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))

account=BankAccoount(account_number=45678321,account_holder_name="Sivaram",initial_balance=10000)
account.display_balance()
account.deposit(500.0)
account.withdraw(250.0)
account.display_balance()
    
  


  
