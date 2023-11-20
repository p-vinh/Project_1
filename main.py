"""
Expand your program to recognize Python octal and hexadecimal integer literals (section 2.4.4 - 2.4.5)
For simplicity, you can assume the input string s length <=20.
Your program should ask for user input as a string, and check if it can be a valid decimal integer or not.
You also need to include your NFA design (with unlimited digits allowed
you can break this into a few smaller NFA's so it's not one humongous machine) drawn using JFLAP.

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

def init_octal_nfa():
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
    alphabet = set("01234567_oO")
    transitions = {
                    **{('q0', str(digit)): {'q5'} for digit in alphabet if digit != "0"},
                    ('q0', '0'): {'q1'},
                    
                    **{('q1', str(digit)): {'q5'} for digit in alphabet if digit != "O" and digit != "o"},
                    ('q1', 'o'): {'q2'},
                    ('q1', 'O'): {'q2'},
                    
                    **{('q2', str(digit)): {'q3'} for digit in range(8)},
                    ('q2', '_'): {'q4'},
                    ('q2', 'O'): {'q5'},
                    ('q2', 'o'): {'q5'},
                    
                    **{('q3', str(digit)): {'q3'} for digit in range(8)},
                    ('q3', '_'): {'q4'},
                    ('q3', 'O'): {'q5'},
                    ('q3', 'o'): {'q5'},
                    
                    **{('q4', str(digit)): {'q3'} for digit in range(8)},
                    ('q4', '_'): {'q5'},
                    ('q4', 'o'): {'q5'},
                    ('q4', 'O'): {'q5'},
                    
                    **{('q5', str(digit)): {'q5'} for digit in alphabet}
                    }
        
    initial_state = 'q0'
    accepting_states = {'q3'}
    octal_nfa = NFA.NFA(states, alphabet, transitions, initial_state, accepting_states)
    
    return octal_nfa

def init_hexadecimal_nfa():
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
    alphabet = set("0123456789abcdefABCDEF_xX")
    transitions = {
                    ('q0', '0'): {'q1'},
                    ('q1', 'x'): {'q2'},
                    ('q1', 'X'): {'q2'},
                    
                    ('q2', '_'): {'q3'},
                    ('q2', None): {'q3'},
                    
                    **{('q3', str(char)): {'q4'} for char in alphabet if char != "_" and char != "x" and char != "X"},
                    **{('q4', str(char)): {'q4'} for char in alphabet if char != "_" and char != "x" and char != "X"},
                    ('q4', None): {'q2', 'q5'}
                    }
    
    initial_state = 'q0'
    accepting_states = {'q5'}

    hexadecimal_nfa = NFA.NFA(states, alphabet, transitions, initial_state, accepting_states)
    
    return hexadecimal_nfa

def main():
    
    octal_nfa = init_octal_nfa()
    hexadecimal_nfa = init_hexadecimal_nfa()
    
    while True:
        s = input("Enter a string: ").strip()
        
        if s == "quit":
            break
        
        if hexadecimal_nfa.process_input(s):
            print("Valid Hexadecimal Integer literal")
        else:
            print("Invalid Hexadecimal Integer literal")
        
        if octal_nfa.process_input(s):
            print("Valid Octal Integer literal")
        else:
            print("Invalid Octal Integer literal")
        
        hexadecimal_nfa.reset()
        octal_nfa.reset()

    # test_cases = generate_test_cases()
    
    # for test_case in test_cases:
    #     if nfa.process_input(test_case):
    #         print(f"{test_case}: Valid")
    #     else:
    #         print(f"{test_case}: Invalid")

    #     nfa.reset()    



if __name__ == '__main__':
    main()