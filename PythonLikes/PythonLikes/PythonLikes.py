def likes(likers):
    if len(likers) > 3: return f'{str(likers[0])}, {str(likers[1])} and {len(likers)-2} others like this'
    if len(likers) > 2: return f'{str(likers[0])}, {str(likers[1])} and {str(likers[2])} like this'
    if len(likers) > 1: return f'{str(likers[0])} and {str(likers[1])} like this'
    if len(likers) > 0: return f'{str(likers[0])} likes this'
    else: return 'no one likes this'

# test cases:
print("test: 6 people like it")
print(likes(["Carl","Carol","Peter","Peggy","Frank","Felicia"]))
print("***")
print("test: 5 people like it")
print(likes(["Carol","Peter","Peggy","Frank","Felicia"]))
print("***")
print("test: 4 people like it")
print(likes(["Peter","Peggy","Frank","Felicia"]))
print("***")
print("test: 3 people like it")
print(likes(["Peggy","Frank","Felicia"]))
print("***")
print("test: 2 people like it")
print(likes(["Frank","Felicia"]))
print("***")
print("test: 1 people like it")
print(likes(["Felicia"]))
print("***")
print("test: 0 people like it")
print(likes([]))
print("***")