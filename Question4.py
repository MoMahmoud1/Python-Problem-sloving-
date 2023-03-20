def program_name():
    print('\n**********   Scrabble™ Score  ********** ')


def score(user_input, letters_points):
    total = 0
    for i in user_input:
        if i in letters_points.keys():
            total += letters_points[i]
    print(f'Total point score: {total}')


def main():
    letters_points = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
                      'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 1, 'P': 3,
                      'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5,
                      'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
    program_name()
    while True:
        user_input1 = input("Enter your words: ").upper()
        score(user_input1, letters_points)
        choice = input("enter choice to continue (y/n): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    print("Bye!")


if __name__ == "__main__":
    main()
