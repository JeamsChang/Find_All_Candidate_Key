from itertools import combinations

import tkinter as tk
from tkinter import messagebox

def compute_closure(set, fds):
    """
    Computes the closure of a set under a set of functional dependencies (fds).

    Parameters:
    set (set): The set for which the closure needs to be computed.
    fds (list): The list of functional dependencies.

    Returns:
    set: The closure of the set under the given functional dependencies.
    """
    closure = set.copy()
    while True:
        new_closure = closure.copy()
        for lhs, rhs in fds:
            if lhs.issubset(closure):
                new_closure.update(rhs)
        if new_closure == closure:
            break
        else:
            closure = new_closure
    return closure

def candidate_keys(relation, fds):
    """
    Computes all candidate keys of a relation under a set of functional dependencies (fds).

    Parameters:
    relation (set): The set of attributes in the relation.
    fds (list): The list of functional dependencies.

    Returns:
    list: The list of candidate keys for the relation.
    """
    attrs = set(relation)
    keys = []
    for r in range(1, len(attrs) + 1):
        for subset in combinations(attrs, r):
            subset = set(subset)
            if compute_closure(subset, fds) == attrs:
                if all(not key.issubset(subset) for key in keys):
                    keys.append(subset)
    return keys

def parse_fds(input_fds):
    """
    Parses the user input for functional dependencies and returns a list of tuples.

    Parameters:
    input_fds (str): The user input for functional dependencies.

    Returns:
    list: The list of functional dependencies as tuples.
    """
    fds = []
    for fd in input_fds.split(','):
        lhs, rhs = fd.split('-')
        lhs = set(lhs.strip())
        rhs = set(rhs.strip())
        fds.append((lhs, rhs))
    return fds

# # User input for the relation
# relation_input = input("Enter the attributes of the relation (e.g., A, B, C, D): ")
# relation = set(relation_input.replace(" ", "").split(','))

# # User input for the functional dependencies
# fds_input = input("Enter the functional dependencies (e.g., AB-C, CD-E): ")
# fds = parse_fds(fds_input)

# # Compute candidate keys
# keys = candidate_keys(relation, fds)

# Output the candidate keys
# print("Candidate keys:")
# for key in keys:
#     print(''.join(key))

# Create a GUI for the Candidate Key Miner
root = tk.Tk()
root.title("Candidate Key Miner")

# Create form with relation and functional dependencies fields
relation_label = tk.Label(root, text="Relation:")
relation_label.pack()
relation_entry = tk.Entry(root)
relation_entry.pack()

fds_label = tk.Label(root, text="Functional Dependencies:")
fds_label.pack()
fds_entry = tk.Entry(root)
fds_entry.pack()

# Function to mine candidate keys
def mine_candidate_keys():
    relation = set(relation_entry.get().replace(" ", "").split(','))
    fds = parse_fds(fds_entry.get())
    keys = candidate_keys(relation, fds)
    messagebox.showinfo("Candidate Keys", "Candidate keys:\n" + '\n'.join([''.join(key) for key in keys]))

# Create mine button
mine_button = tk.Button(root, text="Mine Candidate Keys", command=mine_candidate_keys)
mine_button.pack()

# Run the GUI
root.mainloop()

