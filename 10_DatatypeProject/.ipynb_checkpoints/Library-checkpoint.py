books = []

while True:
    print("\n=== Library System ===")
    print("1 Add Book")
    print("2 Issue Book")
    print("3 Return Book")
    print("4 Available Books")
    print("5 Display All Books")
    print("6 Exit")

    ch = input("Enter choice: ")

    # ADD BOOK
    if ch == "1":
        bid = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        book = {
            "id": bid,
            "title": title,
            "author": author,
            "issued": False
        }

        books.append(book)
        print(" Book Added Successfully")

    # ISSUE BOOK
    elif ch == "2":
        bid = int(input("Enter Book ID to Issue: "))
        found = False

        for b in books:
            if b["id"] == bid:
                found = True
                if b["issued"]:
                    print(" Book Already Issued")
                else:
                    b["issued"] = True
                    print(" Book Issued Successfully")
                break

        if not found:
            print(" Book Not Found")

    # RETURN BOOK
    elif ch == "3":
        bid = int(input("Enter Book ID to Return: "))
        found = False

        for b in books:
            if b["id"] == bid:
                found = True
                if not b["issued"]:
                    print(" Book was not issued")
                else:
                    b["issued"] = False
                    print(" Book Returned Successfully")
                break

        if not found:
            print(" Book Not Found")

    # AVAILABLE BOOKS
    elif ch == "4":
        print("\n Available Books:")
        available = False

        for b in books:
            if not b["issued"]:
                print(f"ID: {b['id']}, Title: {b['title']}, Author: {b['author']}")
                available = True

        if not available:
            print("No Available Books")

    # DISPLAY ALL BOOKS
    elif ch == "5":
        print("\n📚 All Books:")

        if len(books) == 0:
            print("No Books Found")
        else:
            for b in books:
                status = "Issued" if b["issued"] else "Available"
                print(f"ID: {b['id']}, Title: {b['title']}, Author: {b['author']}, Status: {status}")

    # EXIT
    elif ch == "6":
        print("Thank you for using Library System")
        break

    else:
        print(" Invalid Choice")