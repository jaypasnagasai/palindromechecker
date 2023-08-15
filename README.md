# Palindrome Checker

This is a simple Python program that allows you to check if a given word is a palindrome. A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Functions](#functions)
- [Example](#example)
- [License](#license)

## Description

The program consists of two functions:

1. `clean_string(s)`: This function takes an input string `s` and performs the following operations:
   - Removes punctuation marks.
   - Removes spaces.
   - Converts the string to lowercase.
   
   The cleaned string is returned as the result.

2. `is_palindrome(s)`: This function takes an input string `s` and checks whether it is a palindrome or not. It calls the `clean_string()` function to preprocess the input, then compares the cleaned input with its reverse to determine if it's a palindrome.

The program also includes a main loop for user interaction. It repeatedly prompts the user to enter a word, and after processing the input, it displays the original input, the cleaned version of the input, and the reversed version of the cleaned input. It then indicates whether the input is a palindrome or not.

## Usage

1. Clone this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the repository is cloned.
4. Run the Python script using the command: `python palindrome_checker.py`

## Functions

### `clean_string(s)`

This function takes a string `s` as input and returns a cleaned version of the string by removing punctuation, spaces, and converting it to lowercase.

### `is_palindrome(s)`

This function takes a string `s` as input, processes it using the `clean_string()` function, and checks if the cleaned string is a palindrome by comparing it to its reverse. It returns `True` if the input is a palindrome, and `False` otherwise.

## Example

Enter a word (or type 'exit' to quit): radar
Original: radar
Cleaned: radar
Reversed: radar
The word is a palindrome!

Enter a word (or type 'exit' to quit): hello
Original: hello
Cleaned: hello
Reversed: olleh
The word is not a palindrome!

Enter a word (or type 'exit' to quit): Exit
Original: Exit
Cleaned: exit
Reversed: tixe
The word is not a palindrome!

Enter a word (or type 'exit' to quit): exit

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
