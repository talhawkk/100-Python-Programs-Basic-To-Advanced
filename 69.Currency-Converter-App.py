from currency_converter import CurrencyConverter
a=CurrencyConverter()
frm=input("from which currency you want to convert : ").upper()
into=input("in which currency you want to convert : ").upper()
amount=int(input("Enter amount : "))
print(a.convert(amount,frm,into))

