def analyze_sentence(sentence):  # Define a function to analyze the sentence
    words = sentence.split()  # Split the sentence into words
    num_words = len(words)  # Count the number of words
    num_chars = len(sentence)  # Count the number of characters
    return num_words, num_chars  # Return the number of words and characters

def main():
    while True:
        try:  # Start a try block to catch exceptions
            sentence = input("Please enter a sentence: ").strip()  # Prompt the user to enter a sentence and strip leading/trailing whitespace
            if not sentence:  # Check if the input is empty
                raise ValueError("The input cannot be empty.")  # Raise a ValueError if the input is empty
            if not sentence.replace(" ", "").isalpha():  # Check if the input contains only alphabetic characters and spaces
                raise ValueError("The input contains invalid characters. Only alphabetic characters and spaces are allowed.")  # Raise a ValueError if the input contains invalid characters
            
            num_words, num_chars = analyze_sentence(sentence)  # Analyze the sentence
            print(f"The sentence has {num_words} words and {num_chars} characters.")  # Print the analysis results
            break  # Exit the loop
        except ValueError as e:  # Catch ValueError exceptions
            print(e)  # Print the error message

if __name__ == "__main__":
    main()