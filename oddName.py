def main():
    name_input = input("Please enter your name")
    name_length = len(name_input)
    while name_length == 0:
        name_input = input("Please enter a valid name")
        name_length = len(name_input)
    for letter in range(1, name_length, 2):
        print(name_input[letter], end="")

main()








