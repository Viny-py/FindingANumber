import math, random, sys

number_list = []

size = int(input("How many numbers in the list?\n"))
find = input("What number would you like to find? \n(ex: 1 biggest, 3 smallest, 2 biggest)\n")

#Making a list to find the number chosen
number_finder = list(find) #ex: "10 biggest" = ["1", "0", " ", "b", "i", "g", "g", "e", "s", "t"]
space_index = number_finder.index(" ") #Finding the space in order to isolate the number chosen
number_finder = number_finder[:space_index]# Getting the chosen number (ex: ["1", "0"])

number = str() # Making a variable to transform the separated number in the list into a number
for string in number_finder: # Getting each value of the list (["1", "0"])
    number = number + str(string) # putting them together to make the string "10"
number = int(number) # String -> int ("10" - > 10)

# Changing the number chosen to "list format",
# for instance: if the number chosen was 10, you want to find the 10th biggest number in the list
# therefore, in a sorted(list), to find that number, you would need to find list[-10]
# and to find the 10th smallest number, it would be list(9)
if "biggest" in find:
    number *= -1
elif "smallest" in find:
    number -= 1
else:
    print("\n Oops! Something went wrong!\nTry typing correctly next time!\n")
    sys.exit()

# Creating a list of the chosen size with random numbers from 1 - 100
for i in range(size):
    number_list.append(random.randint(1, 100))

# New variable to store all the random values in the list (copy())
# Using set() to remove all numbers that are repeated
# Then transforming it into a list
# Then sorting the list (smallest -- biggest) with no repeating numbers
new_list = sorted(list(set(number_list.copy())))

#prints the original list (all random numbers in a random order)
print(f"Original list: {number_list}")

#Using the variable "find" to mention the chosen number ("10 biggest")
# prints the chosen position of the number
# eg:"10 biggest" changed to (10 * -1 = -10), therefore, finding new_list[-10]
# In other words, the 10th biggest number in the list!
print(f"The {find.replace(" ", "º ")} number on the list is the number {new_list[number]}.")