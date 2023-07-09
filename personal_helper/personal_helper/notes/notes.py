notes = []

def add_note():
    # Додавання нотатки
    title = input('Enter a title for the note: ')
    content = input('Enter the note text: ')
    tags = input('Enter tags for the note (comma-separated, press Enter to skip): ')
   
    if tags:
        tags = [tag.strip() for tag in tags.split(',')]
        
    note = {'title': title, 'content': content, 'tags': tags}
    notes.append(note)
    save_notes()
    print('Note successfully added and saved!')
    
def edit_note():
    # Редагування нотатки
    title = input('Enter the title of the note to edit: ')
    note_found = False

    for note in notes:
        if note['title'] == title:
            new_title = input('Enter a new title for the note: ')
            new_content = input('Enter new note text: ')
            new_tags = input('Enter new tags for the note (comma-separated, press Enter to skip): ')
            
            if new_tags:
                new_tags = [tag.strip() for tag in new_tags.split(',')]
            
            note['title'] = new_title
            note['content'] = new_content
            note['tags'] = new_tags
            note_found = True
            break

    if note_found:
        save_notes()
        print('Note successfully edited and saved!')
    else:
        print('No note with this title was found.')

def delete_note():
    # Видалення нотатки
    title = input('Enter the title of the note to delete: ')
    note_found = False

    for note in notes:
        if note['title'] == title:
            notes.remove(note)
            note_found = True
            break

    if note_found:
        save_notes()
        print('Note successfully deleted!')
    else:
        print('No note with this title was found.')

def search_notes():
    # Пошук нотатків
    keyword = input('Enter a keyword to search: ')
    if found_notes := [
        note
        for note in notes
        if keyword.lower() in note['title'].lower()
        or keyword.lower() in note['content'].lower()
    ]:
        print('Found notes:')
        for note in found_notes:
            print(f"Title: {note['title']}")
            print(f"Text: {note['content']}")
            print()
    else:
        print('No notes found.')


def sort_notes_by_tag():
    # Сортування нотаток за тегами
    tags = set()
    for note in notes:
        if note['tags']:
            tags.update(note['tags'])
    tags_list = list(tags)

    print('Available tags:')
    for i, tag in enumerate(tags_list):
        print(f'{i + 1}. {tag}')

    choice = input('Enter the tag number to sort notes: ')
    if choice.isdigit() and int(choice) in range(1, len(tags_list) + 1):
        tag = tags_list[int(choice) - 1]
        if sorted_notes := [
            note
            for note in notes
            if note['tags']
            and tag.lower() in [t.lower() for t in note['tags']]
        ]:
            print('Sorted notes:')
            for note in sorted_notes:
                print(f"Title: {note['title']}")
                print(f"Text: {note['content']}")
                print(f"Tags: {', '.join(note['tags'])}")
                print()
        else:
            print('No notes found with this tag.')
    else:
        print('Invalid tag number.')

def save_notes():
    # Збереження нотаток у файл
    with open('notes.txt', 'w') as file:
        for note in notes:
            file.write(f"Title: {note['title']}\n")
            file.write(f"Text: {note['content']}\n")
            if note['tags']:
                file.write(f"Tags: {', '.join(note['tags'])}\n")
            file.write('\n')


def load_notes():
    # Завантаження нотаток з файлу
    notes.clear()
    try:
        with open('notes.txt', 'r') as file:
            lines = file.readlines()
            title = ''
            content = ''
            tags = []

            for line in lines:
                if line.startswith('Title: '):
                    title = line[7:].strip()
                elif line.startswith('Text: '):
                    content = line[6:].strip()
                elif line.startswith('Tags: '):
                    tags = [tag.strip() for tag in line[6:].split(',')]
                elif line == '\n':
                    note = {'title': title, 'content': content, 'tags': tags}
                    notes.append(note)
                    title = ''
                    content = ''
                    tags = []
    except FileNotFoundError:
        pass

def main():
    load_notes()

    while True:
        print('Menu:')
        print('1. Add a note')
        print('2. Edit note')
        print('3. Delete note')
        print('4. Search notes')
        print('5. Sort notes by tags')
        print('6. Go out')

        choice = input('Enter the option number: ')

        if choice == '1':
            add_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            search_notes()
        elif choice == '5':
            sort_notes_by_tag()
        elif choice == '6':
            break
        else:
            print('Invalid input. Please try again.')

if __name__ == "__main__":
    main()
