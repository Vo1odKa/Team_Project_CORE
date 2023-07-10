from collections import UserDict
from datetime import datetime
import pickle
import re

tutorial = '''
Available commands:
"add [name]* [phones]** [emails]** [birthday]** [address]**" - adds a new contact to the address book
 name - no more than three words
 phones - can be several (each must contain 10 to 12 digits), enter with a space
 emails - can be several, enter with a space
 birthday - date in format dd/mm/yyyy (must be only one)
 address - must contain street and house number, all elements must be separated by a slash and start with a slash (example: /Country/City/Street/House)
"phone [name]*" - shows phone numbers of a particular contact
"find [any piece of information]*" - search for matches among existing contacts
"when birthday [name]*" - calculates the number of days until the contact's next birthday
"days until birthday: [any number]*" - displays the names of contacts whose birthday is in the specified number of days
"change ('phone'/'email'/'birthday'/'address') [name]* [phone/email/birthday/address]*" - change any contact's data
"delete ('phone'/'email'/'birthday'/'address') [name]* [phone/email/birthday/address]*" - delete any contact's data
"show all" - show you full list of contacts in the address book
"good bye", "bye", "close", "exit" or "end" - exit the address book and save it in file "address_book.bin"
* - mandatory field      ** - optional field    '''

# Об'єкти класу "адресна книга"
class AddressBook(UserDict):
    # Функція, що записує контакт до адресної книги
    def add_record(self, Record):
        self.update({Record.Name.name: Record})
        return "Done!"

    # Функція, що виводить Номери телефону певного контакту
    def show_number(self, Name):
        return self.data[Name.name].Phones.phone

    # Функція, що виводить спbсок всіх контактів, що містяться у адресній книзі
    def show_all(self):
        for name, info in self.data.items():
            yield f'{name}: {info.Phones.phone} {info.Emails.email} {info.Birthday.birthday} {info.Address.address}'

    # Функція, що шукає контакти, які містять певну послідовність літер в умені контакту, або чисел у його телефонних номерах
    def find(self, piece_of_info):
        res = []
        for name, numbers in self.data.items():
            if piece_of_info in ' '.join([name, str(numbers.Phones.phone), str(numbers.Emails.email), str(numbers.Birthday.birthday), str(numbers.Address.address)]):
                res.append(name)
        if res:
            for name in res:
                print(f'{name}: {self.data[name].Phones.phone} {self.data[name].Emails.email} {self.data[name].Birthday.birthday} {self.data[name].Address.address}')
        else:
            print('No matches')

    # Функція, що виводить імена контактів, у яких день народження через певну кількість днів
    def birthday_after_n_days(self, days):
        contacts = ''
        for contact in self.data:
            if int(self.data[contact].days_to_birthday().split(' ')[1]) == int(days):
                contacts += contact + ' and '
        if contacts:
            return f'{contacts.removesuffix(" and ")} will have birthday in this day'
        else:
            return 'No one celebrates their birthday on this day'

# Об'єкти класу "контакт", що міститеме всю інформацію про нього
class Record:
    def __init__(self, Name, Phones=None, Birthday=None, Emails=None, Address=None):
        self.Name = Name
        self.Phones = Phones
        self.Birthday = Birthday
        self.Emails = Emails
        self.Address = Address

    # функція, що додає номер телефону до контакту
    def add_phone(self, Phone):
        self.Phones.phone = list(set(self.Phones.phone) | set(Phone.phone))
        return "Done!"

    # Функція, що змінює наявні номери телефону на нові
    def change_phone(self, Phone):
        self.Phones = Phone
        return "Done!"

    # Функція, що видаляє наявний номер телефону
    def delete_phone(self, Phone):
        self.Phones.phone = list(set(self.Phones.phone) - set(Phone.phone))
        return "Done!"
    
    # Функція, що змінює день народження на новий
    def change_birthday(self, Birthday):
        self.Birthday = Birthday
        return "Done!"

    # Функція, що видаляє наявний день народження
    def delete_birthday(self, Birthday):
        self.Birthday.birthday = list(set(self.Birthday.birthday) - set(Birthday.birthday))
        return "Done!"
    
    # Функція, що змінює наявні email на нові
    def change_email(self, Email):
        self.Emails = Email
        return "Done!"

    # Функція, що видаляє наявний email
    def delete_email(self, Email):
        self.Emails.email = list(set(self.Emails.email) - set(Email.email))
        return "Done!"
    
    # Функція, що змінює наявну адресу
    def change_address(self, Address):
        self.Address = Address
        return "Done!"

    # Функція, що видаляє наявну адресу
    def delete_address(self, Address):
        self.Address.address = list(set(self.Address.address) - set(Address.address))
        return "Done!"

    # Функція, що розраховує кількість днів до наступного дня нородження контакта
    def days_to_birthday(self):
        if self.Birthday.birthday:
            current_datetime = datetime.now()
            birthday = datetime.strptime(self.Birthday.birthday, '%d/%m/%Y')
            if int(current_datetime.month) > int(birthday.month) or (int(current_datetime.month) == int(birthday.month) and int(current_datetime.day) >= int(birthday.day)):
                next_birthday = datetime(
                    year=current_datetime.year+1, month=birthday.month, day=birthday.day)
                return f"In {(next_birthday - current_datetime).days} days"
            else:
                next_birthday = datetime(
                    year=current_datetime.year, month=birthday.month, day=birthday.day)
                return f"In {(next_birthday - current_datetime).days} days"
        else:
            return "The birthsay date is unknown."


# Після отримання введеної користувачем команди та відокремлення від неї слова-ключа, отримана інформація сортується за критеріями
class Field:
    def __init__(self, data):
        # Відокремлюються всі слова та обєднує їх у "ім'я" контакту
        self.name = re.findall(r'[a-z]+\s?[a-z]+\s?[a-z]+', data)[0]
        # Відокремлюються всі номери
        self.phone = re.findall(r'\b\d{10,12}\b', data)
        # Відокремлення дату, що має формат дд/мм/рррр (мається на увазі, що вона має бути введена тільки одна)
        self.birthday = re.findall(r'\d{2}\/\d{2}\/\d{4}', data)
        # Відокремлює всі адреси електронної пошти
        self.email = re.findall(r'[a-zA-Z0-9_.]+@[a-zA-Z]+[.][a-zA-Z]{2,}', data)
        # Відокремлює адресу контакту
        self.address = re.findall(r'\/[a-zA-Z-.\s]+\/[a-zA-Z0-9-.\s]+\/?[a-zA-Z0-9-.\s]*\/?[a-zA-Z0-9-.\s]*\/?[a-zA-Z0-9-.\s]*', data)


# Об'єкти класу "ім'я контакту"
class Name(Field):
    def __init__(self, name):
        super().__init__(name)

# Об'єкти класу "номер телефону"
class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)

# Обєкти класу "день народження"
class Birthday(Field):
    def __init__(self, birthday):
        super().__init__(birthday)

# Обєкти класу "електронна пошта"
class Email(Field):
    def __init__(self, email):
        super().__init__(email)

# Обєкти класу "адреса"
class Address(Field):
    def __init__(self, address):
        super().__init__(address)


# Уникання будь-яких помилок під час роботи програми
def input_error(func):
    def inner():
        flag = True
        while flag:
            try:
                result = func()
                flag = False
            except IndexError:
                print('Enter the name and numbers separated by a space.')
            except ValueError:
                print('I have no idea how you did it, try again.')
            except KeyError:
                print("The contact is missing.")
        return result
    return inner


# Головна функція, куди додаємо весь функціонал
@ input_error
def main():
    # Продовжуємо доповнювати вже існуючу адресну книгу, або ж створюємо нову з нуля
    try:
        with open("address_book.bin", "rb") as fh:
            CONTACTS = pickle.load(fh)
    except FileNotFoundError:
        CONTACTS = AddressBook()
    print(tutorial)
    bot_status = True
    # Умава, що забеспечує безкінечний цикл запиту, поки не буде виходу
    while bot_status:
        # Введення команди з консолі
        command = input('Enter the command: ').lower()
        # Додавання нового контакту
        if command.startswith('add'):
            command = command.removeprefix('add ')
            if Name(command).name in CONTACTS.data:
                print(CONTACTS.data[Name(command).name].add_phone(
                    Phone(command)))
            # Додавання нової інформації до вже існуючого контакту
            else:
                print(CONTACTS.add_record(
                    Record(Name(command), Phone(command), Birthday(command), Email(command), Address(command))))
        # Зміна номеру телефону у вже існуючому контакті
        elif command.startswith('change phone'):
            command = command.removeprefix('change phone ')
            print(CONTACTS.data[Name(command).name].change_phone(Phone(command)))
        # Видалення номеру телефону з вже існуючого контакту
        elif command.startswith('delete phone'):
            command = command.removeprefix('delete phone ')
            print(CONTACTS.data[Name(command).name].delete_phone(Phone(command)))
        # Зміна дня народження у вже існуючому контакті
        elif command.startswith('change birthday'):
            command = command.removeprefix('change birthday ')
            print(CONTACTS.data[Name(command).name].change_birthday(Birthday(command)))
        # Видалення дня народження з вже існуючого контакту
        elif command.startswith('delete birthday'):
            command = command.removeprefix('delete birthday ')
            print(CONTACTS.data[Name(command).name].delete_birthday(Birthday(command)))
        # Зміна email у вже існуючому контакті
        elif command.startswith('change email'):
            command = command.removeprefix('change email ')
            print(CONTACTS.data[Name(command).name].change_email(Email(command)))
        # Видалення email з вже існуючого контакту
        elif command.startswith('delete email'):
            command = command.removeprefix('delete email ')
            print(CONTACTS.data[Name(command).name].delete_email(Email(command)))
        # Зміна адреси у вже існуючому контакті
        elif command.startswith('change address'):
            command = command.removeprefix('change address ')
            print(CONTACTS.data[Name(command).name].change_address(Address(command)))
        # Видалення адреси з вже існуючого контакту
        elif command.startswith('delete address'):
            command = command.removeprefix('delete address ')
            print(CONTACTS.data[Name(command).name].delete_address(Address(command)))
        # Вивід всіх існуючих номерів телефону певного контакту (вказувати ім'я після пробілу)
        elif command.startswith('phone'):
            command = command.removeprefix('phone ')
            print(CONTACTS.show_number(Name(command)))
        # Вивід всіх існуючих контактів у адресній книзі
        elif command == "show all":
            if CONTACTS:
                for contact in CONTACTS.show_all():
                    print(contact)
            else:
                print('The contact list is empty.')
        # Вивід кількості днів до наступного дня народження певного контакту із тих, що маються
        elif command.startswith('when birthday'):
            command = command.removeprefix('when birthday ')
            print(CONTACTS.data[Name(command).name].days_to_birthday())
        elif command.startswith('days until birthday'):
            command = command.removeprefix('days until birthday: ')
            print(CONTACTS.birthday_after_n_days(command))
        # Пошук контакту за певною послідовністю літер або чисел
        elif command.startswith('find'):
            command = command.removeprefix('find ')
            CONTACTS.find(command)
        # Вихід із програми (сюди треба додати автоматичне збереження наявної адресної книги)
        elif command in ("good bye", "bye", "close", "exit", "end"):
            with open("address_book.bin", "wb") as fh:
                pickle.dump(CONTACTS, fh)
            print("The address book is saved to a file 'address_book.bin'. See You later!")
            bot_status = False
        # Якщо користувач некоректно ввів команду (тут можна реалізувати додаткове завдання з підказкою можливих команд)
        else:
            print("Enter correct command, please.")


if __name__ == '__main__':
    main()
