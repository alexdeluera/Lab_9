def encode(password):
    new_str=""
    for char in password:
        new_num=int(char)+3
        new_str+=str(new_num)
    return new_str

def decode(password):
    old_password = []
    for char in password:
        char = int(char)
        if 3 <= char <= 9:
            char = str(char - 3)
        elif char == 0:
            char = "7"
        elif char == 1:
            char = "8"
        elif char == 2:
            char = "9"
        old_password.append(char)
    original = ''.join(old_password)
    return password, original

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
