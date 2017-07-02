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
	for currentWord in wordList:
		if len(tmpWord)==len(currentWord):
			if compareLetters(tmpWord,currentWord)==True:
				stOut+=" "+currentWord
				del currentWord
				status=1
	
	if status==1:
		print stOut
		n+=1
	break
