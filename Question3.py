def program_name():
    print('\n**********  Anagrams  ********** ')


def anagrams_tester(user_input1, user_input2):
    first_word = {}
    second_word = {}
    first_word_keys = first_word.fromkeys(user_input1)
    second_word_keys = second_word.fromkeys(user_input2)
    if sorted(first_word_keys) == sorted(second_word_keys):
        print(f'{user_input1} and {user_input2} are anagrams')
    else:
        print(f'{user_input1} and {user_input2} are not  anagrams')


def main():
    program_name()
    while True:
        user_input1 = input("Enter your first word: ")
        user_input2 = input("Enter your second word: ")
        anagrams_tester(user_input1, user_input2)
        choice = input("enter choice to continue (y/n): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    print("Bye!")

if __name__ == "__main__":
    main()
