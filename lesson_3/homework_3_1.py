# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.
from random import randint
first_number = randint(0, 20)
second_number = randint(0, 20)
result_1 = first_number if first_number > second_number else second_number
print(result_1)

# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.
number_1 = randint(0, 40)
result_2 = "Too high" if number_1 >= 20 else "Thank you"
print(result_2)


# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = "mike"
last_name = "soloman"
result_3 = "".join(first_name + last_name).upper() if len(first_name) < 5 else first_name.lower()
print(result_3)


# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = randint(10, 35)
result_4 = f"Thank you, your number was {number_2}" if 10 <= number_2 <= 20 else f"Incorrect answer {number_2}"
print(result_4)

# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = randint(12, 24)
result_5 = ""
if age:
    if age >= 18:
        result_5 = f"Since your age is {age}\nYou can vote!"
    elif age >= 17:
        result_5 = f"Since your age is {age}\nYou can learn how to drive!"
    elif age >= 16:
        result_5 = f"Since your age is {age}\nYou can buy lottery tickets!"
    else:
        result_5 = f"Since your age is {age}\nYou can go to trick and treat!"
else:
    result_5 = "Invalid Value"
print(result_5)

# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = randint(1, 12)
result_month = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]
print(f"Your random num selection was {month} ... which is {result_month[month -1 ]}")


