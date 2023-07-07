notes = []

while True:
    print('Menu:')
    print('1. Add a note')
    print('2. Go out')

    choice = input('Enter the option number: ')

    if choice == '1':
       # Додавання та збереження нотатки
        title = input('Enter a title for the note: ')
        content = input('Enter the note text: ')
        note = {'title': title, 'content': content}
        notes.append(note)
        with open('notes.txt', 'a') as file:
            file.write(f"Title: {note['title']}\n")
            file.write(f"Text: {note['content']}\n")
            file.write('\n')
        print('Note successfully added and saved!')

    elif choice == '2':
        # Вихід з програми
        break

    else:
        print('Invalid input. Please try again.')