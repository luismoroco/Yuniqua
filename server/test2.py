import sys
from io import StringIO


def execute_and_save_result(code):
    # Save the reference to the current stdout
    original_stdout = sys.stdout

    # Create a StringIO object to capture the output
    output_buffer = StringIO()
    sys.stdout = output_buffer

    try:
        # Execute the Python code
        exec(code)

        # Get the captured output as a string
        result_str = output_buffer.getvalue()
        return result_str

    except Exception as e:
        error_message = f"Error while executing the code:\n{str(e)}"
        return error_message

    finally:
        # Restore the original stdout
        sys.stdout = original_stdout


# Example Python code as a string
python_code = """
def add_numbers(a, b)g:
    return a + b

result = add_numbers(3, 4)
print(f"The result is: {result}")
"""

# Execute the code and get the result as a string
result_string = execute_and_save_result(python_code)

# Print or use the result string as needed
print(result_string)
