# s = "bahubali"
# s1=  "ali"
# if s1 in s:
#     print(s.index(s1))
# else:
#     print("not")

# s = "hello how are you "
# l = []
# s1 = ""

# for i in s:
#     if i == " ":
#         l.append(s1)
#         s1 = ""
#     else:
#         s1 += i
# print(l)


d = {"a" : 1, "b" : 22, "c" : 13, "d" : 45, "e" : 2}
b = 0
for i in d:
    if d[i] > b:
        b = d[i]
        s = i
print(s)

# d1 = {"a" : 1, "b" : 22, "c" : 13, "d" : 45, "e" : 2}
# d2 = {"b" : 21, "c" : 2, "d" : 5, "f" : 33, "g" : 8}

# for i in d1.keys():
#     if i in d2.keys():
#         d2[i] += d1[i]
#     else:
#         d2[i] = d1[i]
# print(d2)

# s = "dsvndsbidndsbvyqkwk"
# d = {}
# for i in s:
#     count = 0
#     if i not in d:
        
#         count += 1
# print(d[i])