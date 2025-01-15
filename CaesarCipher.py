"""def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    text = input("Enter the text: ").strip()
    key = int(input("Enter the key: ").strip())

    if choice == 'encrypt':
        print("Encrypted text:", encrypt(text, key))
    elif choice == 'decrypt':
        print("Decrypted text:", decrypt(text, key))
    else:
        print("Invalid choice")

"""
import requests
import string
from collections import Counter

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decrypted_text += char
    return decrypted_text

def try_all_shifts(text):
    shifted_texts = {}
    for shift in range(26):
        shifted_texts[shift] = caesar_cipher_decrypt(text, shift)
    return shifted_texts

def is_english_word(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    return response.status_code == 200

def count_english_words(text):
    words = text.split()
    english_word_count = 0
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if is_english_word(cleaned_word):
            english_word_count += 1
    return english_word_count

def find_best_shift(shifted_texts):
    best_shift = None
    max_english_words = 0
    for shift, text in shifted_texts.items():
        english_word_count = count_english_words(text)
        if english_word_count > max_english_words:
            max_english_words = english_word_count
            best_shift = shift
    return best_shift

def frequency_analysis(text):
    frequencies = Counter(text)
    most_common = frequencies.most_common(1)[0][0]
    assumed_space = ' '
    shift = (ord(most_common) - ord(assumed_space)) % 26
    return shift

# Encrypted message
encrypted_message = "BRXFD QQRWO RVHDK RPLQJ SLJHR Q.LIB RXUKR PLQJS LJHRQ GRHVQ RWFRP HEDFN ,WKHQ ZKDWB RXKDY HORVW LVDSL JHRQ"

shifted_results = try_all_shifts(encrypted_message)
best_shift = find_best_shift(shifted_results)
print(f"The best shift is: {best_shift}")
print(f"Decrypted message: {shifted_results[best_shift]}")
def brute_force_decrypt(encrypted_message):
    shifted_texts = try_all_shifts(encrypted_message)
    best_shift = find_best_shift(shifted_texts)
    decrypted_message = shifted_texts[best_shift]
    
    max_english_words = 0
    best_decryption = ""
    
    for length in range(1, len(decrypted_message) + 1):
        for start in range(len(decrypted_message) - length + 1):
            substring = decrypted_message[start:start + length]
            english_word_count = count_english_words(substring)
            if english_word_count > max_english_words:
                max_english_words = english_word_count
                best_decryption = substring
    
    return best_decryption

best_decryption = brute_force_decrypt(encrypted_message)
print(f"Best decryption: {best_decryption}")