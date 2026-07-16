print("============================ \n       WORD FREQUENCY \n============================")
sent = input("Enter a sentence :")
word = input("Enter a word to check it's frequency :")

count = 0

words = sent.split()

for w in words :
    if w == word :
        count = count + 1
print("Frequency :", count)
