name = input("Enter your full name (first and surname): ")
hometown = input("Enter your hometown: ")

while True:
    age_input = input("Enter your age (number only): ")
    if age_input.isdigit():
        age = int(age_input)  
        break
    else:
        print("Invalid input. Please enter a numeric age.")

# Store data in a dictionary
biography = {
    "name": name,
    "hometown": hometown,
    "age": age
}
print(biography["name"], biography["hometown"], biography["age"], sep="\n")

