# Lab-5_A-3

# create a function that attempts to modify a global numerical variable without global.

# describe the problem.

# rewrite to return new value instead.

# global numeric variable

global_numeric = 10

def mod_attempt():
    global_numeric = global_numeric / 2
    return global_numeric

mod_attempt() # UnboundLocalError: cannot access local variable 'global_numeric' where it is not associated with a value
# removing global_numeric = 10 would give the same error

# corrected version:
global_numeric = 10

def mod_attempt():
    global_numeric_2 = global_numeric / 2
    print(global_numeric_2)

mod_attempt()
