notes = []

while True:
    print('Меню:')
    print('1. Додати нотатку')
    print('2. Вийти')

    choice = input('Введіть номер опції: ')

    if choice == '1':
        # Додавання та збереження нотатки
        title = input('Введіть заголовок нотатки: ')
        content = input('Введіть текст нотатки: ')
        note = {'title': title, 'content': content}
        notes.append(note)
        with open('notes.txt', 'w') as file:
            for note in notes:
                file.write(f"Заголовок: {note['title']}\n")
                file.write(f"Текст: {note['content']}\n")
                file.write('\n')
        print('Нотатка успішно додана та збережена!')

    elif choice == '2':
        # Вихід з програми
        break

    else:
        print('Невірний ввід. Будь ласка, спробуйте ще раз.')
