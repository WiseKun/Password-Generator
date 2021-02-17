# Password Generator made by Mustafa A
# Version 1.0 -- Add basic functionality
# Version 1.1 -- Make passwords a bit shorter + Remove quantity + Add password strength + Able to see average password strength

import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_len = len(alphabet)

other_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '£', '$', '%', '&', ':', ';', '@', '#', '~', '<', '>', '?']
other_characters_len = len(other_characters)

def generate_password():
    password_lst = []
    for i in range(random.randint(8, 12)):
        random1 = random.randint(0, 1)
        if (random1==0):
            random2 = random.randint(0, 1)
            if (random2==0):
                password_lst.append(alphabet[random.randint(0, alphabet_len-1)])
            else:
                password_lst.append(alphabet[random.randint(0, alphabet_len-1)].upper())
        else:
            password_lst.append(other_characters[random.randint(0, other_characters_len-1)])

    return ''.join(password_lst)

password = generate_password()
print('{}'.format(password))

def password_strength(password):
    password_check = {'lower': False, 'upper': False, 'number': False, 'other': False, 'length': False}
    for letter in password:
        if (letter in alphabet):
            password_check['lower'] = True
        elif (letter in [i.upper() for i in alphabet]):
            password_check['upper'] = True
        elif (letter in other_characters[:10]):
            password_check['number'] = True
        elif (letter in other_characters[10:]):
            password_check['other'] = True

    if (len(password) >= 8):
        password_check['length'] = True
    
    strong_password = True
    for value in password_check.values():
        if (value==False):
            strong_password = False
            break
        else:
            pass
    return strong_password

passwords = []
for i in range(1000):
    passwords.append(generate_password())

strengths = []
for password in passwords:
    strengths.append(password_strength(password))

total_strength = 0
for strength in strengths:
    total_strength += strength

average_strength = total_strength/len(strengths)
print(average_strength) # The current average strength is 0.7 to 0.8 most of the time