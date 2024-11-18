class MooreMachine:
    def __init__(self):
        self.states = {}  # Dictionary to hold state and output pairs
        self.transitions = {}  # Dictionary to hold transitions

    def add_state(self, state, output):
        self.states[state] = output
        self.transitions[state] = {}

    def add_transition(self, from_state, input_symbol, to_state):
        self.transitions[from_state][input_symbol] = to_state


class MealyMachine:
    def __init__(self):
        self.states = {}  # Dictionary to hold states
        self.transitions = {}  # Dictionary to hold transitions with outputs

    def add_state(self, state):
        self.states[state] = {}

    def add_transition(self, from_state, input_symbol, to_state, output):
        self.transitions[(from_state, input_symbol)] = (to_state, output)


def convert_moore_to_mealy(moore):
    mealy = MealyMachine()

    # Create states in Mealy machine
    for state in moore.states:
        mealy.add_state(state)

    # Create transitions in Mealy machine
    for state, outputs in moore.states.items():
        for input_symbol, next_state in moore.transitions[state].items():
            output = outputs  # Output is the output of the current state
            mealy.add_transition(state, input_symbol, next_state, output)

    return mealy


# Example usage
if __name__ == "__main__":
    # Create a Moore machine
    moore_machine = MooreMachine()
    moore_machine.add_state('S0', 0)
    moore_machine.add_state('S1', 1)

    moore_machine.add_transition('S0', '0', 'S0')
    moore_machine.add_transition('S0', '1', 'S1')
    moore_machine.add_transition('S1', '0', 'S0')
    moore_machine.add_transition('S1', '1', 'S1')

    # Convert to Mealy machine
    mealy_machine = convert_moore_to_mealy(moore_machine)

    # Display Mealy machine transitions
    print("Mealy Machine Transitions:")
    for (from_state, input_symbol), (to_state, output) in mealy_machine.transitions.items():
        print(f"{from_state} --{input_symbol}--> {to_state} (Output: {output})")