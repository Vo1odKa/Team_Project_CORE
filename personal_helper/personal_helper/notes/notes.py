def add_note(notes):
    # Додавання та збереження нотатки
    title = input('Enter a title for the note: ')
    content = input('Enter the note text: ')
    tags = input('Enter tags for the note (comma-separated, press Enter to skip): ')
   
    if tags:
        tags = [tag.strip() for tag in tags.split(',')]
        
    note = {'title': title, 'content': content, 'tags': tags}
    notes.append(note)
    with open('notes.txt', 'a') as file:
        file.write(f"Title: {note['title']}\n")
        file.write(f"Text: {note['content']}\n")
        if tags:
            file.write(f"Tags: {', '.join(note['tags'])}\n")
        file.write('\n')
    print('Note successfully added and saved!')
    return notes

def edit_note(notes):
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
        with open('notes.txt', 'w') as file:
            for note in notes:
                file.write(f"Title: {note['title']}\n")
                file.write(f"Text: {note['content']}\n")
                if note['tags']:
                    file.write(f"Tags: {', '.join(note['tags'])}\n")
                file.write('\n')
        print('Note successfully edited and saved!')
    else:
        print('No note with this title was found.')

def delete_note(notes):
    # Видалення нотатки
    title = input('Enter the title of the note to delete: ')
    note_found = False

    for note in notes:
        if note['title'] == title:
            notes.remove(note)
            note_found = True
            break

    if note_found:
        with open('notes.txt', 'w') as file:
            for note in notes:
                file.write(f"Title: {note['title']}\n")
                file.write(f"Text: {note['content']}\n")
                if note['tags']:
                    file.write(f"Tags: {', '.join(note['tags'])}\n")
                file.write('\n')
        print('Note successfully deleted!')
    else:
        print('No note with this title was found.')

def search_notes(notes):
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

def main():
    notes = []

    while True:
        print('Menu:')
        print('1. Add a note')
        print('2. Edit note')
        print('3. Delete note')
        print('4. Search notes')  
        print('5. Go out')

        choice = input('Enter the option number: ')

        if choice == '1':
            notes = add_note(notes)
        elif choice == '2':
            edit_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            search_notes(notes) 
        elif choice == '5':
            break
        else:
            print('Invalid input. Please try again.')

if __name__ == "__main__":
    main()