#include <string.h>
#include <stdio.h>


#define FILENAME "wordlist.txt"

int getOccurence (char* string, char pattern, int len)
{
	int count=0;
	int i=0;

	for (i=0;i<len;i++)
		if(*(string+i)==pattern)
			count++;

	return count;
}

int isAnagram (char* first, char* second)
{
	int i=0;
	int j=0;
	int k=0;
	int lenFirst=strlen(first);
	int lenSecond=strlen(second);


	if (lenFirst!=lenSecond)		
		return 0;

	for (i=0;i<strlen(first);i++)
	{	
		j=getOccurence (first, *(first+i), lenFirst);
		k=getOccurence (second,*(first+i) , lenSecond);
		if (j!=k)
			return 0;
	}

	return 1;
}

int printAnagram(char* first, FILE* fd)
{
	char second[100]="\0";
	int status=0;
	char strAnagram[300]="\0";

	strcat(strAnagram,first);
	while (second!=NULL)
	{
		if (fgets(second,sizeof(second),fd)==NULL)
				break;
		if(isAnagram(first,second)!=0){
			status=1;
			sprintf(strAnagram+strlen(strAnagram),"\t%s",second);
		}
		break;
	}
	if(status)
	{
		strcat(strAnagram,"\n");
		printf("%s\n",strAnagram);
	}
}

int main(void)
{
	FILE* fd=fopen(FILENAME,"r");
	char line[100]="\0";
	off_t currentPos=0;

	int i=0;

	//printf("%d\n",isAnagram("test","estt"));;
	if (fd!=NULL)
	{
		while (line!=NULL)
		{
			if (fgets(line,sizeof(line),fd)==NULL)
				break;
			 currentPos=ftello(fd);
			 printAnagram(line,fd);
			 fseek(fd, currentPos, SEEK_SET);
		}
	}
	else
		printf("error\n");
	return 0;
}