#Ryan McDowell
#8/19/21
#Practicing analyzing multiple files in Python.

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        #Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

book_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for book in book_names:
    count_words(book)