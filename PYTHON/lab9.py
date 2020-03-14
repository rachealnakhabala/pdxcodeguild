'''
"ft": "0.3048 m",
"mi": "1609.34 m",
"m": "1 m",
"km": "1000 m",
1 yard is 0.9144 m,
1 inch is 0.0254 m,'''

units = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yard": 0.9144,
    "in": 0.0254,
}

while True:
    distance = float(input("Enter your distance:"))
    unit = input("Enter the unit:")

    while unit not in units:
        unit = input(f"Enter the unit:{units.keys()}\n")

    meters = distance * units[unit]


    meters = round(meters, 3)
    print(f"{distance} {unit} is {meters}m")


    answer = input("would you like to add another unit?")

    if answer == "yes":
        unit = input("Enter the unit")
        conversion = float(input("Enter the the conversion above: "))
        units[unit]= conversion
    else:
        print("thank you:)")
        break 