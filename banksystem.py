import sys
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def main():
  login()
def account():
  class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 

  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance)
  def dw():  
    s = Bank_Account()
    choicee=input("Do you want withdraw or  Deposit:") 
    if(choicee=="withdraw"):
      s.withdraw()
    elif(choicee=="deposit"):
      s.deposit()
      s.display() 
  dw()
  option=input("Do you want to continue withdraw or deposit (y/n):")
  if option=='y':
    dw()
  elif option=='n':
    con=input("Do you want to continue y/n:")
    if con=='y':
      login()
    elif con=='n':
      sys.exit 
   
   
def bank_system():
    print("deltails")
    def name_check(name):
        if(name.isalpha()):
            return 1
        else:
            print("The name you enter is not valid")
            name_check(input("Enter the name:"))
    def check_number(mobile):
        def isValid(s):
            Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
            return Pattern.match(mobile)
        if (isValid(mobile)):
            return 1
        else:
            print ("The number you enter is not valid ")
            check_number(input("Enter the acc number:"))        
    def check_email(email):
        if(re.search(regex,email)):
            return 1     
        else:
            print("The email ID you enter is not valid")
        check_email(input("Enter the mail ID:"))
    print("********BANK SYSTEM********")        
    name=input("Enter the name: ")
    name_check(name)
    mobile=input("Enter the acc number:")
    check_number(mobile)
    email=input("Enter the mail ID :")
    check_email(email)
    con=input("Do you want to continue y/n:")
    if con=='y':
        login()
    elif con=='n':
        sys.exit
def login():
    print("******Login Page********")
    choice=int(input(("1. Login \n2. withdraw&deposit \n3. Logout \nEnter your choice: ")))
    if choice == 1:
        bank_system()
    elif choice == 2:
        account()
    elif choice == 3:
        sys.exit
    else:
        print("You must only select either 1,2,3, or 4")
        print("Please try again")
main()
