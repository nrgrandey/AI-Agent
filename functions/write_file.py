import os

def write_file(working_directory, file_path, content):
    try:
        working_directory = os.path.abspath(working_directory)
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not target_file_path.startswith(working_directory):
            return f"Error: Cannot write to '{target_file_path}' as it is outside the permitted working directory"

        # Ensure the directory exists
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        with open(target_file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        return f"Succesfully wrote to '{target_file_path}' ({len(content)} characters written)"
    except Exception as e:
        return f"Error: {str(e)}"
