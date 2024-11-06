def length_conversion():
    print("\nLength Conversion:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Miles to Kilometers")
    print("4. Kilometers to Miles")
    choice = int(input("Enter choice (1-4): "))
    
    if choice == 1:
        meters = float(input("Enter meters: "))
        print(f"{meters} meters is {meters / 1000} kilometers.")
    elif choice == 2:
        kilometers = float(input("Enter kilometers: "))
        print(f"{kilometers} kilometers is {kilometers * 1000} meters.")
    elif choice == 3:
        miles = float(input("Enter miles: "))
        print(f"{miles} miles is {miles * 1.60934} kilometers.")
    elif choice == 4:
        kilometers = float(input("Enter kilometers: "))
        print(f"{kilometers} kilometers is {kilometers / 1.60934} miles.")
    else:
        print("Invalid choice.")


def weight_conversion():
    print("\nWeight Conversion:")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Grams")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")
    choice = int(input("Enter choice (1-4): "))
    
    if choice == 1:
        grams = float(input("Enter grams: "))
        print(f"{grams} grams is {grams / 1000} kilograms.")
    elif choice == 2:
        kilograms = float(input("Enter kilograms: "))
        print(f"{kilograms} kilograms is {kilograms * 1000} grams.")
    elif choice == 3:
        pounds = float(input("Enter pounds: "))
        print(f"{pounds} pounds is {pounds * 0.453592} kilograms.")
    elif choice == 4:
        kilograms = float(input("Enter kilograms: "))
        print(f"{kilograms} kilograms is {kilograms / 0.453592} pounds.")
    else:
        print("Invalid choice.")


def temperature_conversion():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = int(input("Enter choice (1-4): "))
    
    if choice == 1:
        celsius = float(input("Enter Celsius: "))
        print(f"{celsius}°C is {(celsius * 9/5) + 32}°F.")
    elif choice == 2:
        fahrenheit = float(input("Enter Fahrenheit: "))
        print(f"{fahrenheit}°F is {(fahrenheit - 32) * 5/9}°C.")
    elif choice == 3:
        celsius = float(input("Enter Celsius: "))
        print(f"{celsius}°C is {celsius + 273.15}K.")
    elif choice == 4:
        kelvin = float(input("Enter Kelvin: "))
        print(f"{kelvin}K is {kelvin - 273.15}°C.")
    else:
        print("Invalid choice.")


def volume_conversion():
    print("\nVolume Conversion:")
    print("1. Liters to Milliliters")
    print("2. Milliliters to Liters")
    print("3. Gallons to Liters")
    print("4. Liters to Gallons")
    choice = int(input("Enter choice (1-4): "))
    
    if choice == 1:
        liters = float(input("Enter liters: "))
        print(f"{liters} liters is {liters * 1000} milliliters.")
    elif choice == 2:
        milliliters = float(input("Enter milliliters: "))
        print(f"{milliliters} milliliters is {milliliters / 1000} liters.")
    elif choice == 3:
        gallons = float(input("Enter gallons: "))
        print(f"{gallons} gallons is {gallons * 3.78541} liters.")
    elif choice == 4:
        liters = float(input("Enter liters: "))
        print(f"{liters} liters is {liters / 3.78541} gallons.")
    else:
        print("Invalid choice.")


def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Choose the type of conversion:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Volume")
    choice = int(input("Enter choice (1-4): "))
    
    if choice == 1:
        length_conversion()
    elif choice == 2:
        weight_conversion()
    elif choice == 3:
        temperature_conversion()
    elif choice == 4:
        volume_conversion()
    else:
        print("Invalid choice. Please select a valid option (1-4).")


if __name__ == "__main__":
    unit_converter()
