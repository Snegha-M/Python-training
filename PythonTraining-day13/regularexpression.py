'''
What is Regular Expression?
    Regular Expressions, also known as “regex” or “regexp”, are used to match strings of text
    such as particular characters, words, or patterns of characters.
    It means that we can match and extract any string pattern from the text with the help of regular expressions.
How can we use regular expression?
    Import the regex module with import re.
    Create a Regex object with the re. compile() function. ...
    Pass the string you want to search into the Regex object's search() method. ...
    Call the Match object's group() method to return a string of the actual matched text
'''
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())