alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = list(alphabet)
alphabet_list_length = len(alphabet_list)

def encode(message_to_encode_decode, secret_shift_number):
    encoded_message = ""
    for letter in message_to_encode_decode:
        if letter in alphabet_list:
            letter_index = alphabet_list.index(letter)
            encoded_index = (letter_index + secret_shift_number) % alphabet_list_length
            encoded_message += alphabet_list[encoded_index]
        else:
            encoded_message += letter
    print(f"The encoded message is: {encoded_message}\n")

def decode(message_to_encode_decode, secret_shift_number):
    decoded_message = ""
    for letter in message_to_encode_decode:
        if letter in alphabet_list:
            letter_index = alphabet_list.index(letter)
            decoded_index = (letter_index - secret_shift_number) % alphabet_list_length
            decoded_message += alphabet_list[decoded_index]
        else:
            decoded_message += letter
    print(f"The decoded message is: {decoded_message}\n")

cipher = True
while cipher:
    decode_or_encode = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: ")).strip().lower()
    message_to_encode_decode = str(input("Type your message: ")).strip().lower()
    secret_shift_number = int(input("Type your shift number: "))
    if decode_or_encode == "encode":
        encode(message_to_encode_decode, secret_shift_number)
    elif decode_or_encode == "decode":
        decode(message_to_encode_decode, secret_shift_number)
    else:
        print("Not valid option.\n")
        continue
    continue_or_not = str(input("Type 'yes' if you want to go again. Otherwise type 'no'. ")).strip().lower()
    if continue_or_not == "yes":
        continue
    else:
        cipher = False
