class NFA:
    #this is decIntegers only
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.current_states = {initial_state}
        self.accepting_states = accepting_states

    def process_input(self, input_string):
        
        for char in input_string:
            if char not in self.alphabet:
                return False
            
        for symbol in input_string:
            self.current_states = self.get_next_states(symbol)
            self.current_states.update(self.get_next_states(None))
            
            # if there are no next states, return False
            if not self.current_states:
                return False
        
        # Edge case: if there is only one character, get the next states.
        self.current_states = self.get_next_states(None) # Get all lambda transitions from the current states.
        
        return any(state in self.accepting_states for state in self.current_states)

    def get_next_states(self, symbol):
        next_states = set()
        for state in self.current_states:
            if (state, symbol) in self.transitions:
                next_states.update(self.transitions[(state, symbol)])
            if (state, None) in self.transitions:
                next_states.update(self.transitions[(state, None)])
                
        return next_states
    
    def reset(self):
        self.current_states = {self.initial_state}
    
# states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11'}
# alphabet = set("0123456789_")
# transitions = {('q0', '0'): {'q1'}, ('q1', '1'): {'q2'}, ('q2', '0'): {'q0'}}
# initial_state = 'q0'
# accepting_states = {'q2'}



# nfa = NFA(states, alphabet, transitions, initial_state, accepting_states)