#tools function


def compareLetters (pattern, toCompare):
	for letter in pattern:
		if letter not in toCompare:
			return False
		else:#letter is in
			if toCompare.count(letter) != pattern.count(letter):
				return False

	return True

#main function
import linecache
wordList=[]

n=1
fd=open("wordlist.txt","r")

with open('wordlist.txt') as f:
    fileSize=sum(1 for _ in f)

for i in range (1,fileSize):
	status=0
	line=linecache.getline("wordlist.txt", i)
	stOut=str(n)+':'+line
	for j in range(i+1,fileSize):
		currentWord=linecache.getline("wordlist.txt", j)
		if len(line)==len(currentWord):
			if compareLetters(line,currentWord)==True:
				stOut+=" "+currentWord
				del currentWord
				status=1

	if status==1:
		print stOut
		n+=1
	print i