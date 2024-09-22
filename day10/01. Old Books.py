book = input()
count_books = 0
threshold_text = 'No More Books'

is_book_found = False

searched_book = input()
while searched_book != threshold_text:
    if searched_book == book:
        is_book_found = True
        print(f'You checked {count_books} books and found it.')
        break
    count_books += 1
    searched_book = input()
if not is_book_found:
    print(f'The book you search is not here!')
    print(f'You checked {count_books} books.')
