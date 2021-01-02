#include <stdio.h>

void main()
{
	char h[10]="Hello",e[10]="World",i,j;
	for(i=0;h[i]!='\0';++i);
	//printf("%d" "%s",i,h[i]);
	
	h[i]=' ';
	//printf("%d" "%c",i,h[i]);
	
	i=i+1;
	//printf("%d" "%c",i,h[i]);
	
	for(j=0; e[j]!='\0'; ++j, ++i)
	{
		h[i]=e[j];
	}
	printf("%s",h);

	printf("%c",x);
	int i;
	for (i=0;i<=127;i++)
	
	{
		i=(char)i;
		printf("\n %c",i);
	}
}

