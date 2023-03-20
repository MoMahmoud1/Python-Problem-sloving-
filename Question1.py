def program_name():
    print('\n**********  Province Postal Codes  ********** ')


def find_province(province_characters):
    postel_code = input("please enter the postel code as A1A 1A1 : ").upper()
    if postel_code[0] in province_characters.keys():
        if postel_code[1] == "0":
            print(f"the postal code is for an urban address in {province_characters[postel_code[0]]}.")
        elif postel_code[1] != "0":
            print(f"the postal code is for an rural address in {province_characters[postel_code[0]]}.")
    else:
        print("postel code not found, please try again ")


def main():
    province_characters = {'A': 'Newfoundland', 'B': 'Nova Scotia ', 'C': 'Prince Edward Island',
                           'E': 'New Brunswick', 'R': 'Manitoba ',
                           'S': 'Saskatchewan ', 'T': 'Alberta', 'V': 'British Columbia ',
                           'X': 'Nunavut or Northwest Territories', 'H': 'Quebec ', 'G': 'Quebec ', 'J': 'Quebec ',
                           'k': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario',
                           'Y': 'Yukon'}

    program_name()

    while True:
        find_province(province_characters)
        choice = input("enter choice to continue (y/n): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    print("Bye!")


if __name__ == "__main__":
    main()
