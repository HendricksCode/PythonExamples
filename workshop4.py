class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password 

class BankUser(User):
    def __init__(self, name, pin, password):
        self.balance = 0
        super().__init__(name, pin, password)

    def show_balance(self):
        print(f"{self.name} has a balance of: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, transfer_amount, recp_user):
        ask_for_pin = int(input(f"Hi {self.name} Please type your PIN: "))
        if ask_for_pin == self.pin:
            self.withdraw(transfer_amount)
            recp_user.deposit(transfer_amount)
            return True
        else:
            print("Incorrect PIN")
            return False
    
    def request_money(self, request_amount, recp_user):
        ask_for_pin = int(input(f"Please type {recp_user.name}'s PIN: "))
        ask_for_password = input(f"Hi {self.name} Please type your PASSWORD: ")
        if ask_for_pin == recp_user.pin and ask_for_password == self.password: 
            recp_user.withdraw(request_amount)
            self.deposit(request_amount)
            return True
        else:
            return False


# ----Driver Code for Task 1----
# user1 = User("Keith", 1234, "weakPassword")
# print(user1.name, user1.pin, user1.password)

# ----Driver Code for Task 2----
# user1 = User("Keith", 1234, "weakPassword")
# print(user1.name, user1.pin, user1.password)

# ----Driver Code for Task 3----
# bank_user1 = BankUser("Bob", 4321, "strongPassword")
# print(bank_user1.name, bank_user1.pin, bank_user1.password, bank_user1.balance)

# ----Driver Code for Task 4----
# bank_user1 = BankUser("Bob", 4321, "strongPassword")
# bank_user1.show_balance()
# bank_user1.deposit(50)
# bank_user1.show_balance()
# bank_user1.withdraw(25)
# bank_user1.show_balance()

# ----Driver Code for Task 5----
# bank_user1 = BankUser("Bob", 4321, "strongPassword")
# bank_user2 = BankUser("Keith", 1234, "weakPassword")
# bank_user2.deposit(5000)
# bank_user2.show_balance()
# bank_user1.show_balance()
# bank_user2.transfer_money(500, bank_user1)
# bank_user1.show_balance()
# bank_user2.show_balance()
# bank_user2.request_money(1000, bank_user1)
# bank_user1.show_balance()
# bank_user2.show_balance()