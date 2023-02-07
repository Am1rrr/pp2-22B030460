def palindrome(a):
    txt= a[::-1]
    if txt==txt[::-1]:
        print('Yes')
    else:
        print('No')
palindrome(str(input()))
