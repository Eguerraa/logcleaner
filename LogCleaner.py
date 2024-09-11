import sys
import os
import configparser

def get_executable_path():
    if getattr(sys, 'frozen', False):
        # If the application is frozen (compiled as an exe)
        return os.path.dirname(sys.executable)
    else:
        # If running in the script form (not compiled)
        return os.path.dirname(os.path.abspath(__file__))

def load_lines_from_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    
    # Get the lines from the config file
    lines = config.get('LINES_TO_REMOVE', 'lines')
    
    # Split the lines into a list, removing any leading/trailing whitespace
    lines_to_remove = [phrase.strip() for phrase in lines.split(',')]
    
    return lines_to_remove

def clean_log_file(input_filename, lines_to_remove):
    try:
        # Read the input file
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        
        # Filter out lines containing any of the lines
        cleaned_lines = [
            line for line in lines
            if not any(phrase in line for phrase in lines_to_remove)
        ]
        
        # Create the new filename
        base, ext = os.path.splitext(input_filename)
        output_filename = f"{base}_cleaned{ext}"
        
        # Write the cleaned lines to the new file
        with open(output_filename, 'w') as file:
            file.writelines(cleaned_lines)
        
        print(f"Cleaned file saved as {output_filename}")
    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_filename = sys.argv[1]
    
    # Get the directory where the executable or script is located
    script_dir = get_executable_path()
    
    # Set the config.ini file path in the same directory as the script/exe
    config_file = os.path.join(script_dir, 'config.ini')
    
    if os.path.isfile(input_filename):
        if os.path.isfile(config_file):
            lines_to_remove = load_lines_from_config(config_file)
            clean_log_file(input_filename, lines_to_remove)
        else:
            print(f"Configuration file {config_file} not found.")
    else:
        print(f"Invalid file. Please provide a valid file path.")
