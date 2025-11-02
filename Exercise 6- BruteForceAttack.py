correct_password = "nicoganda"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Password correct. Access granted.")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. You have {remaining} attempts remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")
