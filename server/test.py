import sys


def execute_and_save_result(code, output_file):
    # Save the reference to the current stdout
    original_stdout = sys.stdout

    with open(output_file, "w") as file:
        sys.stdout = file

        try:
            # Open the output file for writing

            # Execute the Python code
            exec(code)

        except Exception as e:
            print(f"Error while executing the code:\n{str(e)}")
        finally:
            # Restore the original stdout
            sys.stdout = original_stdout


# Example Python code as a string
python_code = """
def add_numbers(a, b)x:
    return a + b

result = add_numbers(3, 4)
print(f"The result is: {result}")
"""

# Specify the name of the output file
output_file_name = "output.txt"

# Execute the code and save the result to a file
execute_and_save_result(python_code, output_file_name)
