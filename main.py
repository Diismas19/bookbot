import sys
from stats import get_num_words, get_caracters_count,output

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as book:
        book_contents=book.read()
    return book_contents
    
def main():
    book_text=get_book_text(sys.argv[-1])
    output(get_caracters_count(book_text),get_num_words(book_text),sys.argv[-1])

main()