a = int(input())
b = int(input())

def squares(a,b):
    for i in range(a,b+1):
        yield i**2
        tttt
print(*squares(a,b), ' ')