import math
from datetime import datetime

# 1.ask the dimensions
width = int(input("Enter the width of the tire in mm: "))
print("")
aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
print("")
diameter = int(input("Enter the diameter of the wheel in inches: "))
print("")

# 2.Calculate the volume
volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# 3.result rounded to two decimal places
print(f"The approximate volume is {volume:.2f} liters")

# 4.date (YYYY-MM-DD)
current_date_and_time = datetime.now()
date = f"{current_date_and_time:%Y-%m-%d}"


# 5.ask if the user wants to buy tires
buy = input("Would you like to buy tires with these dimensions? (yes/no): ").strip().lower()

if buy == "yes":
    print("")
    phone = input("Please enter your phone number: ").strip()
    name = input("Please enter your name: ").strip()
    city = input("Please enter your city: ").strip()
    with open("volumes.txt", "at") as file:
        print("")
        print(f"Customer phone: {phone}", file=file)
        print(f"Customer name: {name}", file=file)
        print(f"Customer city: {city}", file=file)
        print(f"{date}")
    print("Thank you! We will contact you soon.")
else:
    print("")
    print("Thank you for using the Tire Volume Calculator!")
    print(f"{date}")
