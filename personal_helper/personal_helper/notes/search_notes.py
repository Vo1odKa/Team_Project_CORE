"""
The code now includes a new feature to search for notes based on a keyword.
When the user selects the option to search notes, they can enter a keyword,
and the program will find and display the notes containing the keyword in their titles or contents.
The search is case-insensitive, meaning it will match regardless of the letter casing.
The matching notes' titles and contents are then printed on the screen.
If no matching notes are found, a "No notes found" message is displayed.
"""

def search_notes(notes):
    keyword = input('Enter a keyword to search: ')
    found_notes = []

    for note in notes:
        if keyword.lower() in note['title'].lower() or keyword.lower() in note['content'].lower():
            found_notes.append(note)

    if found_notes:
        print('Found notes:')
        for note in found_notes:
            print(f"Title: {note['title']}")
            print(f"Text: {note['content']}")
            print()
    else:
        print('No notes found.')


if __name__ == "__main__":
    
    notes = [
        {'title': 'Note 1', 'content': 'This is the content of note 1.'},
        {'title': 'Note 2', 'content': 'This is the content of note 2.'},
        {'title': 'Note 3', 'content': 'This is the content of note 3.'}
    ]

    search_notes(notes)

