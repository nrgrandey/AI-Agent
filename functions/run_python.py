import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory = os.path.abspath(working_directory)
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not target_file_path.startswith(working_directory):
            return f"Error: Cannot execute '{file_path}' as it is outside the permitted working directory"

        # Ensure the file exists
        if not os.path.isfile(target_file_path):
            return f"Error: File '{file_path}' not found"

        # Ensure the file is a Python file
        if not target_file_path.endswith('.py'):
            return f"Error: '{file_path}' is not a Python file"

        # Prepare the command to run the Python file
        command = ['python', target_file_path] + args

        # Run the command
        result = subprocess.run(command, timeout=30, cwd=working_directory, text=True, stdout=True, stderr=True)

        stdout = f"STDOUT:\n{result.stdout}" if result.stdout else "STDOUT:\n"
        stderr = f"STDERR:\n{result.stderr}" if result.stderr else "STDERR:\n"

        if result.returncode == 0:
            if stdout:
                return f"Output from '{target_file_path}':\n{stdout}"
            else:
                return f"'{target_file_path}' executed successfully with no output."
        else:
            return f"Process exited with code {result.returncode}"
    except Exception as e:
        return f"Error: {str(e)}"