import os
from config import MAX_FILE_CHARACTERS
def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not target_file_path.startswith(working_directory):
            return f"Error: Cannot access '{target_file_path}' as it is outside the permitted working directory"

        if not os.path.isfile(target_file_path):
            return f"Error: 'File not found or is not a regular file: '{target_file_path}'"

        with open(target_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if len(content) > MAX_FILE_CHARACTERS:
            content = content[:MAX_FILE_CHARACTERS] + f"\n\n[File '{target_file_path}' truncated to the first 10,000 characters]"

        return content
    except Exception as e:
        return f"Error: {str(e)}"
