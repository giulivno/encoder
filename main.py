
def encode(password):


    encoded_password = ""

    # Encode password
    for i in password[:]:
        encoded_password = encoded_password + str(int(i)+3)

    print("Your password has been encoded and stored")

    return encoded_password

def decode(encoded):
    decoded = ""
    for num in encoded:
        num = int(num)
        new = 0
        if num > 2:
            new = str(int(num) - 3)
            decoded += new
        elif num == 0:
            new = "7"
            decoded += new
        elif num == 1:
            new = "8"
            decoded += new
        elif num == 2:
            new = "9"
            decoded += new
    return decoded

def main():

    choice = 0
    while True:
        print("\nMenu\n-------------\n1. Encode"
              "\n2. Decode\n3. Quit")
        choice = int(input("\nPlease enter an option: "))

        if choice == 1:
            password = input("Please enter you password to encode: ")
            encoded = encode(password)
        if choice == 2:
            #Decoded - Griffin Pitts
            decoded = decode(encoded)
            print(f"\nThe encoded password is {encoded}, and "
                  f"the orginal password is {decoded}.")
        if choice == 3:
            exit()

main()
