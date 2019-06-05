def master_yoda(text):
    my_list=text.split()
    reversed_word=my_list[::-1]
    return " ".join(reversed_word)

result = master_yoda('I am home')
print(result)
