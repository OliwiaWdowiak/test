secret_word = "apple"
user_word = ""
user_word_count = 0
user_word_limit = 3
attemps = False

while user_word != secret_word and not(attemps):
    if user_word_count < user_word_limit:
        user_word = input("Enter a word: ")
        user_word_count += 1
    else:
        attemps = True

if attemps:
    print("You lost")
else:
    print("You win")
