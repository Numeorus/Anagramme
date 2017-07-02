#tools function

def createLetters(word):
	letterList=[]
	for iLetter in range(0,len(word)-1):
		if word[iLetter] not in letterList:
			letterList.append(word[iLetter])
	return letterList


def getOccurences(word,letterList):
	letterOccurence=[]
	for iLetter in range(0,len(letterList)):
		letterOccurence.append(word.count(letterList[iLetter]))
	return letterOccurence

def compareLetters (letterList, letterOccurence, toCompare):
	for iLetter in range (0,len(letterList)):
		if letterList[iLetter] not in toCompare:
			return False
		if toCompare.count(letterList[iLetter])!=letterOccurence[iLetter]:
			return False
	return True

#main function
import sys

wordList=[]

with open('wordlist.txt') as openfileobject:
    for line in openfileobject:
        wordList.append(line)

n=1
while True:
	status=0
	if len(wordList)==0:
		break
	tmpWord=wordList[0]
	del wordList[0]
	stOut=str(n)+':'+tmpWord
	L=createLetters(tmpWord)
	I=getOccurences(tmpWord,L)
	for currentWord in wordList:
		if len(tmpWord)==len(currentWord):
			if compareLetters(L,I,currentWord)==True:
				stOut+=" "+currentWord
				del currentWord
				status=1
	
	if status==1:
		print stOut
		n+=1
	
