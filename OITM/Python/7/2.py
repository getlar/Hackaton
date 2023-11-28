with open('hexa.txt', 'r') as file:
    hex_codes = file.read().split()

# Convert hex to characters
text_characters = [chr(int(code, 16)) for code in hex_codes]

# Join characters to form the original text
original_text = ''.join(text_characters)

# Print or use the original text
print(original_text)

print(int(105546/(2023 + 49*10)))