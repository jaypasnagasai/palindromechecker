import string

# Function to clean the input string by removing punctuation, spaces, and converting to lowercase
def clean_string(s):
    cleaned_input = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    return cleaned_input

# Function to check if a string is a palindrome
def is_palindrome(s):
    cleaned_input = clean_string(s)
    reversed_input = cleaned_input[::-1]
    return cleaned_input == reversed_input

# Main loop for user interaction
while True:
    user_input = input("Enter a word (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break  # Exit the loop if the user enters 'exit'
    
    print(f"Original: {user_input}")
    
    # Clean the user input
    cleaned_input = clean_string(user_input)
    reversed_input = cleaned_input[::-1]
    
    print(f"Cleaned: {cleaned_input}")
    print(f"Reversed: {reversed_input}")
    
    # Check if the cleaned input is a palindrome
    if is_palindrome(user_input):
        print("The word is a palindrome!")
    else:
        print("The word is not a palindrome.")
