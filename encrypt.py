def encrypt_text(text: str, key: int, start_column: int) -> str:
    """
    Encrypt text using transposition method.
    
    Args:
        text: Text to encrypt
        key: Number of columns (key)
        start_column: Column to start reading from (1-based)
    
    Returns:
        Encrypted text
    """
    # Remove any existing newlines and spaces at the end
    text = text.rstrip()
    
    # Calculate number of rows needed
    text_length = len(text)
    rows = (text_length + key - 1) // key
    
    # Pad text with spaces if needed
    padded_length = rows * key
    text = text.ljust(padded_length)
    
    # Create matrix
    matrix = []
    for i in range(rows):
        start = i * key
        end = start + key
        matrix.append(list(text[start:end]))
    
    # Read by columns starting from specified column
    result = []
    current_col = start_column - 1  # Convert to 0-based index
    
    for _ in range(key):
        for row in matrix:
            result.append(row[current_col])
        current_col = (current_col + 1) % key
    
    return ''.join(result)

def decrypt_text(encrypted_text: str, key: int, start_column: int) -> str:
    """
    Decrypt text using transposition method.
    
    Args:
        encrypted_text: Text to decrypt
        key: Number of columns (key)
        start_column: Column that was used to start reading from (1-based)
    
    Returns:
        Decrypted text
    """
    # Calculate number of rows
    text_length = len(encrypted_text)
    rows = text_length // key
    
    # Create matrix
    matrix = [['' for _ in range(key)] for _ in range(rows)]
    
    # Fill matrix by columns
    current_col = start_column - 1  # Convert to 0-based index
    text_index = 0
    
    for _ in range(key):
        for row in range(rows):
            matrix[row][current_col] = encrypted_text[text_index]
            text_index += 1
        current_col = (current_col + 1) % key
    
    # Read matrix by rows
    result = []
    for row in matrix:
        result.extend(row)
    
    # Remove trailing spaces
    return ''.join(result).rstrip()
