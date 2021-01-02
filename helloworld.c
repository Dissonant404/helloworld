#include <stdio.h>

void main()
{
	char h[10]="Hello",e[10]="World",i,j;
	for(i=0;h[i]!='\0';++i);
	
	h[i]=' ';
	i=i+1;
	
	for(j=0; e[j]!='\0'; ++j, ++i)
	{
		h[i]=e[j];
	}
	printf("%s",h);
}

