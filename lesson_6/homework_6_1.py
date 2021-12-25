# You are given a list in list_1 variable, write a swap_first_last
# function to return a new list with
# the first and the last elements of the list swapped.
# Return this list

list_1 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]

def swap_first_last(array_1):
    my_1 = array_1.copy()
    array_1[0] = my_1[-1]
    array_1[-1] = my_1[0]
    return array_1
print(swap_first_last(list_1))


# You are given a list in list_2 variable, write a reverse_list function which
# creates a new list in reversed order.
# Return this list

list_2 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]

def reverse_list(array_2):
    return array_2[::-1]
#or
def rev_list(array_2):
    new_one = [x for x in array_2[::-1]]
    return new_one
#or
def revivo_listo(array_2):
    new_list = []
    counter = len(array_2) - 1
    while counter > -1:
        new_list.append(array_2[counter])
        counter -= 1
    return new_list
print(revivo_listo(list_2))
#or

def revo_(array_2):
    array_2.reverse()
    return array_2
print(revo_(list_2))

# Create a list which contains only number items and save it to the
# list_3 variable. Then write multiply_list_items
# function to multiply all the items in a list. Return result of multiplication
from random import randint, random

list_3 = []

for x in range(10):
    list_3.append(randint(1, 4))

def multiply_list_items(array_3):
    result = 1
    for x in array_3:
        result *= x
    return result
print(list_3)
print(multiply_list_items(list_3))


#or

list_3 = []
for x in range(6):
    list_3.append(randint(1, 5))

def multiplakisyon(array_3):
    new_num = 1
    counter = 0
    while counter < len(array_3):
        if str(array_3[counter]).isdigit():
            new_num *= array_3[counter]
        counter += 1
    return new_num

print(list_3)
print(multiplakisyon(list_3))

# Create a list which contains only number items and save it to the list_4
# variable. Then write a smallest_item_list
# function to get the smallest number from a list. Return smallest element

list_4 = [10, 2, 5, 5, 0, -976]

def smallest_item_list(array_4):
    array_4.sort()
    return array_4[0]

print(smallest_item_list(list_4))

#or

def smaly_smaly(array_4):
    return min(array_4)
print(smaly_smaly(list_4))

#or loop

import random
def smally_smally(array_4):
    my_min = array_4[0]
    for x in array_4:
        if my_min > x:
            my_min = x
    return my_min

random.shuffle(list_4)

print(list_4)
print(smally_smally(list_4))
# Given a list in list_5 variable, write a remove_duplicates_list function
# to remove duplicates from a list.
# Return new list without duplicates

list_5 = [1, 3, 1, 1, 1, 2, 3, 4,
          'hello', 1, 2, 3, 4, 'hello', 'hello', 1]

def remove_duplicates_list(array_5):
    return list((set(array_5)))
print(remove_duplicates_list(list_5))

#or

def rem_dup(array_5):
    new_list = []
    counter = 0
    while counter < len(array_5):
        if array_5[counter] not in new_list:
            new_list.append(array_5[counter])
        counter += 1
    return new_list
print(rem_dup(list_5))

#or using for loop

def remy_remy(array_5):
    new_remi = []

    for x in array_5:
        if x not in new_remi:
            new_remi.append(x)
    return new_remi
print(remy_remy(list_5))

#or one sentence

def remo_remo(array_5):
    new_list_5 = []
    [new_list_5.append(num) for num in array_5 if num not in new_list_5]
    return new_list_5
print(remo_remo(list_5))


# You are given a list in list_6 variable.Enter an integer number and save it to number_1 variable,
# write a longer_words_list function which will return the list of words that are longer than number_1
# from a given list of words.
number_1 = 7.1
list_6 = ['On', 'it', 'differed', 'repeated', 'wandered', 'required', 'in.', 'Then', 'girl', 'neat', 'why', 'yet',
          'knew', 'rose', 'spot.', 'Moreover', 'property', 'we', 'he', 'kindness', 'greatest', 'be', 'oh', 'striking',
          'laughter.', 'In', 'me', 'he', 'at', 'collecting', 'affronting', 'principles', 'apartments.', 'Has', 'visitor',
          'law', 'attacks', 'pretend', 'you', 'calling', 'own', 'excited', 'painted.', 'Contented', 'attending',
          'smallness', 'it', 'oh', 'ye', 'unwilling.', 'Turned', 'favour', 'man', 'two', 'but', 'lovers.', 'Suffer',
          'should', 'if', 'waited', 'common', 'person', 'little', 'oh.', 'Improved', 'civility', 'graceful', 'few',
          'smallest', 'screened', 'settling.', 'Likely', 'active', 'her', 'warmly', 'has.']

def longer_words_list(array_6, number1):
    return [x for x in array_6 if len(x) > number1]

print(longer_words_list(list_6, number_1))

#or

def ooohhh_loooong_jooohn_or_long_JOHNSON(array_6, num_1):
    new_list= []
    for x in array_6:
        if len(x) > num_1:
            new_list.append(x)
    return new_list
print(ooohhh_loooong_jooohn_or_long_JOHNSON(list_6, number_1))


# Given two lists in list_7 and list_8 variables.
# Write a function find_item_lists that takes two lists and returns
# True if they have at least one common member.
list_7 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]
list_8 = ['asdasd', True, 8, False, 94, 'Hello world', None, range(1, 11), 100, 1]

def find_item_lists(array_7, array_8):
    counter = len(list_8) - 1
    while counter > -1:
        if list_7[counter] in list_8:
            return True
        counter -= 1
    else:
        return False
print(find_item_lists(list_7, list_8))

# You are given a list in list_9 variable.
# Write a function list_to_string to convert a list of
# characters into a string.
list_9 = ['I', ' ', 'l', 'i', 'k', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n', " "]

def list_to_string(list9):
    return ''.join(list9)
print(list_to_string(list_9))

#or

def li_to_str(list9):
    return "".join(str(x) for x in list9)
print(li_to_str(list_9))

#for loop

def litst_to_ssssss(list9):
    my_str = ""
    for x in list9:
        my_str += str(x)
    return my_str
print(litst_to_ssssss(list_9))


# Given a list of numbers in list_10 and a number number_2,
# write count_items_list function which will count number of
# occurrences of number_2 in the given list
list_10 = [1, 2, 3, 1, 1, 1, 2, 3, 4]
number_2 = 1

def count_items_list(array_10, number2):
    return list_10.count(number2)
print(count_items_list(list_10, number_2))

# or for loops

def counting_of_items(array_10, number2):
    counter = 0
    for x in array_10:
        if x == number2:
            counter += 1
    return counter
print(counting_of_items(list_10, number_2))

# or one line

def count_items(array_10, number2):
    counter = [x for x in array_10 if number2 == x]
    return counter
print(count_items(list_10, number_2))

# Given a list of numbers, write a function even_items_list to return
# new list which include all even numbers in
# given list.
list_11 = [1, 2, 3, 1, 1, 1, 2, 3, 4]

def even_items_list(array_11):
    return [x for x in array_11 if x % 2 == 0]
print(even_items_list(list_11))

