names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

if "Sam" in names:
    print("Sam is present in the list.")
else:
    print("Sam is not present in the list.")

search_term = input("Enter a name to search for: ")
if search_term in names:
    print(f"{search_term} is present in the list.")
else:
    print(f"{search_term} is not present in the list.")
