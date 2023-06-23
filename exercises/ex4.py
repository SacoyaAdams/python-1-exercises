# pass the function a parameter (sentence)


def count_words():
    # make an input that receives a sentence
    sentence = input("Enter sentence: ")
    # create a counter  ( set counter to 0, count each word and add (increment) to the counter)
    counter = 0
    # iterate thru sentence (for loop)
    # print(sentence)
    for word in sentence.split():
        # must happen within the for loop
        # print(word)
        # count each word and add 1 to the counter, doesn't include any space
        counter += 1
    # returns the value of the counter
    print(f"Number of words: {counter}")