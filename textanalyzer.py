def text_analyzer():
    #splitting of the words
    words = [word.strip() for word in text.split()]

    #unique words using a set
    unique_words = set(words)

    #word frequencies
    word_freq = {word: words.count(word) for word in unique_words}

    #character count
    char_count = len(text.replace(" ", ""))

    #Displaying the results
    print("Text Analysis of your given paragraph: ")
    print("Total words in the paragraph: ",words)
    print("Total unique words in the paragraph: ",unique_words)
    print("The character count of the paragraph is: ",char_count)
    print("The word frequency in the paragraph is: ",word_freq)
    print("The above result might be clumsy, If you have the patience then, please go through it...")

text = input("Enter your custom paragraph: ") 
text_analyzer()    
