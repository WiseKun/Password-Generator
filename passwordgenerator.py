# Password Generator made by Mustafa A (WiseKun)
import random
import string

password_length = 8 #int(input('Enter password length: ')) # Length of the generated password (Passwords shorter than 8 not recommended)

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

numbers = string.digits
numbers_len = len(numbers)

other_chars = string.punctuation

# The strength is just an estimate
def password_strength(password):
  password_check = {'lower': False, 'upper': False, 'number': False, 'other': False, 'length': False}
  for letter in password:
    if (letter in lower_alphabet):
      password_check['lower'] = True
    elif (letter in upper_alphabet):
      password_check['upper'] = True
    elif (letter in numbers):
      password_check['number'] = True
    elif (letter in other_chars):
      password_check['other'] = True
    
    if (len(password) >= 8):
      password_check['length'] = True
    
  strength = 0
  for value in password_check.values():
    if (value):
      strength += 100/len(password_check.values())
  return strength
    # Returns a number from 0 to 100 with 0 being very weak and 100 being strong

def generate_password():
  if (password_length >= 4):
    password = ''
    while (password_strength(password) != 100):
      password = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, password_length))
    return password
  else:
    # Warning -- Passwords less than 4 are very weak
    return ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, password_length))

my_password = generate_password()
print('Password: {}\nStrength: %{}'.format(my_password, password_strength(my_password)))

def determine_overall_strength(quantity=1000):
  total_strength = 0
  for i in range(quantity):
    password = generate_password()
    strength = password_strength(password)
    #print("Password: {}\nStrength: {}\n".format(password, strength))
    total_strength += strength
  return float(total_strength/quantity)

#print(determine_overall_strength(10000)) # The current average strength is always %100
