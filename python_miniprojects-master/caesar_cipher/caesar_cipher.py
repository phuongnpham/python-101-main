lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

secret_lowercase = secret.lower()

encrypted_secret = ""

for char in secret_lowercase:
    if char in lowercase_letters:
        index = (lowercase_letters.index(char) + cipher) % 26
        encrypted_secret += lowercase_letters[index]
    else:
        encrypted_secret += char

print(encrypted_secret)