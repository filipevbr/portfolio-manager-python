import json
import datetime
from utils import clear_screen, get_valid_text, get_valid_int

# Constants
DATA_FILE = 'portfolio.json'

def load_data():
    """Loads projects from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(project_list):
    """Saves the project list to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(project_list, file, indent=4)
        print('-' * 40)
        print('SUCCESS: Data saved successfully.')
    except Exception as e:
        print(f'ERROR: Could not save data. {e}')

def display_menu():
    print('-' * 30)
    print('PORTFOLIO MANAGER - MAIN MENU')
    print('-' * 30)
    print('ADD    - Add new project')
    print('LIST   - List all projects')
    print('UPDATE - Update a project')
    print('DELETE - Remove a project')
    print('ABOUT  - About the app')
    print('QUIT   - Save & Exit')
    print('-' * 30)

def display_projects(project_list):
    """Helper to display the list, used in LIST, UPDATE and DELETE."""
    if not project_list:
        print('\nERROR: No projects found.\n')
        return False
    
    print('-' * 10, 'PROJECT LIST', '-' * 11)
    for index, project in enumerate(project_list, start=1):
        status_txt = 'Completed' if project['completed'] else 'Pending'
        print(f"{index}. {project['name']} - [{status_txt}]")
        
        # Show history
        if 'history' in project and project['history']:
             for date_log, desc in project['history']:
                 print(f"   - {date_log}: {desc}")
    print('-' * 35)
    return True

def add_project(project_list):
    print('-' * 10, 'ADD PROJECT', '-' * 10)
    
    quantity = get_valid_int("Enter number of projects to add: ")
    
    if quantity is None or quantity <= 0:
        print('\nERROR: Invalid number.\n')
        return

    for i in range(quantity):
        print(f"\n--- Project {i + 1} of {quantity} ---")
        name = get_valid_text("Enter project name: ")

        new_project = {
            'name': name,
            'completed': False,
            'history': []
        }
        
        project_list.append(new_project)
        print(f"SUCCESS: '{name}' added to portfolio.")

def update_project(project_list):
    print('-' * 10, 'UPDATE PROJECT', '-' * 10)
    
    if not display_projects(project_list):
        return

    project_id = get_valid_int("\nEnter the project NUMBER (ID) to update: ")

    if project_id is None or project_id < 1 or project_id > len(project_list):
        print('\nERROR: Project not found.\n')
        return

    target_project = project_list[project_id - 1]
    
    print(f"\nUPDATING: {target_project['name']}")
    print("1 - Rename Project")
    print("2 - Toggle Status (Pending/Completed)")
    print("3 - Cancel")
    
    option = get_valid_text("Choose an option: ")
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    match option:
        case '1':
            old_name = target_project['name']
            new_name = get_valid_text("Enter new name: ")
            target_project['name'] = new_name
            target_project['history'].append((now, f"Renamed: '{old_name}' -> '{new_name}'"))
            print(f"\nSUCCESS: Renamed to '{new_name}'.")
        case '2':
            target_project['completed'] = not target_project['completed']
            new_status = 'Completed' if target_project['completed'] else 'Pending'
            target_project['history'].append((now, f"Status changed to: {new_status}"))
            print(f"\nSUCCESS: Status updated to '{new_status}'.")
        case '3':
            return
        case _:
            print('\nERROR: Invalid option.')

def delete_project(project_list):
    print('-' * 10, 'DELETE PROJECT', '-' * 10)
    
    if not display_projects(project_list):
        return

    project_id = get_valid_int("\nEnter the project NUMBER (ID) to delete: ")

    if project_id is None or project_id < 1 or project_id > len(project_list):
        print('\nERROR: Project not found.\n')
        return

    target_project = project_list[project_id - 1]
    
    print(f"\nWARNING: You are about to delete '{target_project['name']}'.")
    confirm = get_valid_text("Type DELETE to confirm: ")
    
    if confirm == 'DELETE':
        removed = project_list.pop(project_id - 1)
        print(f"\nSUCCESS: '{removed['name']}' was removed.")
        save_data(project_list)
    else:
        print("\nOperation cancelled.")

def show_about():
    print('-' * 30)
    print('ABOUT')
    print('Portfolio Manager - Academic Project')
    print('Author: Filipe Vaz')
    print('Version: 2.0 (English + JSON)')
    print('-' * 30)

def main():
    # Load data when program starts
    projects = load_data()
    
    while True:
        clear_screen()
        display_menu()
        
        command = get_valid_text("\nEnter command: ")
        
        match command:
            case 'ADD':
                add_project(projects)
            case 'LIST':
                display_projects(projects)
            case 'UPDATE':
                update_project(projects)
            case 'DELETE':
                delete_project(projects)
            case 'ABOUT':
                show_about()
            case 'QUIT':
                save_data(projects)
                print('\nExiting application... Goodbye!')
                break
            case _:
                print('\nERROR: Invalid command.')
        
        input('\nPress ENTER to continue...')

if __name__ == "__main__":
    main()
    