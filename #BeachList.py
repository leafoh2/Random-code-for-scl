#Made by @67bf on dc

#beach list
beachList = ["towel", "sunscreen", "book", "water bottle", "hat"]

# Show the current list
print("Current beach list:", beachList)

# Keep asking until the user says no
answer = "yes"
while answer == "yes":
    answer = input("Do you want to add another item to the list? (yes or no): ")

    if answer == "yes":
        new_item = input("What item do you want to add? ")
        beachList.append(new_item)
        print("You added", new_item, "to the beach list.")

# Print how many items are in the list
print("There are", len(beachList), "items in the beach list.")
print ()
# Sort and print the list alphabetically
beachList.sort()
print("Beach list in alphabetical order:")
print ()
print(beachList)

