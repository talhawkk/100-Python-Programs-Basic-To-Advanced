import phonenumbers
from phonenumbers import carrier,geocoder,timezone
number=input("Enter Your Phone Number with +...: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,'en')
region=geocoder.description_for_number(phone,'en')
print(phone)
print(time)
print(car)
print(region)