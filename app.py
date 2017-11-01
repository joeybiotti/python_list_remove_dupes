a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 3, 5, 8, 6, 6]
b = []

print(a)
print("#########################")


def no_dupes(a, b):
    for i in a:
        if i not in b:
            b.append(i)
        print(b)
    
no_dupes(a, b)