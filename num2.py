while True:

    print("****************************")
    print("SEARCH FILE")
    print("****************************")

    import os

    for root, dirs, files in os.walk(input(r"Enter directory path: ")):
        for file in files:
            # .pdf can be changed depending on what file is searching
            if file.endswith(".pdf"):
                print(os.path.join(root, file))

    a = input("Do you have another file to search? (YES/NO): ")
    print("\n")
    if a.upper() == 'YES':
        continue
    print("Thank you!")
    break
