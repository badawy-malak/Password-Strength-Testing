'importing the functions from different files'
import unittest                                   
import PasswordLength
import Uppercase
import lowercase
import special_characters_and_digits
import Names_and_known_phrases 
import repeated_patterns 
import characters_from_username                        

'intitating the class'
class TestmyCourseWork2(unittest.TestCase):          
    'testing the password length'
    def test_length(self):                        
        self.assertEqual(PasswordLength.password_length('abc123Abc'), 'Strong')
    def test_length(self):                        
        self.assertEqual(PasswordLength.password_length('Abc123ab'), 'Moderate')
    def test_length(self):                        
        self.assertEqual(PasswordLength.password_length('Abcabc'), 'Weak')
    'testing is the password contains uppercases'
    def test_Uppercase(self):                     
        self.assertEqual(Uppercase.checking_for_uppercases('ABC123abc'), 'Strong')
    def test_Uppercase(self):                     
        self.assertEqual(Uppercase.checking_for_uppercases('Abc123abc'), 'Moderate')
    def test_Uppercase(self):                     
        self.assertEqual(Uppercase.checking_for_uppercases('abc123'), 'Weak')
    'testing is the password contains lowercases'
    def test_Lowercase(self):                     
        self.assertEqual(lowercase.checking_for_lowercases('ABCabc123'),'Strong')
    def test_Lowercase(self):                     
        self.assertEqual(lowercase.checking_for_lowercases('ABCaBC123'),'Moderate')
    def test_Lowercase(self):                     
        self.assertEqual(lowercase.checking_for_lowercases('ABCABC123'),'Weak')
    'testing is the password contains special characters and digits'
    def test_special_characters(self):            
        self.assertEqual(special_characters_and_digits.checking_for_special_characters_digits('abc123!@#'),'Strong')
    def test_special_characters(self):            
        self.assertEqual(special_characters_and_digits.checking_for_special_characters_digits('abc123!ab'),'Moderate')
    def test_special_characters(self):            
        self.assertEqual(special_characters_and_digits.checking_for_special_characters_digits('abcABC'),'Weak')
    'testing is the password contains names or known phrases'
    def test_names_and_known_phrases(self):       
        self.assertEqual(Names_and_known_phrases.checking_for_names_and_known_phrases('KH4061CEM'),'Strong')
    def test_names_and_known_phrases(self):       
        self.assertEqual(Names_and_known_phrases.checking_for_names_and_known_phrases('rita1'),'Weak')
    'testing is the password contains characters from username'
    def test_username(self):                      
        self.assertEqual(characters_from_username.checking_for_characters_in_username('Coursework2','programming@tkh'),'Strong')
    def test_username(self):                      
        self.assertEqual(characters_from_username.checking_for_characters_in_username('programming','programming@tkh'),'Weak')
    'testing is the password contains patterns'
    def test_patterns(self):                      
        self.assertEqual(repeated_patterns.checking_for_repeated_patterns('Coursework2'),'Strong')
    def test_patterns(self):                      
        self.assertEqual(repeated_patterns.checking_for_repeated_patterns('abcabcabc'),'Weak')

if __name__ == "__main__":
    'Calling the main function'
    unittest.main()                                
