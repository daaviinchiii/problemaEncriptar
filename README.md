# Text Encryption/Decryption Program

This program implements a transposition cipher for text encryption and decryption. It reads text from a file, encrypts it using the specified key and starting column, and then verifies the encryption by decrypting the text.

## Features

- Text encryption using transposition method
- Text decryption
- File I/O support
- Input validation
- Verification of encryption/decryption process

## Requirements

- Python 3.6 or higher

## Usage

1. Create a text file with the content you want to encrypt
2. Run the program:
   ```bash
   python main.py
   ```
3. When prompted:
   - Enter the input file name
   - Enter the encryption key (number of columns)
   - Enter the starting column (1 to key)

## Output

The program will:
1. Read the text from the input file
2. Encrypt the text
3. Decrypt the text to verify
4. Save the encrypted text to `encrypted.txt`
5. Save the decrypted text to `decrypted.txt`
6. Display all three versions (original, encrypted, and decrypted) in the console

## Example

Input file (`input.txt`):
```
Encriptação por transposição
```

Running the program with:
- Key: 5
- Starting column: 3

Will produce:
- Encrypted text in `encrypted.txt`
- Decrypted text in `decrypted.txt`
- Console output showing all three versions

## Notes

- The program handles UTF-8 encoding for proper character support
- All characters, including newlines, are considered in the encryption
- The program verifies that the decrypted text matches the original # problemaEncriptar.
