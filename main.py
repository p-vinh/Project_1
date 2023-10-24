"""
Recognize Python decimal integer literals (section 2.4.4 - 2.4.5)
For simplicity, you can assume the input string s length <=20.
Your program should ask for user input as a string, and check if it can be a valid decimal integer or not.
You also need to include your NFA design (with unlimited digits allowed
you can break this into a few smaller NFA's so it's not one humongous machine) drawn using JFlapLinks to an external site.. (Please submit the .jff files.)



Expand your program to recognize Python octal and hexadecimal integer literals (section 2.4.4 - 2.4.5)
For simplicity, you can assume the input string s length <=20.
Your program should ask for user input as a string, and check if it can be a valid decimal integer or not.
You also need to include your NFA design (with unlimited digits allowed
you can break this into a few smaller NFA's so it's not one humongous machine) drawn using JFLAP.

"""



def isOperator(s):
    pass

def isPlus(s):
    pass

def isStar(s):
    pass

def isClosedParen(s):
    pass

def isOpenParen(s):
    pass


# Function to check if the string is a valid decimal integer; Loops through the string and calls the appropriate function for each character in the expression
def match_expr(s, expr, match_length=0):
    pass

# Outermost function: Loops through the string and calls the appropriate function for each character
def match(s):
    pass



def main():
    pass



if __name__ == '__main__':
    main()