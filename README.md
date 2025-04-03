# Task 1: Read a File and Handle Errors 

1.  **Attempts to Open the File:**
    * The script uses a `try` block to attempt to open the file named `sample.txt` in read mode (`'r'`).

2.  **Reads and Prints Line by Line:**
    * If the file is opened successfully, the script prints the message `'reading file content:'`.
    * It then iterates through the file object `file1` using a `for` loop. This allows the script to read the file line by line, which is memory-efficient, especially for large files.
    * For each `line` read from the file, it is printed to the console using `print(line, end='')`.
        * `end=''` is used to prevent the `print()` function from adding an extra newline character after each line, as each line read from the file typically already includes one.

3.  **Closes the File:**
    * `file1.close()`: After reading all the lines, the script explicitly closes the file to release system resources.

4.  **Handles `FileNotFoundError`:**
    * `except FileNotFoundError:`: If the file `sample.txt` does not exist in the specified location, a `FileNotFoundError` will be raised. This `except` block catches this specific error.
    * `print('error: file not found!')`: If the file is not found, a user-friendly error message is printed to the console.

5.  **Handles Other Unexpected Errors:**
    * `except Exception as e:`: This is a general exception handler that catches any other unexpected errors that might occur during the file operations (e.g., permission issues, encoding errors).
    * `print(f'an unexpected error occurred:{e}')`: If any other error occurs, a generic error message along with the specific error details (`e`) is printed to the console, which can be helpful for debugging.

# Task 2: Write and Append Data to a File

1.  **Writes Initial Data:**
    * The script prompts the user to "enter text to write to the file:".
    * It opens a file named `output.txt` in **write mode (`'w'`)**. If the file exists, its contents will be overwritten. If it doesn't exist, a new file will be created.
    * The user's input is written to the `output.txt` file.
    * A confirmation message "data successfully written to output.txt" is printed.

2.  **Appends Additional Data:**
    * The script then prompts the user to "enter additional text to append:".
    * It opens the **same** file `output.txt` again, but this time in **append mode (`'a'`)**. This ensures that any new data is added to the end of the existing content.
    * A newline character (`\n`) is added before the additional user input to ensure that the appended text starts on a new line in the file.
    * The additional user input is written to the `output.txt` file.
    * A confirmation message "data successfully appended" is printed.

3.  **Reads and Displays Final Content:**
    * The script prints the message "final content of output.txt:".
    * It opens the `output.txt` file in **read mode (`'r'`)**.
    * It iterates through each line in the file using a `for` loop.
    * Each `line` is printed to the console. The `end=''` argument in the `print()` function prevents adding an extra newline character, ensuring the output matches the file's formatting.
