Amount = 0 
balance = 10000
password = 1234 
print ( ' thank you for choosing ahly bank \n ' ) 
user_pin = int ( input ( ' Enter your pin \n: ' ) )
while user_pin != password :
    print ( ' Invalid pin , please try again \n ' )
    user_pin = int ( input ( ' Enter your pin :\n ' ) )
    if user_pin == password :
        print ( ' Pin accepted , you can proceed \n' )
        break
print ( ' Enter which transaction you want to perform\n ' )
print ( ' 1. Deposit                          2. Withdraw\n ')
print ( ' 3. Check Balance                    4. Exit \n' )
chosen_option = int ( input ( ' Choose 1, 2, 3 or 4 : \n' ) )       
while True : 
    if chosen_option not in [ 1, 2, 3, 4 ] :
        print ( ' Invalid option , please choose a valid option ' )
        chosen_option = int ( input ( ' Choose 1, 2, 3 or 4 :  ' ) )
    if chosen_option == 1 : 
        print ( ' Your current balance is : ' , balance )
        Amount = float ( input ( ' Please Enter the amount you want to deposit /n '))
        balance = balance + Amount
        print ( ' You have successfully deposited :  ' , Amount )
        print ( ' Your new balance is :  ' , balance )
        print ( ' Thank you for using our ATM service  ' )
        break
    elif chosen_option == 2 : 
        print ( ' Your current balance is :  ' , balance )
        Amount = float ( input ( ' Please Enter the amount you want to withdraw  '))
        while Amount > balance :
            print ( ' Insufficient Balance ' )
            print ( ' Enter a valid amount to withdraw Within your balance ' )
            Amount = float ( input ( ' Please Enter the amount you want to withdraw  '))     
        else :
            balance = abs ( balance - Amount )
            print ( ' You have successfully withdrawn : ' , Amount )
            print ( ' Your new balance is : ' , balance )
            print ( ' Thank you for using our ATM service ' )
        break
    elif chosen_option == 3 :
        print ( ' Your current balance is : ' , balance )
        print ( ' Thank you for using our ATM service ' )
        break
    elif chosen_option == 4 :
        print ( ' Thank you for using our ATM service ' )
        break