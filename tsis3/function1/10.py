
def duplicates(mylist):
    mylist = list(dict.fromkeys(mylist))
    print(mylist)
line=input()
words=line.split(' ')
numbers=[str(i) for i in words]
duplicates(numbers)
