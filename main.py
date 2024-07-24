def encode(password):
    new_str=""
    for char in password:
        new_num=int(char)+3
        new_str+=str(new_num)
    return new_str

print(encode("12345555"))