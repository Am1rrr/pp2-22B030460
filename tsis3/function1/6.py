def reverse_words(string):
    s = string.split()[::-1]
    l = []
    for i in s:
        l.append(i)
    return " ".join(l)

string = input("Enter a string: ")
print(reverse_words(string))
