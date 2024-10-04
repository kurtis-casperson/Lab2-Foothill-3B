# Description

This is my lab 2 assignment. This lab focused on learning about inheritance and mutation of data and methods.

# Steps to Follow

Create a BankAccount class.
As you implement your BankAccount class, you should think about the following:

What should be stored within the BankAccount class? That is, what are its instance variables?
What should happen if the wrong pin is provided for any of the methods (other than **init**, which is setting the initial pin)?
What should happen if you try to withdraw more than is in the account?
Does your bank account behave as you expect? Try depositing and/or withdrawing change, instead of whole dollar amounts. Do you want your real bank account to behave this way?

1. Create a SavingsAccount class that behaves just like a BankAccount, but also has an interest rate and a method that increases the balance by the appropriate amount of interest.

2. Create a FeeSavingsAccount class that behaves just like a SavingsAccount but also charges a fee every time you withdraw money. The fee should be set in the constructor and deducted before each withdrawal.
