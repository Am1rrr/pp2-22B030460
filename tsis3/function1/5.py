def permutations(string):
    if len(string) == 0:
        return ['']
    prev_list = permutations(string[1:len(string)])
    next_list = []
    for i in range(len(prev_list)):
        for j in range(len(string)):
            new_string = prev_list[i][0: j] + string[0] + prev_list[i][j: len(string) - 1]
            if new_string not in next_list:
                next_list.append(new_string)
    return next_list

string = input("Enter a string: ")
print("All permutations of given string are: ")
result = permutations(string)
for s in result:
    print(s)
