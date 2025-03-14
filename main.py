from encrypt import encrypt_text, decrypt_text

def read_file(filename: str) -> str:
    """Read text from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)

def write_file(filename: str, content: str) -> None:
    """Write text to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file: {e}")
        exit(1)

def get_user_input() -> tuple[int, int]:
    """Get key and start column from user input."""
    while True:
        try:
            key = int(input("Enter the encryption key (number of columns): "))
            if key <= 0:
                print("Key must be positive.")
                continue
                
            start_column = int(input(f"Enter the starting column (1 to {key}): "))
            if not 1 <= start_column <= key:
                print(f"Starting column must be between 1 and {key}.")
                continue
                
            return key, start_column
        except ValueError:
            print("Please enter valid numbers.")

def main():
    # Get input file name
    input_file = input("Enter the input file name: ")
    
    # Read text from file
    text = read_file(input_file)
    
    # Get encryption parameters
    key, start_column = get_user_input()
    
    # Encrypt text
    encrypted = encrypt_text(text, key, start_column)
    
    # Decrypt text to verify
    decrypted = decrypt_text(encrypted, key, start_column)
    
    # Write results to files
    write_file("encrypted.txt", encrypted)
    write_file("decrypted.txt", decrypted)
    
    # Print results
    print("\nOriginal text:")
    print(text)
    print("\nEncrypted text:")
    print(encrypted)
    print("\nDecrypted text:")
    print(decrypted)
    
    # Verify if decryption worked
    if text == decrypted:
        print("\nVerification successful: Decrypted text matches original text!")
    else:
        print("\nWarning: Decrypted text does not match original text!")

if __name__ == "__main__":
    main() 