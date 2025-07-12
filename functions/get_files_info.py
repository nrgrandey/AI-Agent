import os
def get_files_info(working_directory, directory=None):
    try:
        working_directory = os.path.abspath(working_directory)
        target_directory = os.path.abspath(os.path.join(working_directory, directory or ""))

        if not target_directory.startswith(working_directory):
            return f"Error: Cannot list '{target_directory}' as it is outside the permitted working directory."

        if not os.path.isdir(target_directory):
            return f"Error: '{target_directory}' is not a directory."

        files_list = os.listdir(target_directory)
        files_info = []

        for file_name in files_list:
            file_path = os.path.join(target_directory, file_name)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                files_info.append({
                    "name": file_name,
                    "size": file_size,
                    "is_dir": False
                })
            elif os.path.isdir(file_path):
                file_size = os.path.getsize(file_path)
                files_info.append({
                    "name": file_name,
                    "size": file_size,
                    "is_dir": True
                })

        if directory == ".":
            result = "Result for current directory:"
        else:
            result = f"Result for '{directory}' directory:"


        for file in files_info:
            result += f"\n - {file['name']}: file_size={file['size']} bytes, is_dir={file['is_dir']}"
        return result
    except Exception as e:
        return f"Error: {str(e)}"
