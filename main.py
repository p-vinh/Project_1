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

import NFA



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
    states = {'q0', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q10', 'q11'}
    alphabet = set("0123456789_")
    transitions = {
                   # non-zero digit 
                   **{('q0', str(digit)): {'q10'} for digit in range(1, 10)},
                   **{('q10', str(digit)): {'q10'} for digit in range(1, 10)},
                   
                   # lambda transition
                   ('q10', None) : {'q2', 'q3', 'q8'},
                   ('q10', '_') : {'q8'},
                   
                   # 0+
                   ('q2', '0') : {'q4'},
                   ('q4', '0') : {'q4'},
                   
                   # (["_"] 0)*
                   ('q4', None) : {'q5', 'q10'},
                   ('q5', '_') : {'q6'},
                   ('q5', None) : {'q6'},
                   ('q6', '0') : {'q7'},
                   ('q7', None) : {'q5', 'q10'},
                   
                   # (["_"] digit)*
                   **{('q8', str(digit)): {'q11'} for digit in range(0, 10)},
                   **{('q11', str(digit)): {'q11'} for digit in range(0, 10)},               
                   ('q11', None) : {'q3', 'q10'}
                  }
    
    initial_state = 'q0'
    accepting_states = {'q3'}
    nfa = NFA.NFA(states, alphabet, transitions, initial_state, accepting_states)
    
    while True:
        s = input("Enter a string: ")
        
        if s == "quit":
            break
        
        if nfa.process_input(s):
            print("Valid decimal integer literal")
        else:
            print("Invalid decimal integer literal")

        nfa.reset()    



if __name__ == '__main__':
    main()