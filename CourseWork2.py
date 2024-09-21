'Team Name: Peewee'
'Repository Name: Coursework-02'
'Team Members:      - Rita Tamer. - Malak Badawy. - Ismail Emad.'
'Team Members ID:   - 202200191.  - 202101278.    - 202100753.'

'importing the functions from different files'

import PasswordLength
import Uppercase
import lowercase
import special_characters_and_digits
import Names_and_known_phrases 
import repeated_patterns 
import characters_from_username

def main(): 
    'printing conditions to abide to the strong password requirements'
    print("Hello! This a password validation software.\nPlease make sure to abide by these regulations for a valid Password:")
    print("Your password length should be at least 8 characters or more.\nYour password should at least contain one uppercase and one lowercase character")
    print("Your password should contain at least one special character and one digit.\nYour password should not contain any patterns.")
    print("Your Password should not be a name or a known phrase.\nYour password should not be a repetition of the username.")
    print ("If any condition is 'Weak' or 'Moderate' you will need to enter a new password.")
    'user inputs username and Password'
    Username = input("Please enter your username: ")        
    Password = input("Please enter your password: ")        
    'calling the functions (previously imported from the files above)'
    length = PasswordLength.password_length(Password)
    upper = Uppercase.checking_for_uppercases(Password)
    lower = lowercase.checking_for_lowercases(Password)
    special = special_characters_and_digits.checking_for_special_characters_digits(Password)
    names = Names_and_known_phrases.checking_for_names_and_known_phrases(Password)
    patterns = repeated_patterns.checking_for_repeated_patterns(Password)
    username = characters_from_username.checking_for_characters_in_username(Password,Username)
    'organizing the output of each function'
    array = [length,upper,lower,special,names,patterns,username]        
    array1 = ['Password length', 'usage of uppercases', 'usage of lowercases', 'usage of special characters and digits','uniqueness', 'occurrence of patterns', 'relativity to username']
    'checking if the password abides by the conditions'
    while True:     
        if length == 'Strong' and upper == 'Strong'  and lower == 'Strong' and special == 'Strong' and names == 'Strong'  and patterns == 'Strong'  and username == 'Strong' :
            array =[length,upper,lower,special,names,patterns,username]
            for i in range (len(array1)):
                print (array1[i],": ",array[i])
            'password status'
            print("Valid Password")    
            break
        else:
            'password status'
            print("Invalid password")    
            for i in range (len(array1)):
                print (array1[i],": ",array[i])
            'if password does not meet the requirements the user is required to enter a new password to be tested'
            Password = input("Enter password: ")        
            length = PasswordLength.password_length(Password)
            upper = Uppercase.checking_for_uppercases(Password)
            lower = lowercase.checking_for_lowercases(Password)
            special = special_characters_and_digits.checking_for_special_characters_digits(Password)
            names = Names_and_known_phrases.checking_for_names_and_known_phrases(Password)
            patterns = repeated_patterns.checking_for_repeated_patterns(Password)
            username = characters_from_username.checking_for_characters_in_username(Password,Username)
            array =[length,upper,lower,special,names,patterns,username]
            for i in range (len(array1)):
                print (array1[i],": ",array[i])
    return array

main()



