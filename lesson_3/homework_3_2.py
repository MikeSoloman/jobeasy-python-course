# Enter a number between 1 and 20, save this value to number variable.
# If number is greater than 0 and less than or equal to 7, save the number * 10 to result_1.
# If number is  greater than 7 and less than or equal to 15, save the result of floor division of the number divided by
# 3 to result_1 variable
# If number is  greater than 15 and less than or equal to 20, save the number raised to the power 3 to result_1
# Else save the text "Wrong value" to result_1

from random import randint
number = 14
changed_num = 0
result_1 = None
if number:
    if 15 < number <= 20:
        changed_number = number ** 3
        print(f"Your original number was {number} and it's {changed_number} now")
    elif 7 < number <= 15:
        changed_number = number // 3
        print(f"Your original number was {number} and it's {changed_number} now")
    else:
        changed_number = number * 10
        print(f"Your original number was {number} and it's {changed_number} now")
else:
    pass

# Enter two numbers between 1 and 10, save this values to number_1 variable and number_2 variables.
# If number_1 and number_2 are greater than 0 and less than or equal to 5 save in the product of their multiplication
# to result_2
# If one of the variables (number_1 or number_2) is greater than 5 and less than or equal to 10, but the other isn't,
# then save the sum of the two numbers to result_2
# If both numbers are greater than 5 and less than or equal to 10, multiply their sum by 3 and save it to result_2
# Else save the text "Wrong values, try again" to result_2

number_1 = 5
number_2 = 7
result_2 = None

if 0 < number_1 <= 5 and 0 < number_2<= 5:
    result_2 = number_1 * number_2
    print(f"Your num1 was {number_1} and your num2 was {number_2} which resulted in {result_2}")
elif 5 < number_1 <=10 or 5< number_2 <= 10:
    result_2 = number_1 + number_2
    print(f"Your num1 was {number_1} and your num2 was {number_2} which resulted in {result_2}")
elif 5 < number_1 <= 10 and 5< number_2 <= 10:
    result_2 = (number_1 + number_2) * 3
    print(f"Your num1 was {number_1} and your num2 was {number_2} which resulted in {result_2}")
else:
    result_2 = "Wrong values"
    print(result_2)


# Enter your first name and save it to first_name variable,
# then Enter last name and save it to last_name
# If first_name or last_name are shorter than 6 characters,
# save a full name (with a space between) to result_3
# Else save first_name to result_3 as many times as length of last_name value

first_name = "Mikeeeee"
last_name = "SUHFUHFHU"
result_3 = first_name + " " + last_name if len(first_name) < 6 or len(last_name) < 6 else (first_name + " ") * len(last_name)
print(result_3)


# Enter a random number. Save this value to random_number variable
# If this number is less 10 or greater than 99, save the text "Please, put in a number between 10 and 99" to result_4
# If a number doesn't meet the first condition, find the remainder of random_value divided by 2.
# If it is 0, save the text "Even number" to result_4 , else save the message "Odd number"

random_number = randint(1, 150)
result_4 = None
if random_number:
    if random_number < 10 or random_number > 99:
        print(f"your number was {random_number}")
        result_4 = "Please, put in a number between 10 and 99"
        print(result_4)
    elif random_number % 2 == 0:
        print(f"your number was {random_number}")
        result_4 = "even"
        print(result_4)
    elif random_number % 2 != 0:
        print(f"your number was {random_number}")
        result_4 = "odd"
        print(result_4)
else:
    pass
