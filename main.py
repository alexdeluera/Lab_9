def encode(password):
    new_str=""
    for char in password:
        new_num=int(char)+3
        new_str+=str(new_num)
    return new_str

def decode(password):
    #to be filled in by partner
    pass

def main():
    option=0
    
    while option!=3:
        print("\nMenu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        option=int(input("Please enter an option: "))
        if option==1:
            password=input("Please enter your password to encode: ")
            encode_pass=encode(password)
            print("Your password has been encoded and stored!")
        elif option==2:
            print(f"The encoded password is {encode_pass}, and the original password is {decode(encode_pass)}.")
        else:
            break

if __name__=="__main__":
    main()