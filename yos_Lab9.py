
def encode_password(password):
    encoded = ""
    for digit in password:
        dig = str((int(digit) + 3))
        encoded += dig
    return encoded


def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = int(input("Please enter your option: "))

        if choice == 1:
            decode = (input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        if choice == 2:
               print(f"The encoded password is: {encode_password(decode)}, and the original password is {decode}")
        if choice == 3:
            break


if __name__ == '__main__':
    main()
