class Bank:
    Account = 10327467182
    balance = 5580

    def credit(self,amount):
        Bank.balance= Bank.balance+amount
        print(f"amount has been credited\nNow your current balance is {Bank.balance}")

    def debit(self,amount):
        if amount<Bank.balance:
            Bank.balance= Bank.balance-amount
            print(f"amount has been credited\nNow your current balance is {Bank.balance}")
        else: 
            print("insufficient balance !!!!")
    
    def show(self):
        print(f"Account number : {Bank.Account}\n Current Balance : {Bank.balance}")

a1=Bank()
amount=int(input("enter amount : "))
x=int(input(f"Account number = {a1.Account} \nCurrent Balance = {a1.balance}\nIF you want to credit press 1 or if you want to debit press 2 : "))
if x==1:
    a1.credit(amount)
elif x==2:
    a1.debit(amount)
else:
    print("enter correct input")