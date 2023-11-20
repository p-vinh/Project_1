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
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q10', 'q11'}
    alphabet = set("0123456789_+-eE.")
    transitions = {
        **{('q0', str(c)): {'q1'} for c in range(10)},
        ('q0', 'e'): {'q2'},
        ('q0', 'E'): {'q2'},
        ('q0', '_') : {'q3'},
        ('q0', '.') : {'q4'},
        ('q0', '+') : {'q13'},
        ('q0', '-') : {'q13'},
        
        **{('q1', str(c)): {'q5'} for c in range(10)},
        ('q1', 'e'): {'q2'},
        ('q1', 'E'): {'q2'},
        ('q1', '_') : {'q6'},
        ('q1', '.') : {'q7'},
        ('q1', '+') : {'q13'},
        ('q1', '-') : {'q13'},
        
        **{('q2', str(c)): {'q8'} for c in range(10)},        
        ('q2', '+') : {'q4'},
        ('q2', '-') : {'q4'},
        ('q2', '_') : {'q13'},
        ('q2', '.') : {'q13'},
        ('q2', 'e') : {'q13'},
        ('q2', 'E') : {'q13'},
        
        **{('q3', str(c)): {'q9'} for c in range(10)},
        ('q3', 'e'): {'q13'},
        ('q3', 'E'): {'q13'},
        ('q3', '_') : {'q13'},
        ('q3', '.') : {'q13'},
        ('q3', '+') : {'q13'},
        ('q3', '-') : {'q13'},
        
        **{('q4', str(c)): {'q8'} for c in range(10)},
        ('q4', 'e'): {'q13'},
        ('q4', 'E'): {'q13'},
        ('q4', '_') : {'q13'},
        ('q4', '.') : {'q13'},
        ('q4', '+') : {'q13'},
        ('q4', '-') : {'q13'},
        
        **{('q5', str(c)): {'q5'} for c in range(10)},
        ('q5', 'e'): {'q2'},
        ('q5', 'E'): {'q2'},
        ('q5', '_') : {'q6'},
        ('q5', '.') : {'q7'},
        ('q5', '+') : {'q13'},
        ('q5', '-') : {'q13'},
        
        **{('q6', str(c)): {'q5'} for c in range(10)},
        ('q6', 'e'): {'q13'},
        ('q6', 'E'): {'q13'},
        ('q6', '_') : {'q13'},
        ('q6', '.') : {'q13'},
        ('q6', '+') : {'q13'},
        ('q6', '-') : {'q13'},
        
        **{('q7', str(c)): {'q8'} for c in range(10)},
        ('q7', 'e'): {'q13'},
        ('q7', 'E'): {'q13'},
        ('q7', '_') : {'q13'},
        ('q7', '.') : {'q13'},
        ('q7', '+') : {'q13'},
        ('q7', '-') : {'q13'},
        
        **{('q8', str(c)): {'q10'} for c in range(10)},
        ('q8', 'e'): {'q2'},
        ('q8', 'E'): {'q2'},
        ('q8', '_') : {'q11'},
        ('q8', '.') : {'q12'},
        ('q8', '+') : {'q13'},
        ('q8', '-') : {'q13'},
        
        **{('q9', str(c)): {'q9'} for c in range(10)},
        ('q9', 'e'): {'q2'},
        ('q9', 'E'): {'q2'},
        ('q9', '_') : {'q3'},
        ('q9', '.') : {'q4'},
        ('q9', '+') : {'q13'},
        ('q9', '-') : {'q13'},
        
        **{('q10', str(c)): {'q10'} for c in range(10)},
        ('q10', 'e'): {'q2'},
        ('q10', 'E'): {'q2'},
        ('q10', '_') : {'q11'},
        ('q10', '.') : {'q12'},
        ('q10', '+') : {'q13'},
        ('q10', '-') : {'q13'},
        
        
    }
    
    initial_state = 'q0'
    accepting_states = {'q1',}
    nfa = NFA.NFA(states, alphabet, transitions, initial_state, accepting_states)
    
    while True:
        s = input("Enter a string: ")
        
        if s == "quit":
            break
        
        if nfa.process_input(s):
            print("Valid Floating point literal")
        else:
            print("Invalid Floating point literal")
        
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