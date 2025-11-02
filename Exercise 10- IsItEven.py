def is_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    try:
        user_input = int(input("Enter a number: "))
        result = is_even_or_odd(user_input)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()