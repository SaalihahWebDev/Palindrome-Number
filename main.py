def is_palindrome_number(number):
    return number==number[::-1]
def start_game():
    print("Welcome to palindrome number game🎉🎉🎉")
    while True:
        number=input("🔢🔢🔢🔢Enter a number to check if it is a palindrome or type'Exit' to not play❌❌❌❌: ")
        if number.lower()=="exit":
            print("Thanks for playing 🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻")
            break
        if not number.isdigit():
            print("Enter numbers only.No symbols allowed🚫🚫🚫🚫")
            continue
        if is_palindrome_number(number):
            print(f"Yes,{number} is a palindromic number\n")
        else:
            print(f"No,{number} isnot a palindromic number\n")
start_game()