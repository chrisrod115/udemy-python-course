import string

ALPHABET=string.ascii_lowercase

# encode/decode
def encode_decode(message, offset, en_de):
    res = "" 
    if en_de == 'decode':
        offset *= -1

    for char in message:
        char=char.lower()
        if char in ALPHABET:
            start_index= ALPHABET.find(char)
            new_index=(start_index+offset)%26
            res += ALPHABET[new_index]
        else:
            res+=char
                
    return res

# main
message = input("Enter your message: ")
offset = int(input("Enter the offset: "))
choice = input("Encode or Decode? (encode/decode): ").lower()

result = encode_decode(message, offset, choice)
print("Result:", result)