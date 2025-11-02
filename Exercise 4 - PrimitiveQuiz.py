quiz = [
    ("France", "Paris"),("Germany", "Berlin"),("Italy", "Rome"),("Spain", "Madrid"),("Portugal", "Lisbon"),
    ("Greece", "Athens"),("Netherlands", "Amsterdam"),("Belgium", "Brussels"),("Austria", "Vienna"),("Sweden", "Stockholm")
]
for country, capital in quiz:
    answer = input(f"What is the capital of {country}? ")
    if answer.casefold() == capital.casefold():
        print("Congrats, you got the correct answer!")
    else:
        print(f"Wrong answer. The correct answer is {capital}.")


