import re

oneline_book_text = ''

with open('leo-ch3-sample.txt', 'r') as book:
  oneline_book_text = book.read()

# replace each ?, !, or . with that punctuation mark and a newline
# could do a regex split and join the resulting list with newline too
multiline_book_text = oneline_book_text.replace('!', '!\n')
multiline_book_text = multiline_book_text.replace('.', '.\n')
multiline_book_text = multiline_book_text.replace('?', '?\n')

with open('leo-ch3-multiline.txt', 'w') as multiline_book:
    multiline_book.write(multiline_book_text)
