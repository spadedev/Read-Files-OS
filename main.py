while True:
    print("********************************")
    print("COUNT STRINGS")
    print("********************************")

    f = open("Message")

    content = f.read()

    search = input("Enter a string to search: ")

    count = content.count(search)

    print("Number of times the string appears:", count)
    print("\n")

    choice = input("Do you have another string? (YES/NO): ")

    if choice.upper() == 'YES':
        continue
    print("Thank you!")
    break

