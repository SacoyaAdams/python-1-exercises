
# the function accepts two parameters, one is a string(sentence) and the 2nd is a ! to replace the .
# ! is a string data type
def replace_period(sentence, punctuation):
    # print(list(sentence))
    # change the string to a list, so i can mutate
    new_list = list(sentence)
    # iterate thru the list using the index for access to the index and element
    for index in range(len(new_list)):
        # print(index)
        # condition, if the element at that index is a "." then reassign it to a "!"
        if new_list[index] == '.':
            new_list[index] = punctuation
    # print the new list joined back together as a sentence
    print("".join(new_list))

        # no need for an else statement
    # return the new sentence


