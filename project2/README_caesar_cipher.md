# Caesar Cipher Tool

A simple command-line tool written in Python that encrypts and decrypts text using the classic Caesar cipher (shift cipher).

**Author:** CyberTechSali

## Overview

This project was built to practice core Python fundamentals (loops, string manipulation, `ord()`/`chr()`, modular arithmetic) while exploring the foundations of encryption and decryption logic.

The Caesar cipher shifts each letter of the alphabet by a fixed number of positions (the "key"). It is one of the oldest and simplest encryption techniques, and a great starting point for understanding how modern cryptographic systems (like AES) evolved from these basic principles.

## Features

- Encrypts any text using a chosen shift key
- Decrypts the encrypted text back to the original
- Preserves spaces, numbers, and punctuation (they are not shifted)
- Handles both uppercase and lowercase letters correctly
- Runs in a loop, letting you test multiple messages in one session

## Requirements

- Python 3.x (no external libraries needed)

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/caesar-cipher.git
cd caesar-cipher
```

## Usage

Run the script:

```bash
python3 caesar_cipher.py
```

You will see a welcome banner, then be prompted to enter a text and a shift key. Type `quitter` at any time to exit.

### Example output

```
====================================================
   CAESAR CIPHER TOOL
   Author: CyberTechSali
   Encrypts and decrypts text using a shift (key)
   Type 'quitter' to exit
====================================================

Enter the text to encrypt (or 'quitter' to exit): Hello, World!
Enter the key (shift, e.g. 3): 3
Original text : Hello, World!
Encrypted text: Khoor, Zruog!
Decrypted text: Hello, World!
----------------------------------------
Enter the text to encrypt (or 'quitter' to exit): quitter
Closing the program. Goodbye!
```

## How it works

Each letter is converted to its position in the alphabet (A=0, B=1, ... Z=25) using `ord()`, shifted by the key, wrapped around using the modulo operator (`% 26`) so the shift loops back to the start of the alphabet when needed, then converted back to a letter using `chr()`:

```
Encryption: E(x) = (x + shift) % 26
Decryption: D(x) = (x - shift) % 26
```

Since the Caesar cipher is a **symmetric** cipher, the same key is used to both encrypt and decrypt — decryption is simply encryption with a negative shift.

Non-alphabetic characters (spaces, digits, punctuation) are left unchanged to avoid producing invalid output.

## Security limitations

The Caesar cipher is intentionally weak and used here for **learning purposes only**:

- Only 25 possible keys → trivial to brute-force
- Vulnerable to frequency analysis, since the shifted text preserves the same letter-frequency pattern as the original language
- Not suitable for any real-world confidentiality use case

Modern encryption (like AES) solves these weaknesses using much larger key spaces (128-bit+), confusion and diffusion techniques, and XOR-based operations rather than simple shifting.

## Possible improvements

- Add a brute-force decryption mode that tries all 25 keys automatically
- Add frequency analysis to guess the key without knowing it
- Implement a Vigenère cipher (multi-key version) as a next step
- Add file input/output support for encrypting entire text files

## License

This project is open source and available for learning purposes.
