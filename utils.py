import os

def clear_screen():
    """
    Clears the terminal screen based on the OS.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_text(prompt):
    """
    Prompts for input and ensures it is NOT empty.
    """
    text = input(prompt).strip().upper()

    while not text:
        print('-' * 40)
        print('   ERROR: This field cannot be empty.')
        print('-' * 40)
        text = input(prompt).strip().upper()
    
    return text

def get_valid_int(prompt):
    """
    Tries to convert input to int. Returns None if invalid.
    """
    try:
        return int(input(prompt).strip())
    except ValueError:
        return None
    