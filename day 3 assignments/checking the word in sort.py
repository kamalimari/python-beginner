word = input("enter the word")
word1=sorted(word)
word2=[]
for i in word:
    word2.append(i)
if word2 == word1:
    print(True)
else:
    print(False)
