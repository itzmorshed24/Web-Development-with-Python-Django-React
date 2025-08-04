"""
#List
fruits = ['apple', 'banana', 'cherry']


#starting point, ending point condition, increment

index = 0
while index<len(fruits):
    print(fruits[index])
    index = index+1
#String
word ="Hello"
index=0
while index<len(word):
    print(word[index])
    index = index+1

    #Range

index = 0
end = 10
while index<end:

    if index == 5:
        index = index+1
        continue
    print(index)
    index = index+1

"""
#dictionary

examResult = {"Physics":98, "Math": 88, "Bangla": 78}
keys=list(examResult.keys())

index = 0
while index<len(keys):
    eachkey=keys[index]
    print(examResult[eachkey])
    index = index+1
