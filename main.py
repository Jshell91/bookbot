def main():

        report("books/frankenstein.txt")
        

def words_count(string):
    words = string.split()
    return len(words)

def char_count(string):
    lowered = string.lower()
    dictionary = {}
    for char in lowered:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] +=1
    return dictionary

def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def report(path):
    
    book = read_book(path)
    dictionary = char_count(book)
    words = words_count(book)

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    for i in dictionary:
        print(f"The '{i}' character was found {dictionary[i]} times")
    
    print("--- End report --- ")



main()