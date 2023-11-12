temperature = float(input("Enter the temperature: "))
conversion_direction = input('Enter the conversion direction ("C TO F" or "F TO C") :  ')

if conversion_direction == "C TO F":
    fahrenheit = (temperature * 9 / 5) + 32
    print(f"{temperature}°C is equal to {fahrenheit}°F")

elif conversion_direction == "F TO C":
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius}°C")

else:
    print(input("Invalid conversion direction. Do well to enter 'C to F' or 'F to C': "))
print('That is your answer')
