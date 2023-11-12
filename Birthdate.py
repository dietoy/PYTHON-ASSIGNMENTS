import datetime

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d')

current_date = datetime.datetime.now()
print(current_date)

age = current_date.year - birthdate.year

print("Your age is:", age, "years")