def get_files_info(working_directory, directory="."):
    try:
        import os
        abs_wd_path = os.path.abspath(working_directory)
        full_wd_path = os.path.join(abs_wd_path, directory)
        norm_wd_path = os.path.normpath(full_wd_path)
        target_dir = os.path.normpath(os.path.join(abs_wd_path, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_wd_path, target_dir]) == abs_wd_path

        if (valid_target_dir == False):
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if (os.path.isdir(target_dir) == False):
            return (f'Error: "{directory}" is not a directory')
        
        dir_items = os.listdir(target_dir)
        files_info = []
        for i in dir_items:
            name = os.path.join(target_dir, i)
            size = os.path.getsize(name)
            is_dir = os.path.isdir(name)
            files_info.append(f"- {i}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"

get_files_info(working_directory="calculator", directory=".")
