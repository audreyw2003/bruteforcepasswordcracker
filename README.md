# Brute Force Password Cracker

## Overview

This project is a simple brute force password cracker written in Python. It generates a specified number of random passwords and compares them to a target password to determine if it can be cracked.

## Features

- Generates random passwords of a specified length.
- Saves generated passwords to a text file (`passwordlist.txt`).
- Compares generated passwords to a target password.
- Prints whether the target password was cracked or not.

## Requirements

- Python 3.x

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Script:**

   ```bash
   python password_cracker.py
   ```

3. **Input Prompts:**

   - Enter the target password you want to attempt brute force on.
   - Enter the number of passwords to generate for comparison during brute force.

4. **Output:**

   - The script will generate the specified number of passwords and save them to `passwordlist.txt`.
   - It will then compare each generated password to the target password.
   - It will then print whether the password was cracked.

### Functions

1. **`save_pass_list(pass_list)`**:
   - Saves the generated passwords to `passwordlist.txt`.

2. **`brute_force(target_password, num_passwords)`**:
   - Generates passwords and compares them to the target password.
   - Returns the target password if cracked, otherwise `None`.

3. **`generate_passwords(num_passwords)`**:
   - Generates a list of random passwords of length 15.

4. **`main()`**:
   - Prompts the user for the target password and the number of passwords to generate.
   - Executes the brute force attack and prints the result.

## Notes

- Use this script responsibly and ethically. Only attempt to crack passwords on systems where you have explicit permission.
- Brute force attacks are computationally expensive and time-consuming. Consider using them as a last resort.

---

