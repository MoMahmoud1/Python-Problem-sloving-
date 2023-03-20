def program_name():
    print('\n**********  Unique Characters  ********** ')


def find_unique_characters(user_input):
    letters = {}
    keys = letters.fromkeys(user_input)
    for i in keys:
        if i in keys:
            print(f'{user_input} has {len(keys)} unique characters.')
        else:
            print("the words has only one unique character.")
        break


def main():
    program_name()
    while True:
        user_input = input("Enter your words: ")
        find_unique_characters(user_input)
        choice = input("enter choice to continue (y/n): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    print("Bye!")


if __name__ == "__main__":
    main()
