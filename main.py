class BankAccount: 
  """Bank Account protected by a pin number."""

  def __init__(self, pin): 
      """Initial account balance is 0 and pin is 'pin'."""
      self.__pin = pin
      self.balance = 0

  def deposit(self, pin, amount): 
      """Increment account balance by amount and return new balance."""
      if pin:
        self.balance += amount
        return self.balance
      else:
        return "Incorrect pin"

  def withdraw(self, pin, amount): 
      """Decrement account balance by amount and return amount withdrawn."""
      if amount > self.balance:
        return "Insufficient funds"
      if pin:
          self.balance -= amount
          return self.balance
      else:
          return "Incorrect pin"

  def get_balance(self, pin): 
      """Return account balance."""
      if pin:
          return self.balance
      else:
          return "Incorrect pin"

  def change_pin(self, oldpin, newpin): 
      """Change pin from oldpin to newpin."""
      if oldpin == self.__pin:
          self.__pin = newpin 
          return self.__pin
      else:
          raise ValueError("Old pin is incorrect.")



class SavingsAccount(BankAccount):
  """I removed the pin functionality from the savings account class because it is a 
  subclass of the bank account class.
  The user does not need a pin to access
  the savings account
  """
  def __init__(self, pin, interest_rate):
      super().__init__(pin)
      self.balance = 0
      self.interest_rate = interest_rate

  def add_interest(self ):
      """Add interest amount to savings balance."""
      self.balance += (self.balance * self.interest_rate)
      return self.balance



class FeeSavingsAccount(SavingsAccount):
    """charges a fee every time you withdraw money."""
    def __init__(self, pin, interest_rate, withdrawal_fee):
      super().__init__(pin, interest_rate)
      self.withdrawal_fee = withdrawal_fee


    def fee_withdraw(self, amount): 
      """Decrement savings balance by the fee and amount and return amount withdrawn."""
      if amount > self.balance:
        return "Insufficient funds"

      else:
          self.balance -= self.withdrawal_fee
          self.balance -= amount
          return self.balance

 
result = BankAccount(1234)

# print(result.deposit(1234, 200.50))
# print(result.withdraw(1234, 500))
# print(result.get_balance(1234))
# print(result.change_pin(1234, 4321))


savings = SavingsAccount(1234, 0.05)
print(savings.deposit(1234, 100))
print(savings.add_interest())

fee_savings = FeeSavingsAccount(1234, 0.05, 2)
print(fee_savings.deposit(1234, 100))
print(fee_savings.fee_withdraw(50))