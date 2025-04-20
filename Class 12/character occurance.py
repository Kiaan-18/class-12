string=input("Enter any word:")
char=input("Enter a character you want to count:")
i=0
count=0
while i<len(string):
    if string[i]==char:
        count=count+1
    i=i+1
print("The occurance of the given character is",count)
