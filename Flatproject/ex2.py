import tkinter as tk
from tkinter import messagebox


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


class MooreMealyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moore to Mealy Machine Converter")
        
        # Set background color
        self.root.configure(bg='lightblue')

        self.moore_machine = MooreMachine()

        # Input for state and output
        tk.Label(root, text="State:", bg='lightblue').grid(row=0, column=0)
        self.state_entry = tk.Entry(root, bg='white', fg='black')
        self.state_entry.grid(row=0, column=1)

        tk.Label(root, text="Output:", bg='lightblue').grid(row=1, column=0)
        self.output_entry = tk.Entry(root, bg='white', fg='black')
        self.output_entry.grid(row=1, column=1)

        self.add_state_button = tk.Button(root, text="Add State", command=self.add_state, bg='green', fg='white')
        self.add_state_button.grid(row=2, columnspan=2)

        # Input for transitions
        tk.Label(root, text="From State:", bg='lightblue').grid(row=3, column=0)
        self.from_state_entry = tk.Entry(root, bg='white', fg='black')
        self.from_state_entry.grid(row=3, column=1)

        tk.Label(root, text="Input Symbol:", bg='lightblue').grid(row=4, column=0)
        self.input_symbol_entry = tk.Entry(root, bg='white', fg='black')
        self.input_symbol_entry.grid(row=4, column=1)

        tk.Label(root, text="To State:", bg='lightblue').grid(row=5, column=0)
        self.to_state_entry = tk.Entry(root, bg='white', fg='black')
        self.to_state_entry.grid(row=5, column=1)

        self.add_transition_button = tk.Button(root, text="Add Transition", command=self.add_transition, bg='orange', fg='white')
        self.add_transition_button.grid(row=6, columnspan=2)

        self.convert_button = tk.Button(root, text="Convert to Mealy", command=self.convert, bg='blue', fg='white')
        self.convert_button.grid(row=7, columnspan=2)

        self.result_text = tk.Text(root, height=10, width=50, bg='white', fg='black')
        self.result_text.grid(row=8, columnspan=2)

    def add_state(self):
        state = self.state_entry.get().strip()
        output = self.output_entry.get().strip()
        if state and output:
            self.moore_machine.add_state(state, output)
            self.state_entry.delete(0, tk.END)
            self.output_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added state {state} with output {output}.")
        else:
            messagebox.showerror("Error", "Please enter both state and output.")

    def add_transition(self):
        from_state = self.from_state_entry.get().strip()
        input_symbol = self.input_symbol_entry.get().strip()
        to_state = self .to_state_entry.get().strip()
        if from_state and input_symbol and to_state:
            if from_state in self.moore_machine.states and to_state in self.moore_machine.states:
                self.moore_machine.add_transition(from_state, input_symbol, to_state)
                self.from_state_entry.delete(0, tk.END)
                self.input_symbol_entry.delete(0, tk.END)
                self.to_state_entry.delete(0, tk.END)
                messagebox.showinfo("Success", f"Added transition from {from_state} to {to_state} on input {input_symbol}.")
            else:
                messagebox.showerror("Error", "Both states must exist.")
        else:
            messagebox.showerror("Error", "Please enter from state, input symbol, and to state.")

    def convert(self):
        mealy_machine = convert_moore_to_mealy(self.moore_machine)
        self.result_text.delete(1.0, tk.END)
        for (from_state, input_symbol), (to_state, output) in mealy_machine.transitions.items():
            self.result_text.insert(tk.END, f"From {from_state} on input '{input_symbol}' -> To {to_state} with output '{output}'\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = MooreMealyConverterApp(root)
    root.mainloop()