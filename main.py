"""
Recognize Python decimal integer literals (section 2.4.4 - 2.4.5)
For simplicity, you can assume the input string s length <=20.
Your program should ask for user input as a string, and check if it can be a valid decimal integer or not.
You also need to include your NFA design (with unlimited digits allowed
you can break this into a few smaller NFA's so it's not one humongous machine) drawn using JFlapLinks to an external site.. (Please submit the .jff files.)

"""

import NFA
import random

# Debug function
def generate_test_cases():
    test_cases = []

    for _ in range(10):
        # Nonzerodigit
        start = ''.join(str(random.randint(0, 9)) for _ in range(1, 3))
        
        choice = random.randint(0, 1)
        # (["_"] digit)*
        if choice == 0:
            for _ in range(5):
                rest = ''.join([random.choice(['_', '']) + str(random.randint(0, 9)) for _ in range(1, 3)])
            test_cases.append(start + rest)
            
        # "0"+ (["_"] "0")* 
        elif choice == 1:
            for _ in range(5):
                start = '0' * random.randint(0, 3) # 1 or more 0's. Is able to generate invalid strings
                rest = ''.join([random.choice(['_', '', '0']) for _ in range(4)])
            test_cases.append(start + rest)
    

    return test_cases


def main():
    states = {'q0', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q10'}
    alphabet = set("0123456789_+-eE.")
    transitions = {
                    # floatnumber   ::=  pointfloat | exponentfloat
                    ('q0', None): {'q1', 'q2'},
                    
                    # pointfloat ::=  [digitpart] fraction
                    **{('q2', digit): {'q3'} for digit in '0123456789'},
                    ('q2', None): {'q3'},
                    ('q3', None): {'q4'},
                    ('q3', '_'): {'q4'},
                    **{('q4', digit): {'q5'} for digit in '0123456789'},
                    ('q5', None): {'q3'},
                    
                    # fraction: "." digitpart | digitpart "."
                    ('q3', '.'): {'q1'},
                    **{('q1', digit): {'q6'} for digit in '0123456789'},
                    **{('q7', digit): {'q8'} for digit in '0123456789'},
                    ('q8', None): {'q6'},
                    ('q3', None): {'q11'},
                    ('q6', None): {'q11', 'q7', 'q9'},
                    ('q6', '_'): {'q7'},
                    ('q6', '.'): {'q9'},
                    
                    # exponentfloat ::= (digitpart | pointfloat) exponent
                    ('q11', 'e'): {'q10'},
                    ('q11', 'E'): {'q10'},
                    ('q10', '+'): {'q1'},
                    ('q10', '-'): {'q1'},
                    ('q10', None): {'q1'}
                  }
    
    initial_state = 'q0'
    accepting_states = {'q9'}
    nfa = NFA.NFA(states, alphabet, transitions, initial_state, accepting_states)
    
    while True:
        s = input("Enter a string: ")
        
        if s == "quit":
            break
        
        if nfa.process_input(s):
            print("Valid Floating point literals")
        else:
            print("Invalid Floating point literals")
        
        nfa.reset()

    # test_cases = generate_test_cases()
    
    # for test_case in test_cases:
    #     if nfa.process_input(test_case):
    #         print(f"{test_case}: Valid")
    #     else:
    #         print(f"{test_case}: Invalid")

    #     nfa.reset()    



if __name__ == '__main__':
    main()