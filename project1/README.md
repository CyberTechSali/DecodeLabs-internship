# Password Strength Checker

A simple command-line tool written in Python that evaluates whether a password is **weak**, **medium**, or **strong** based on length and character composition.

**Author:** CyberTechSali

## Overview

This project was built to practice core Python fundamentals (strings, conditionals, loops, functions) while exploring basic password security concepts, such as:

- Minimum length enforcement
- Character diversity (uppercase letters, digits, symbols)
- Why weak passwords are a common entry point in real-world breaches

## Features

- Classifies any password as **weak**, **medium**, or **strong**
- Checks for:
  - Minimum length (8+ characters)
  - At least one uppercase letter
  - At least one digit
  - At least one symbol
- Runs in a loop, letting you test multiple passwords in one session
- Simple, readable code — ideal for beginners

## Requirements

- Python 3.x (no external libraries needed)

## Installation

```bash
git clone https://github.com/CyberTechSali/password-strength-checker.git
cd password-strength-checker
```

## Usage

Run the script:

```bash
python3 password_checker.py
```

You will see a welcome banner, then be prompted to enter a password. Type `quitter` at any time to exit.

### Example output

```
====================================================
   PASSWORD STRENGTH CHECKER
   Author: CyberTechSali
   Checks whether a password is weak, medium, or strong
   Type 'quitter' to exit
====================================================

Enter a password (or 'quitter' to exit): abc123
Password strength: weak
----------------------------------------
Enter a password (or 'quitter' to exit): Tr0ub4dor!X9
Password strength: strong
----------------------------------------
Enter a password (or 'quitter' to exit): quitter
Closing the program. Goodbye!
```

## How it works

The tool checks four criteria:

1. Length ≥ 8 characters
2. Contains at least one uppercase letter
3. Contains at least one digit
4. Contains at least one non-alphanumeric symbol

A password shorter than 8 characters is automatically classified as **weak**, regardless of the other criteria. Otherwise, the password is scored based on how many of the remaining criteria it meets:

- 0–2 criteria met → weak
- 3 criteria met → medium
- 4 criteria met → strong

 ![Terminal demo](project1/password-check.png)

## Possible improvements

- Add protection against timing attacks using `hmac.compare_digest()`
- Validate input before hashing (gatekeeper principle)
- Expand character checks to support Unicode characters
- Add a graphical interface

## License

This project is open source and available for learning purposes.
