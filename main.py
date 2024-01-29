# Exercise 4:

# Exercise 3: Logical Operators
'''
1. Check if magician AND expert: "you are a master magician"
2. Check if magician but NOT expert: "at least you're getting there"
3. If you're not a magician: "You need magic powers"
'''
is_magician = True
is_expert = False

if is_expert and is_magician:
  print("You are a master magician!")
elif is_magician and not is_expert:
  print("At least you're getting there...")
elif not is_magician:
  print("You need magic powers... )=")


'''
# Exercise 2: Password Checker
username = input('Enter your username: ') # Ask for username
password = input('Enter your password: ') # Ask for password

password_length = len(password)
password_stars = '*' * password_length

# Read password and length to username
print(f'{username}, your password {password_stars} is {password_length} letters long.')
'''

'''
# Exercise 1: Type Conversion
year = input('What year were you born? ')
age = 2023 - int(year) #Convert year => int

print(f'You are {age} years old!')
'''