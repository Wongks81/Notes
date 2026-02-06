
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def main():
    restart = True
    restart_reply = "y"
    while restart:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction=direction,text=text,shift=shift)
        while restart_reply != "n":
            # While loop to check for only Y or N  
            restart_reply = input("Do you want to rerun the program? Y or N : ").lower()
            if restart_reply == "y":
                restart = True
                break
            elif restart_reply == "n":
                restart = False
                break
            else:
                print("Please enter Y or N only!")
                continue



def encrypt(text, shift):
    cipher_text = ""

    ## Loop through each character in the entered text
    for char in text:
        ## Find the index of the char with reference to alphabet list
        text_index = alphabet.index(char)

        ## Add shift to index for the cipher, % 26 is to cater for letters that overflow.
        cipher_text += alphabet[(text_index + shift) % 26]

    print(cipher_text)

def decrypt(text,shift):
    plain_text = ""
    for char in text:
        ## Find the index of the char with reference to alphabet list
        text_index = alphabet.index(char)

        ## Add shift to index for the cipher, % 26 is to cater for letters that overflow.
        plain_text += alphabet[(text_index - shift) % 26]
    
    print(plain_text)

def caesar(direction,text,shift):
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)

if __name__ == "__main__":
    main()