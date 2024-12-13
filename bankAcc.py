class BankAccount:
    def __init__(self): #initial values
        self.balance = 0           
        self.acc_deposit = 0      
        self.withdrawal = 0  
    def deposit(self, amount):
        self.balance += amount
        self.acc_deposit = amount  # deposit amount
    def withdraw(self, amount):
        if amount <= self.balance:  # sufficient funds for withdrawal
            self.balance -= amount
            self.withdrawal = amount  # withdrawal amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        print("Balance after deposit:", self.acc_deposit)
        print("Balance after withdrawal:", self.balance)
account = BankAccount() 
account.deposit(1000)     
account.withdraw(200)     
account.get_balance()     