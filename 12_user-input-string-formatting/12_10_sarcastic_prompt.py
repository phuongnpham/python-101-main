# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user_opinion = input("Please enter your honest opinion: ")
input_lower = user_opinion.lower()
sarcastic_message = " "
for i, char in enumerate(input_lower):
    if i % 2 == 0:
        sarcastic_message += char.lower()
    else:
        sarcastic_message += char.upper()
print(sarcastic_message)