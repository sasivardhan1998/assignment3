str= "marolix technology"
print("The input string is:",str)
myDict=dict()
for character in str:
    if character in myDict:
        myDict[character]+=1
    else:
        myDict[character]=1
print("The dictionary created from characters of the string is:")
print(myDict)