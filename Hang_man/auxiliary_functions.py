"""Auxiliary functions for the Hangman game."""

def load_book(file_path:str) -> list:
    """Load a book from a text file and return a list of words."""
    with open(file_path, 'r' , encoding='utf-8') as file:
       words = file.read().split()
    return words
      
def clean_list_of_words(word_list:list) -> list:
    """Clean a list of words by removing punctuation and converting to lowercase."""
    cleaned_words = []
    # my code to clean the word list 
    for word in word_list[0:100]:
      word = word.lower().strip(".,*,$,!?;:\"'()[]{}<>,1234567890")
      #print(word)
      cleaned_words.append(word)
    return cleaned_words

def reduce_list(word_list:list, max_words:int) -> list:
    """Reduce the list of words to a maximum number of words."""
    return word_list[:max_words]


if __name__ == "__main__":
    # Example usage
    book_path = "C:\\Users\\mario\\Documentos\\desarrollo4\\curso_ds4_2026\\Hang_man\\Dracula.txt"
    words = load_book(book_path)
    print(len(words))
    print(len(words[0]))
    #print(words[0])
    #print(words[:200])
    cleaned_words = clean_list_of_words(words)
    print(cleaned_words)
    print("number of words in the cleaned list:", len(cleaned_words))