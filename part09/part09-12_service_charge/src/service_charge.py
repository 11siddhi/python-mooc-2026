# WRITE YOUR SOLUTION HERE:
class BankAccount:
  def __init__(self, owner: str, acc_num: str, balance: float):
    self.__owner = owner 
    self.__acc_num = acc_num
    self.__balance = balance
  
  def deposit(self, amount: float):
    if amount > 0:
      self.__balance += amount
      self.__service_charge()
    else:
      return ValueError("Amount should be greater the zero")
  
  def withdraw(self, amount: float):
    if self.__balance >= amount:
      self.__balance -= amount
      self.__service_charge()
    else:
      return ValueError("Not enough money to withdraw")
  
  @property
  def balance(self):
    return self.__balance
  
  def __service_charge(self):
    self.__balance -= self.__balance * 0.01

if __name__ == "__main__":
  account = BankAccount("Randy Riches", "12345-6789", 1000)
  account.withdraw(1000)
  print(account.balance)
  # account.deposit(100)
  # print(account.balance)