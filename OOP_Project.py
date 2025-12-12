database = { "name": [], "password": [], "balance": [] }
class BankAccount: 
    def __init__ (self, balance, password,name,isloggedin=False):
        self.balance =balance
        self.password = password
        self.name = name
        self.isloggedin = isloggedin
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        return self.balance
    def check_balance(self, password_for_checking_balance):
        if password_for_checking_balance != self.password:
            return "Invalid Password"
        return self.balance


print(database)
while True: 
    print ( ' select an option : ')
    print ( ' 1. create account ' )
    print ( ' 2. login ' )
    print ( ' 3. exit ' )
    option = int (input ( ' enter option number: ' ))
    if option == 1: 
        name = input (' enter your name:')
        password = int(input (' enter your password (numbers only):'))
        initial_balance = float(input (' enter initial deposit amount:'))
        new_account = BankAccount(name=name, password=password, balance=initial_balance)
        database['name'].append(name)
        database['password'].append(password)
        database['balance'].append(initial_balance)
        print(' account created successfully ')
    elif option == 2:
        name = input (' enter your name:')
        password = int(input (' enter your password (numbers only):'))
        if name in database['name']:
            index = database ['name'].index(name)
            password_in_db = database['password'][index]
            if password == password_in_db:
                print(' login successful ')
                account = BankAccount(name=name, password=password, balance=database['balance'][index], isloggedin=True)
                while account.isloggedin:
                    print ( ' select a transaction : ')
                    print ( ' 1. Deposit ' )
                    print ( ' 2. Withdraw ' )
                    print ( ' 3. Check Balance ' )
                    print ( ' 4. Logout ' )
                    transaction_option = int (input ( ' enter option number: ' ))
                    if transaction_option == 1:
                        amount = float(input(' enter amount to deposit: '))
                        new_balance = account.deposit(amount)
                        new_balance_index = database['name'].index(name)
                        database['balance'][new_balance_index] = new_balance
                        print(f' deposited {amount}. New balance is {new_balance} ')
                    elif transaction_option == 2:
                        amount = float(input(' enter amount to withdraw: '))
                        result = account.withdraw(amount)
                        if result == "Insufficient Balance":
                            print(result)
                        else:
                            new_balance_index = database['name'].index(name)
                            database['balance'][new_balance_index] = result
                            print(f' withdrew {amount}. New balance is {result} ')  
                    elif transaction_option == 3:
                        password_for_checking_balance = int(input(' enter your password to check balance: '))
                        balance_check = account.check_balance(password_for_checking_balance)
                        print(f' your balance is {balance_check} ')
                    elif transaction_option == 4:
                        account.isloggedin = False
                        print(' logged out successfully ')
            else:
                print(' invalid password ')
        else:
            print(' account not found ')
    elif option == 3:
        print(' exiting program ')
        break

print ( )
print ( ' final database state: ' )
print ( database ['name'], database [ 'balance'] )