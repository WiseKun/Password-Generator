# Password Generator made by Mustafa A (WiseKun)
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_len = len(alphabet)

other_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '£', '$', '%', '&', '@', '#', '~', '<', '>', '?']
other_characters_len = len(other_characters)

def generate_password():
    password_lst = []
    num_of_upper_letters = random.randint(3, 4)
    num_of_lower_letters = random.randint(3, 4)
    num_of_numbers = random.randint(3, 4)
    num_of_other_characters = random.randint(3, 4)
    length = num_of_upper_letters+num_of_lower_letters+num_of_numbers+num_of_other_characters

    while (len(password_lst) < length):
        random1 = random.randint(0, 1)
        if (random1 == 0) and (num_of_lower_letters >= 1 or num_of_upper_letters >= 1):
            #print('letter')
            random2 = random.randint(0, 1)
            if (random2 == 0) and (num_of_lower_letters > 0):
                #print('lower')
                num_of_lower_letters -= 1
                password_lst.append(alphabet[random.randint(0, alphabet_len-1)])
            elif (random2 == 1) and (num_of_upper_letters > 0):
                #print('upper')
                num_of_upper_letters -= 1
                password_lst.append(alphabet[random.randint(0, alphabet_len-1)].upper())
                
        elif (random1 == 1) and (num_of_numbers >= 1 or num_of_other_characters >= 1):
            random2 = random.randint(0, 1)
            if (random2 == 0) and (num_of_numbers > 0):
                num_of_numbers -= 1
                password_lst.append(other_characters[random.randint(0, 10)])
            elif (random2 == 1) and (num_of_other_characters > 0):
                num_of_other_characters -= 1
                password_lst.append(other_characters[random.randint(10, other_characters_len-1)])

    return ''.join(password_lst)

my_password = generate_password()
print('{}'.format(my_password))

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
        if (value == False):
            strong_password = False
            break
        else:
            pass
    return strong_password 
    # If the password is not strong it returns 0, else, it returns 1

def determine_strength(quantity=1000):
    total_strength = 0
    for i in range(quantity):
        password = generate_password()
        strength = password_strength(password)
        #print("Password: {}\nStrength: {}\n".format(password, strength))
        total_strength += strength
    return float(round(total_strength/quantity))

print(determine_strength(1000)) # The current average strength is always 1.0
