#Exercise 7: Tesla
#1. Wrap the below code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age. Also, make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age=0):
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()


# Exercise 6: Find duplicates
''''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'z', 'z']

duplicates = []
for letter in some_list:
  if some_list.count(letter) > 1:
    if letter not in duplicates:
      duplicates.append(letter)

print(duplicates)


# Exercise 5: Our First GUI
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#A function
def show_tree():
  for image in picture:
    for pixel in image:
      if (pixel == 1):
        print("*", end='')
      else:
        print(" ", end='')
    print('')

show_tree()
show_tree()
show_tree()

# Exercise 4: Build counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for number in my_list:
  counter = counter + number

print(counter)



# Exercise 3: Logical Operators
1. Check if magician AND expert: "you are a master magician"
2. Check if magician but NOT expert: "at least you're getting there"
3. If you're not a magician: "You need magic powers"


is_magician = True
is_expert = False

if is_expert and is_magician:
  print("You are a master magician!")
elif is_magician and not is_expert:
  print("At least you're getting there...")
elif not is_magician:
  print("You need magic powers... )=")



# Exercise 2: Password Checker
username = input('Enter your username: ') # Ask for username
password = input('Enter your password: ') # Ask for password

password_length = len(password)
password_stars = '*' * password_length

# Read password and length to username
print(f'{username}, your password {password_stars} is {password_length} letters long.')



# Exercise 1: Type Conversion
year = input('What year were you born? ')
age = 2023 - int(year) #Convert year => int

print(f'You are {age} years old!')
'''
