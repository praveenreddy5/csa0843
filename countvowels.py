word=input("enter the word:")
string=word.lower()
print(string)
count=0
list1=['a','e','i','o','u']
for i in string:
    if i in list1:
        count=count+1
print("number of vowels in given word is :",count)
