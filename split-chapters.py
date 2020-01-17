book = ''
with open('Cleaned_Leonardo da Vinci by Walter Isaacson.txt', 'r') as inf:
    book = inf.read()

for chapterNum, chapter in enumerate(book.split('* * *')):
    fptr = None
    if chapterNum is 0:
        fptr = open('Leonardo da Vinci by Walter Isaacson - Intro.txt'.format(chapterNum), 'w')
    fptr = open('Leonardo da Vinci by Walter Isaacson - Chapter {}.txt'.format(chapterNum), 'w')
    fptr.write(chapter)
