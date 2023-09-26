#password generator 
#for a password needs: 
#number alphabets(lower and upper) special symbols 
#for strong password need the combination and the length to be more than 6
import re 
import random 

Max_length = 12 #the length of the password must be of 8 characters

digits = ['0', '1', '2',
          '3', '4', '5', '6', '7', '8', '9']

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

special_symbols = ['@', '#', '$', '%', '=', ':', 
                   '?', '.', '/', '|', '~', '>',
                    '*', '(', ')', '<']

# generating the random password 
# combines all the character arrays above to form one array
COMBINED_LIST = digits + upper_case + lower_case + special_symbols
print(COMBINED_LIST)
 
# randomly select at least one character from each character set above
rand_digit = random.choice(digits)
rand_upper = random.choice(upper_case)
rand_lower = random.choice(lower_case)
rand_symbol = random.choice(special_symbols)

# Generate a random password of length between 6 and 12 characters
password_length = random.randint(6,12)
random_password = ''.join(random.choice(COMBINED_LIST) for _ in range(password_length))

def password_generator(pwd):
    # use of upper lower and special symbols
    
    if not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,12}$", pwd):
        return "password must have one special symbol, lower case, upper case and a digit"
    else:
        return "Password is valid"
    
def main():
    print("Generated Random Password:", random_password)
    input(password_generator(random_password))

# Driver Code
if __name__ == '__main__':
    main()