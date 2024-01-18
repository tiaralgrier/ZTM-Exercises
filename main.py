# Exercise 2: Password Checker
username = input('Enter your username: ') # Ask for username
password = input('Enter your password: ') # Ask for password

password_length = len(password)
password_stars = '*' * password_length

# Read password and length to username
print(f'{username}, your password {password_stars} is {password_length} letters long.')

'''
# Exercise 1: Type Conversion
year = input('What year were you born? ')
age = 2023 - int(year) #Convert year => int

print(f'You are {age} years old!')
'''