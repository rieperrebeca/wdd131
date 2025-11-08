
# 1.charapter types and number definitions
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
           "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?",
           "/", "`", "~"]
NUMBER = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 2 functions

# 2.1 Reads a file and sees if the word is in that file
def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_word = line.strip()
                if case_sensitive:
                    if word == line_word:
                        return True
                else:
                    if word.lower() == line_word.lower():
                        return True
    except FileNotFoundError:
        print(f"Warning: {filename} not found.")
    return False

# 2.2 See if that character is in the list of characters passed
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

# 2.3 Return complexity score (0–5)
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    if word_has_character(word, NUMBER):
        complexity += 1
    return complexity

# 2.4 Evaluate password strength
def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Check short password
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Check long password
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Calculate complexity
    complexity = word_complexity(password)
    strength = 1 + complexity

    return strength

# 2.5 Asks the user for a password to test
def main():
    print("Password Strength Checker")
    print("Enter a password to test or 'Q' to quit.")

    while True:
        password = input("\nPassword: ")

        if password.lower() == "q":
            print("Goodbye!")
            break

        strength = password_strength(password)
        print(f"Password Strength: {strength}/5")

        # Optional enhancement: log results to file
        with open("password_log.txt", "a", encoding="utf-8") as log:
            log.write(f"{password} -> {strength}\n")


# 3 testing team ensure your program runs correctly
if __name__ == "__main__":
    main()
