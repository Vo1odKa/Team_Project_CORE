notes = []

while True:
    print('Меню:')
    print('1. Додати нотатку')
    print('2. Вийти')

    choice = input('Введіть номер опції: ')

    if choice == '1':
        # Додавання нової нотатки
        title = input('Введіть заголовок нотатки: ')
        content = input('Введіть текст нотатки: ')
        note = {'title': title, 'content': content}
        notes.append(note)
        print('Нотатка успішно додана!')

    elif choice == '2':
        # Збереження нотаток у файл
        with open('notes.txt', 'w') as file:
            for note in notes:
                file.write(f"Заголовок: {note['title']}\n")
                file.write(f"Текст: {note['content']}\n")
                file.write('\n')
        print('Нотатки збережені у файлі notes.txt')
        break

    else:
        print('Невірний ввід. Будь ласка, спробуйте ще раз.')
