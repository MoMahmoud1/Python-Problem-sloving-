def program_name():
    print('\n**********  Text Messaging  ********** ')


def keys(user_input, key):
    for i in user_input:
        if i in key.keys():
            print(key[i], end="")


def main():
    key = {'.': '1', '?': '11', '!': '111', ':': '1111', 'A': '2', 'B': '22', 'C': '222',
           'D': '3', 'E': '33', 'F': '333', 'G': '4', 'H': '44', 'I': '444', 'J': '5', 'K': '55', 'L': '555',
           'M': '6', 'N': '66', 'O': '666', 'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
           'T': '8', 'U': '88', 'V': '888', 'W': '9', 'X': '99', 'Y': '999', 'Z': '9999', ' ': '0'}

    program_name()
    while True:
        user_input = input("Enter your words: ").upper()
        keys(user_input, key)
        choice = input("\nenter choice to continue (y/n): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    print("Bye!")


if __name__ == "__main__":
    main()
