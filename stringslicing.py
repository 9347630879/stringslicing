name = "fullstuack"
print(name[0:5])
print(name[1:3])
print(name[:])
print(name[:3])
print(name[1:])
print(name[-8:-1])
print(name[-8:])
print(name[:-1])

#list data types
#impliciit
attendences = ["dhanunjai","sai","sundhar"]
print(type(attendences))

#explicit

attendences =list( ["dhanunjai","sai","sundhar"])
print(type(attendences))

#datatype \variable annotation

attendences:list = ["dhanunjai","sai","sundhar"]
print(type(attendences))

#reverse a string

name = "sai sundhar"
reversed = name[::-1]
print(reversed)

#reversee a string without a slicing
n= "sai"
string_a = " "
for i in n:
    string_a = i + string_a
print(string_a)

#wreverse alist
names = ["dhanunjai","sai","sundhar"]
print(names[::-1])
