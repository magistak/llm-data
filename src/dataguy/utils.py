def validate_file_path(file_path):
    """
    Validate that a file exists and is readable.
    
    Args:
        file_path (str): Path to the file to validate
        
    Returns:
        bool: True if file exists and is readable
        
    Raises:
        FileNotFoundError: If file doesn't exist
        PermissionError: If file isn't readable
    """
    import os
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"File is not readable: {file_path}")
    
    return True
