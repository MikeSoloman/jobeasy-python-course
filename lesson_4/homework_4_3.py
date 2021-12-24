# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save
# it in the variable char_1.
# Write code, which will count how many times your character is included in your
# string.
# Save result to result_1 variable

string_1 = "Samsa Tatli Dedim Sene"
char_1 = 's'
result_1 = 0
counter = 0
for i in string_1:
    if char_1 == i.lower():
        result_1 += 1
print(result_1)

# or

string_1 = "Samsa Tatli Dedim Sene"
char_1 = 's'
result_1 = string_1.lower().count('s')
print(result_1)

# or

resultt_1 = 0
while counter < len(string_1):
    if string_1[counter].lower() == char_1:
        resultt_1 += 1
    counter += 1
print(result_1)

# Enter a random number and save it in variable number_1. Then create code to
# multiply all the digits together
# and save result in the result_2 variable.

num_1 = 253
counter_1 = 0
my_res = 1
while counter_1 < len(str(num_1)):
    my_res *= int(str(num_1)[counter_1])
    counter_1 += 1
print(my_res)

# Enter a random number and save it in variable number_2. Then create code which
# will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 25723344332
result_3 = int(str(number_2)[::-1])
print(result_3)
print(type(result_3))
counter_2 = int(len(str(number_2)) -1)
#or


result_3 = ""

while counter_2 > -1 :
    result_3 += (str(number_2)[counter_2])
    counter_2 -= 1
print(result_3)

#or

