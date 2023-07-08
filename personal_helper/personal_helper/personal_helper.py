# from .address_book.address_book import main as address_book
from .notes.notes import main as notes
# from .sort.sort import main as sort

def main():
    print("Hello, this is Personal Helper")
    print("Please write 'info' to get instructson about Personal Helper commands")
    
    while True:
        string = input("Enter command to Personal Helper: ").lower()
        if string in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif string == "info":
            print("Enter '1' to go to Address Book")
            print("Enter '2' to go to Notes")
            print("Enter '3' to go to Sorter")
        elif string.isdigit():
            if string == "1":
                print("You went to Address Book")
                # address_book() 
            elif string == "2":
                print("You went to Notes")
                notes()
            elif string == "3":
                print("You went to Sorter")
                # sort()
            else:
                print("invalid number")
        else:
            print("invalid command")

if __name__ == "__main__":
    main()