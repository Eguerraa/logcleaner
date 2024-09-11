LogCleaner Utility

Overview
--------
LogCleaner is a tool that cleans a log file by removing lines containing specific phrases, as specified in the `config.ini` file. The tool reads this configuration file, scans the log file, and filters out any matching lines, saving the cleaned log in a new file in the same location as the original log file appending "_cleaned" to the cleaned file.


Files
-----
- LogCleaner.exe: The executable file for cleaning log files.
- config.ini: A configuration file that lists the phrases to be removed from the log.


How to Use
----------
1. **Prepare Your Log File:**
   - Place the log file you want to clean in the same directory as `LogCleaner.exe`, or note its full file path.
   
2. **Edit `config.ini`:**
   - Open the `config.ini` file and specify the phrases you want removed in the following format:

     ```
     [LINES_TO_REMOVE]
     lines = phrase1, phrase2, phrase3
     ```

   - Separate multiple phrases with commas.

   **Example:**

     ```
     [LINES_TO_REMOVE]
     lines = error, warning, timeout
     ```

   - Any line in the log file that contains any of the listed phrases will be removed.

3. **Run the Program:**
   - Open a terminal or command prompt.
   - Navigate to the folder where `LogCleaner.exe` is located.
   - Run the program using this command:

     ```
     LogCleaner.exe <path_to_log_file>
     ```

   - Replace `<path_to_log_file>` with the full path or relative path to your log file.

   **Example:**

     ```
     LogCleaner.exe C:\logs\log.txt
     ```

4. **Cleaned Log File:**
   - After running, a cleaned log file will be saved in the same directory as the original, with `_cleaned` added to the file name. For example:
     - Original: `log.txt`
     - Cleaned: `log_cleaned.txt`


How to Add or Remove Phrases in config.ini
------------------------------------------

1. **Adding Phrases:**
   - Open the `config.ini` file.
   - Add the new phrase to the `lines` list, separated by commas.

   **Example:**
     ```
     [LINES_TO_REMOVE]
     lines = error, warning, timeout, failure
     ```

2. **Removing Phrases:**
   - Delete any unwanted phrases from the `lines` section in `config.ini`.

   **Example:**
     ```
     [LINES_TO_REMOVE]
     lines = error, warning
     ```

   - Save the file after making any changes.


Error Handling
--------------

- If the specified log file cannot be found, an error message will be shown.
- If the `config.ini` file is missing or improperly formatted, the program will print an error message and exit.


Important Notes
---------------

- Ensure that the `config.ini` file is located in the same directory as `LogCleaner.exe`.
- The phrases in the `config.ini` file are case-sensitive.
