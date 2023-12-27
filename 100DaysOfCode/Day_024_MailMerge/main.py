#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt",mode="r") as name:
    names = name.readlines()
    

with open("./Input/Letters/starting_letter.txt",mode="r") as letter:
    start_letter = letter.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = start_letter.replace(PLACEHOLDER, stripped_names)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)        
    

